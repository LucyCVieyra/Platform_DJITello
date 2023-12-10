from djitellopy import Tello
import threading
import keyboard
import os
import time
import numpy as np

dron = Tello()
dron.connect()
dron.takeoff()
time.sleep(0.5)

flag=0
def paro():
    while True:
        if keyboard.is_pressed("p"):
            print("dron.land()")
            dron.land()
            os._exit(1)

hilo_Paro = threading.Thread(target=paro)
hilo_Paro.start()

"""
def detecta():
    while flag == 0:
        # Deteccion de plataforma

hilo_Detecta = threading.Thread(target=detecta)
hilo_Detecta.start()
"""

large, width = 3, 3
n = 1
i, j = 0, 1
a = large * width

while n < a:
    if i == 0:
        i += 1
        for num in np.arange(0, width - i, 1):
            dron.move_right(100)
            #dron.go_xyz_speed(0, -100, 0, 50)
            print("dron.move_right(", 100, ")")
            n += 1
            time.sleep(0.5)
        print("dron.move_right(", (num + 1) * 100, ")")
    else:
        for num in np.arange(0, width - i, 1):
            dron.move_right(100)
            #dron.go_xyz_speed(0, -100, 0, 50)
            print("dron.move_right(", 100, ")")
            n += 1
            time.sleep(0.5)
        print("dron.move_right(", (num+1)*100, ")")
        i += 1
    for num in np.arange(0, large - j, 1):
        dron.move_forward(100)
        #dron.go_xyz_speed(100, 0, 0, 50)
        print("dron.move_forward(", 100, ")")
        n += 1
        time.sleep(0.5)
    print("dron.move_forward(", (num+1)*100, ")")
    j += 1
    for num in np.arange(0, width - i, 1):
        dron.move_left(100)
        #dron.go_xyz_speed(0, 100, 0, 50)
        print("dron.move_left(", 100, ")")
        n += 1
        time.sleep(0.5)
    print("dron.move_left(", (num+1)*100, ")")
    i += 1
    for num in np.arange(0, large - j, 1):
        dron.move_back(100)
        #dron.go_xyz_speed(-100, 0, 0, 50)
        print("dron.move_back(", 100, ")")
        n += 1
        time.sleep(0.5)
    print("dron.move_back(", (num+1)*100, ")")
    j += 1

print("dron.land()")
dron.land()
os._exit(1)

