#chatgpt generated

#pip install pynput

from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False  # Stop listener

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()