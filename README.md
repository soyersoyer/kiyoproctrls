### The project has been merged into the [cameractrls](https://github.com/soyersoyer/cameractrls) project.
# kiyoproctrls
Razer Kiyo Pro controls for Linux

It's a standalone Python script to set the Razer Kiyo Pro custom controls (HDR, HDR mode, FoV, AF mode).
Extracted from the [fmp4streamer](https://github.com/soyersoyer/fmp4streamer) project.

```shell
git clone https://github.com/soyersoyer/kiyoproctrls.git
cd kiyoproctrls
./kiyoproctrls.py
usage: ./kiyoproctrls.py [--help] [-d DEVICE] [--list] [-c CONTROLS]

optional arguments:
  -h, --help    show this help message and exit
  -d DEVICE     use DEVICE, default /dev/video0
  -l, --list    list the controls and values
  -c CONTROLS   set CONTROLS (eg.: hdr=on,fov=wide)

example:
  ./kiyoproctrls.py -c hdr=on,hdr_mode=dark,af_mode=passive,fov=wide
```


# kiyoproctrlsgui
GUI for the Razer Kiyo Pro controls

![kiyoproctrls launcher](https://github.com/soyersoyer/kiyoproctrls/raw/main/gui_launcher.png)

![kiyoproctrls screen](https://github.com/soyersoyer/kiyoproctrls/raw/main/gui_screen.png)

### GUI install

Install the tkinter GUI framework:
```shell
sudo apt install python3-tk
```

Clone the repo:
```shell
git clone https://github.com/soyersoyer/kiyoproctrls.git
```

Add the desktop file to the launcher
```shell
cd kiyoproctrls
desktop-file-install --dir=$HOME/.local/share/applications \
--set-icon="$PWD/kiyopro_240.png" \
--set-key=Exec --set-value="$PWD/kiyoproctrlsgui.py" \
--set-key=Path --set-value="$PWD" \
kiyoproctrls.desktop
```

Run from the launcher or from the shell
```shell
./kiyoproctrlsgui.py
```
