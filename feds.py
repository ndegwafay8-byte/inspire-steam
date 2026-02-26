from machine import Pin
import time
red_led = Pin(28, Pin.OUT)
while True:
    red_led.on()
    yellow_led = Pin(27, pin.out)
    time.sleep(1) # Wait for USB to become ready
    red_led.off()
    yellow_led.on()
    time.sleep(1)
    print("learning iot")