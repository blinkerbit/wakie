from multiprocessing import shared_memory
import time
import sys
import json
from pynput import mouse
from pynput.keyboard import Key,Controller
kybrd_ctrl =Controller()
# mem_shared= shared_memory.SharedMemory(create=True,size= sys.getsizeof(time.time()))

# with open("sh_config.json","wb") as f:
#     a ={
#         "name":mem_shared.name
#     }
#     json.dump(json.dumps(a),f)

last_update = time.time()

def on_move(x, y):
    global last_update
    last_update=time.time()

def on_scroll(x, y, dx, dy):
    global last_update
    last_update  = time.time()

def on_click(x, y, button, pressed):
    global last_update
    last_update = time.time()


from pynput import keyboard

def on_press(key):
    global last_update
    last_update = time.time()
def on_release(key):
    global last_update
    last_update = time.time()

# Collect events until released
listener_keyboard = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener_keyboard.start()

listener_mouse = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener_mouse.start()


while True:
    time.sleep(60)
    if time.time()-last_update >100:
        kybrd_ctrl.press(Key.caps_lock)
        time.sleep(1)








