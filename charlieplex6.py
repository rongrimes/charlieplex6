#!/usr/bin/python3
#Original source: https://github.com/simonmonk/raspberrypi_cookbook_ed2/blob/master/charlieplexing.py
#

import RPi.GPIO as GPIO
import time
import signal

pins = [18, 23, 24]

IN = -1                     # Note: GPIO.IN = 1, so can't use a constant since confuses w/the HI value.
LO = GPIO.LOW
HI = GPIO.HIGH

pin_led_states = [
#  p0  p1  p2
  [LO, HI, IN], # 0
  [HI, LO, IN], # 1
  [IN, LO, HI], # 2
  [IN, HI, LO], # 3
  [LO, IN, HI], # 4
  [HI, IN, LO]  # 5
]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#---------------------------------------------------------
def set_pin(pin_index, pin_state):
    if pin_state == IN:
        GPIO.setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)

def light_led(led_number):
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        set_pin(pin_index, pin_state)

def clear_pins():
    set_pin(0, IN)
    set_pin(1, IN)
    set_pin(2, IN)

def signal_handler(signal, frame):
#   print('You pressed Ctrl+C!')
    clear_pins()
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
    sys.exit(0)

#---------------------------------------------------------

signal.signal(signal.SIGTERM, signal_handler)       # kill in background mode
clear_pins()

try:
    led_cycle=list(range(0,6))+list(range(4,1,-1))
    while True:
        for x in led_cycle:
            light_led(x)
            time.sleep(0.1)
except:
    print()    # gives newline after a ^C.
    clear_pins()
    GPIO.cleanup()                 # resets all GPIO ports used by this program  

