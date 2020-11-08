from fpioa_manager import *
from Maix import GPIO
from board import board_info

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

but_a=GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
but_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)
led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

led_w.value(1) # LED OFF
led_r.value(1) # LED OFF
led_g.value(1) # LED OFF
led_b.value(1) # LED OFF

counter = 0
but_stu = 1

while(True):
    if but_a.value() == 0 and but_stu == 1:

        if led_w.value() == 1:
            led_w.value(0)
        else:
            led_w.value(1)
        but_stu = 0
    if but_a.value() == 1 and but_stu == 0:
        but_stu = 1
