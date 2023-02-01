import pynput.keyboard
import csv
import pandas as pd
import numpy as np
import time
import random

keys = []
keyboard = pynput.keyboard.Controller()


def save_csv(name: str = "key_logger"):
    try:
        name = name + ".csv"
        print(f"Csv file name: {name}")
        df = pd.DataFrame(keys)
        df.to_csv(name, index=False)
        return True
    except Exception as e:
        print(f"Error exporting csv: {e}")
        return False


def on_press(key):
    keys.append(str(key))
    print(f"Key {key} pressed")


def on_release(key):
    print(f"Key {key} released")
    if str(key) == "Key.esc":
        # Save in csv
        save_csv("key_logger")
        return False


def listener_key():
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def simulate_key_press(key):
    try:
        time.sleep(random.randint(0, 2))
        keyboard.press(key)
        keyboard.release(key)
    except AttributeError:
        special_keys = {
            "Key.alt_l": keyboard.Key.alt_l,
            "Key.alt_r": keyboard.Key.alt_r,
            "Key.backspace": keyboard.Key.backspace,
            "Key.cmd": keyboard.Key.cmd,
            "Key.ctrl_l": keyboard.Key.ctrl_l,
            "Key.ctrl_r": keyboard.Key.ctrl_r,
            "Key.delete": keyboard.Key.delete,
            "Key.down": keyboard.Key.down,
            "Key.end": keyboard.Key.end,
            "Key.enter": keyboard.Key.enter,
            "Key.esc": keyboard.Key.esc,
            "Key.f1": keyboard.Key.f1,
            "Key.f2": keyboard.Key.f2,
            "Key.f3": keyboard.Key.f3,
            "Key.f4": keyboard.Key.f4,
            "Key.f5": keyboard.Key.f5,
            "Key.f6": keyboard.Key.f6,
            "Key.f7": keyboard.Key.f7,
            "Key.f8": keyboard.Key.f8,
            "Key.f9": keyboard.Key.f9,
            "Key.f10": keyboard.Key.f10,
            "Key.f11": keyboard.Key.f11,
            "Key.f12": keyboard.Key.f12,
            "Key.home": keyboard.Key.home,
            "Key.left": keyboard.Key.left,
            "Key.page_down": keyboard.Key.page_down,
            "Key.page_up": keyboard.Key.page_up,
            "Key.right": keyboard.Key.right,
            "Key.shift_l": keyboard.Key.shift_l,
            "Key.shift_r": keyboard.Key.shift_r,
            "Key.space": keyboard.Key.space,
            "Key.tab": keyboard.Key.tab,
            "Key.up": keyboard.Key.up,
        }
        keyboard.press(special_keys[key])
        keyboard.release(special_keys[key])


# def replicate(file_name: str = "key_logger.csv"):
#     with open(file_name) as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             simulate_key_press(row[0])


def replicate(file_name: str = "key_logger.csv"):
    keys = pd.read_csv(file_name)
    print(keys.head())
    for r in keys["0"]:
        simulate_key_press(r[1])
