import machine
import utime

#Pin 31 - ADC0
analog_value = machine.ADC(0)

while True:
    sensor = analog_value.read_u16()
    Distance = sensor/100
    Distance = round(Distance,0)
    print("Distance in cm: ",Distance)
    print("Distance in mV: ",sensor)
    #inches = millimeters/25.4
    #print("\nDistance in inc: ",inches)
    utime.sleep(5)