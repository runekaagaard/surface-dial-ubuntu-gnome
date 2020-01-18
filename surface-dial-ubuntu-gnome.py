#!/usr/bin/env python3

import os
import os.path
import sys

from errno import ENOENT
from evdev import InputDevice, UInput
from evdev.events import InputEvent
from evdev.ecodes import EV_KEY, EV_REL, REL_WHEEL, REL_WHEEL_HI_RES, BTN_MOUSE
from signal import signal, SIGINT

# Automatically discover the device.
for name in os.listdir('/dev/input'):
    if not name.startswith('event'):
        continue

    dev = InputDevice('/dev/input/' + name)
    if dev.name == "Surface Dial System Multi Axis":
        print("Found surface dial at", dev.path)
        break
else:
    print("Could not find Surface Dial, please pair it and try again.")
    sys.exit(-ENOENT)


def on_exit(s, f):
    dev.ungrab()
    sys.exit(0)


# Take over complete control over the device - no events will be passed to
# other listeners. They are relayed to the virtual stylus created above.
signal(SIGINT, on_exit)
dev.grab()

cap = {
    EV_REL: [REL_WHEEL, REL_WHEEL_HI_RES],
    EV_KEY: [BTN_MOUSE],
}


def write(ui, event, _type, code, value):
    ui.write_event(InputEvent(event.sec, event.usec, _type, code, value))
    ui.syn()


try:
    with UInput(cap) as ui:
        for event in dev.read_loop():
            if (event.code == 7 and event.type == EV_REL and event.value < 0):
                print("TURN COUNTER CLOCKWISE")
                if event.value != -1:
                    print("    UNEXPECTED COUNTER CLOCKWISE VALUE",
                          event.value)
                write(ui, event, EV_REL, REL_WHEEL_HI_RES, event.value*120)

            elif (event.code == 7 and event.type == EV_REL
                  and event.value > 0):
                print("TURN CLOCKWISE")
                if event.value != 1:
                    print("    UNEXPECTED CLOCKWISE VALUE", event.value*120)
                write(ui, event, EV_REL, REL_WHEEL_HI_RES, event.value)
            elif (event.code == 256 and event.type == EV_KEY
                  and event.value == 1):
                print("CLICK DOWN")
                write(ui, event, EV_KEY, BTN_MOUSE, event.value)
            elif (event.code == 256 and event.type == EV_KEY
                  and event.value == 0):
                print("CLICK UP")
                write(ui, event, EV_KEY, BTN_MOUSE, 0)
finally:
    dev.ungrab()
