# kiyoproctrls
Razer Kiyo Pro controls for Linux

It's a standalone Python script to set the Razer Kiyo Pro custom controls (HDR, HDR mode, FoV, AF mode).
Extracted from the [fmp4streamer](https://github.com/soyersoyer/fmp4streamer) project.

```
$ python3 kiyoproctrls.py
usage: python3 kiyoproctrls.py [--help] [-d DEVICE] [--list] [-c CONTROLS]

optional arguments:
  -h, --help    show this help message and exit
  -d DEVICE     use DEVICE, default /dev/video0
  -l, --list    list the controls and values
  -c CONTROLS   set CONTROLS (eg.: hdr=on,fov=wide)

example:
  python3 kiyoproctrls.py -c hdr=on,hdr_mode=dark,af_mode=passive,fov=wide
```
