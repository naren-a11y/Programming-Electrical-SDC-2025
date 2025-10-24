from gpiozero import LED
from time import sleep

led = LED(17)

for i in range(5):
    print(f"Simulated blink #{i+1}")
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
