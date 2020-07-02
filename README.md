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
```

Download the Repo and extract it

```bash
cd ~/Downloads && wget https://github.com/runekaagaard/surface-dial-ubuntu-gnome/archive/master.zip
```

Using  the command below unzip, and move the program file to your home directory.

```bash
~/Downloads$ unzip master.zip && mv ~/Downloads/surface-dial-ubuntu-gnome-master/surface-dial-ubuntu-gnome.py ~/ && cd ~
```

Make sure the Dial is paired via bluetooth, then simply run the command:

```bash
$ sudo ./surface-dial-ubuntu-gnome.py
```

## Acknowledgements

Based of https://github.com/linux-surface/surface-fix-eraser by @StollD.