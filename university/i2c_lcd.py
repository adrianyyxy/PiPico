from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27

def test_main():
    i2c = I2C(0,scl=Pin(1), sda=Pin(0), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)
    print("test")
    sleep_ms(1000)
    lcd.clear()
    count = 0
    while True:
        lcd.move_to(0,0)
        lcd.putstr("hola mundo")
        sleep_ms(1000)
        lcd.clear()
        sleep_ms(1000)

#if __name__ == "__main__":
test_main()