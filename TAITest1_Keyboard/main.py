from keyboardControl import *

def select_ppsspp():
    hold(key.leftwin)
    press(key.num2)
    release(key.leftwin)

def loadMenu():
    press(key.k)
    sleep(5.0)
    press(key.enter)
    sleep(2.0)
    press(key.enter)
    sleep(2.0)
    press(key.enter)
    sleep(4.0)

def selectPractise():
    press(key.s)
    press(key.s)
    press(key.s)
    press(key.s)
    press(key.s)
    press(key.k)
    sleep(4.0)
    press(key.i)
    press(key.d)
    press(key.i)
    press(key.k)

def selectNetWork():
    press(key.s)
    press(key.s)
    press(key.s)
    press(key.s)
    press(key.k)

def wavu_wavu(n):
    combo([key.d])
    sleep(.05)
    for i in range(n):
        combo([key.s])
        # combo([key.s, key.d])
        combo([key.d])
        sleep(.04)
        combo([key.d])
        sleep(.04)

def wavu_jfsr(n):
    combo([key.d])
    sleep(.05)
    for i in range(n):
        combo([key.s])
        # combo([key.s, key.d])
        combo([key.d])
        sleep(.04)
        combo([key.d])
        sleep(.04)
    combo([key.d])
    sleep(.04)
    combo([key.s, key.d, key.l])

select_ppsspp()
#loadMenu()
#selectPractise()
#sleep(5)
wavu_jfsr(6)
