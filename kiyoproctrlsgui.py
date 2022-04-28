#!/usr/bin/env python3

import os, logging, sys, webbrowser
from kiyoproctrls import KiyoProCtrls, find_usb_ids_in_sysfs

try:
    from tkinter import Tk, ttk, PhotoImage
except Exception as e:
    logging.error(f'tkinter import failed: {e}, please install the python3-tk package')
    sys.exit(3)

v4ldir = '/dev/v4l/by-id/'
ghurl = 'https://github.com/soyersoyer/kiyoproctrls'


def get_kiyo_pro_devices(dir):
    if not os.path.isdir(dir):
        return []
    devices = os.listdir(dir)
    devices.sort()
    devices = list(filter(lambda device: find_usb_ids_in_sysfs(dir + device) == KiyoProCtrls.KIYO_PRO_USB_ID, devices))
    return devices

class KiyoProCtrlsGui:
    def __init__(self):
        self.devices = []
        
        self.fd = 0
        self.device = ''
        self.kiyo_pro = None

        self.window = None
        self.kpimg = None
        self.frame = None
        self.devicescb = None

        self.init_window()
        self.refresh_devices()

    def init_window(self):
        self.window = Tk(className='kiyoproctrls')
        self.kpsmallimg = PhotoImage(file='kiyopro_240.png')
        self.kpimg = PhotoImage(file='kiyopro_big.png')
        self.window.wm_iconphoto(True, self.kpsmallimg)
        self.window.title('kiyoproctrls')
        self.window.winfo_toplevel().title('kiyoproctrls')
        
        ttk.Label(self.window, image=self.kpimg, padding=10).grid()
        gh = ttk.Label(self.frame, text='Github page', foreground='blue', cursor='hand2', padding=5)
        gh.grid(sticky='NW', row=0)
        gh.bind('<Button-1>', lambda e: webbrowser.open(ghurl))

    def refresh_devices(self):
        self.devices = get_kiyo_pro_devices(v4ldir)
        if self.device not in self.devices:
            self.close_device()
            if len(self.devices):
                self.open_device(self.devices[0])
            self.init_gui_device()
        if self.devicescb:
            self.devicescb['values'] = self.devices

    def gui_open_device(self, device):
        self.close_device()
        self.open_device(device)
        self.init_gui_device()

    def open_device(self, device):
        devpath = v4ldir + device
        logging.info(f'opening device: {device}')
        
        try:
            self.fd = os.open(devpath, os.O_RDWR, 0)
        except Exception as e:
            logging.error(f'os.open({devpath}, os.O_RDWR, 0) failed: {e}')

        self.kiyo_pro = KiyoProCtrls(devpath, self.fd)
        self.device = device

    def close_device(self):
        if self.fd:
            os.close(self.fd)
            self.fd = 0
            self.device = ''
            self.kiyo_pro = None

    def init_gui_device(self):
        if self.frame:
            self.frame.destroy()
            self.frame = None
            self.devicescb = None

        self.frame = ttk.Frame(self.window, padding=10)
        self.frame.grid()

        if len(self.devices) == 0:
            ttk.Label(self.frame, text='0 device found', padding=10).grid()
            ttk.Button(self.frame, text='Refresh', command=self.refresh_devices).grid(sticky='NESW')
            return

        self.devicescb = ttk.Combobox(self.frame, state='readonly', values=self.devices, postcommand=self.refresh_devices)
        self.devicescb.set(self.device)
        self.devicescb.grid(sticky='NESW', pady=10)
        self.devicescb.bind('<<ComboboxSelected>>', lambda e: self.gui_open_device(self.devicescb.get()))

        ctrls = ttk.Frame(self.frame)
        ctrls.grid()

        ttk.Label(ctrls, text='AF Mode').grid(column=0, row=0, sticky='W')
        ttk.Button(ctrls, text='Passive', command=lambda: self.kiyo_pro.setup_ctrls({'af_mode': 'passive'}) ).grid(column=1, row=0, sticky='NESW')
        ttk.Button(ctrls, text='Responsive', command=lambda: self.kiyo_pro.setup_ctrls({'af_mode': 'responsive'})).grid(column=2, row=0, sticky='NESW')

        ttk.Label(ctrls, text='HDR', width=10).grid(column=0, row=1, sticky='W')
        ttk.Button(ctrls, text='Off', command=lambda: self.kiyo_pro.setup_ctrls({'hdr': 'off'})).grid(column=1, row=1, sticky='NESW')
        ttk.Button(ctrls, text='On', command=lambda: self.kiyo_pro.setup_ctrls({'hdr': 'on'})).grid(column=2, row=1, sticky='NESW')

        ttk.Label(ctrls, text='HDR Mode').grid(column=0, row=2, sticky='W')
        ttk.Button(ctrls, text='Dark', command=lambda: self.kiyo_pro.setup_ctrls({'hdr_mode': 'dark'})).grid(column=1, row=2, sticky='NESW')
        ttk.Button(ctrls, text='Bright', command=lambda: self.kiyo_pro.setup_ctrls({'hdr_mode': 'bright'})).grid(column=2, row=2, sticky='NESW')

        ttk.Label(ctrls, text='FoV').grid(column=0, row=3, sticky='W')
        ttk.Button(ctrls, text='Narrow', command=lambda: self.kiyo_pro.setup_ctrls({'fov': 'narrow'})).grid(column=1, row=3, sticky='NESW')
        ttk.Button(ctrls, text='Medium', command=lambda: self.kiyo_pro.setup_ctrls({'fov': 'medium'})).grid(column=2, row=3, sticky='NESW')
        ttk.Button(ctrls, text='Wide', command=lambda: self.kiyo_pro.setup_ctrls({'fov': 'wide'})).grid(column=3, row=3, sticky='NESW')

    def start(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = KiyoProCtrlsGui()
    gui.start()
