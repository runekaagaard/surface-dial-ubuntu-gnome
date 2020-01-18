# Welcome to surface-dial-ubuntu-gnome

Work in progress. It's currently hardcoded to the following events:

- rotate counter clockwise: Mouse scroll up
- rotate clockwise: Mouse scroll down
- pressed/released: Mouse pressed/released 

# Usage

You need to install version 1.2.0 of `python-evdev` or higher. Unfortunately,
most distributions seem to package 1.1.2, so you might have to force an update.

```bash
$ sudo pip3 install -U evdev
$ sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
$ sudo apt install gir1.2-appindicator3-0.1
$ sudo apt install libglib2.0-dev libgtk2.0-dev gtk+-3.0
sudo apt-get install libgtk-3-dev
sudo apt install python3-tk
```

Make sure it's paired via bluetooth and then simply run:

```bash
$ sudo ./surface-dial-ubuntu-gnome.py
```

## Acknowledgements

Based of https://github.com/linux-surface/surface-fix-eraser by @StollD.
