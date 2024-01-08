import pyautogui
import keyboard
import json

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print("Config file not found. Please create 'config.json' with key-location mappings.")
        return {}

def double_click_at_coordinates(x, y):
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.tripleClick()

def main():
    config = load_config()

    if not config:
        return

    print("Press the assigned key to trigger the action. Press 'Esc' to pause or stop the app.")

    while True:
        if keyboard.is_pressed('Esc'):
            print("App paused or stopped.")
            break

        if keyboard.read_event().name in config:
            key_pressed = keyboard.read_event(suppress=True).name
            target_x, target_y = config[key_pressed]
            double_click_at_coordinates(target_x, target_y)

if __name__ == "__main__":
    main()
