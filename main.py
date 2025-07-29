from machine import Pin
from utime import sleep

print("oii")

ledVerde = Pin(13, Pin.OUT)
ledVermelho = Pin(15, Pin.OUT)
ledAmarelo = Pin(16, Pin.OUT)

while True:
    ledVerde.on()
    print("Verde on!")
    sleep(20)
    ledVerde.off()
    sleep(0.5)
    
    ledAmarelo.on()
    print("amarelo on!")
    sleep(10)
    ledAmarelo.off()
    sleep(0.5)

    ledVermelho.on()
    print("amarelo on!")
    sleep(7)
    ledVermelho.off()
    sleep(0.5)