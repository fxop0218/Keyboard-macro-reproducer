from pynput import keyboard

filename = "key_logs"


def startRecord(rec: bool = False, file_name: str = "key_logs"):
    filename = file_name
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def on_press(key):
    with open(f"{filename}.txt", "a") as file:
        file.write(f"Key {key} pressed\n")  # Change this from csv file or other thing


def on_release(key):
    with open(f"{filename}.txt", "a") as file:
        file.write(f"Key {key} released\n")


def replay_inputs(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    keyboard_controller = keyboard.Controller()
    for line in lines:
        if "pressed" in line:
            key = line.split(" ")[1].strip()
            keyboard_controller.press(key)
        elif "released" in line:
            key = line.split(" ")[1].strip()
            keyboard_controller.release(key)
