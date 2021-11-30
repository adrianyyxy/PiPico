import utime
from machine import Pin, UART, I2C

dato = str(" ")
Count = int (0)
ReadDistance = int (0)
Control = int (0)
Control_2 = int (0)
Control_3 = int (0)
i = int(0)
Distance = [0,0,0]

esp = UART(0,115200)
sensor = UART(1, 9600,bits=7, parity=0,stop=1, invert=UART.INV_RX)

while True:

    for i in range (0,15):
        if sensor.any()>0:
            dato = sensor.read(50)
            dato = dato.decode()
    for i in range (0,2):
        for element in dato:
            if (Control == 0):
                if (element == "0"):
                    Distance[0] = 0
                    Control = 1
                elif (element == "1"):
                    Distance[0] = 1
                    Control = 1
                elif (element == "2"):
                    Distance[0] = 2
                    Control = 1
                elif (element == "3"):
                    Distance[0] = 3
                    Control = 1
                elif (element == "4"):
                    Distance[0] = 4
                    Control = 1
                elif (element == "5"):
                    Distance[0] = 5
                    Control = 1
                elif (element == "6"):
                    Distance[0] = 6
                    Control = 1
                elif (element == "7"):
                    Distance[0] = 7
                    Control = 1
                elif (element == "8"):
                    Distance[0] = 8
                    Control = 1
                elif (element == "9"):
                    Distance[0] = 9
                    Control = 1
                else:
                    Control = 0
            elif (Control == 1):
                if (element == "0"):
                    Distance[1] = 0
                    Control = 2
                elif (element == "1"):
                    Distance[1] = 1
                    Control = 2
                elif (element == "2"):
                    Distance[1] = 2
                    Control = 2
                elif (element == "3"):
                    Distance[1] = 3
                    Control = 2
                elif (element == "4"):
                    Distance[1] = 4
                    Control = 2
                elif (element == "5"):
                    Distance[1] = 5
                    Control = 2
                elif (element == "6"):
                    Distance[1] = 6
                    Control = 2
                elif (element == "7"):
                    Distance[1] = 7
                    Control = 2
                elif (element == "8"):
                    Distance[1] = 8
                    Control = 2
                elif (element == "9"):
                    Distance[1] = 9
                    Control = 2
                else:
                    Control = 1
            elif (Control == 2):
                if (element == "0"):
                    Distance[2] = 0
                    Control = 3
                elif (element == "1"):
                    Distance[2] = 1
                    Control = 3
                elif (element == "2"):
                    Distance[2] = 2
                    Control = 3
                elif (element == "3"):
                    Distance[2] = 3
                    Control = 3
                elif (element == "4"):
                    Distance[2] = 4
                    Control = 3
                elif (element == "5"):
                    Distance[2] = 5
                    Control = 3
                elif (element == "6"):
                    Distance[2] = 6
                    Control = 3
                elif (element == "7"):
                    Distance[2] = 7
                    Control = 3
                elif (element == "8"):
                    Distance[2] = 8
                    Control = 3
                elif (element == "9"):
                    Distance[2] = 9
                    Control = 3
                else:
                    Control = 2
            elif (Control == 3):
                ReadDistance = (Distance[0] * 100) + (Distance[1] * 10) + (Distance[2])
                Control = 0
                if (ReadDistance <=30):
                    Count = Count + 1
                    if (Count % 2 == 0):
                        #print(Count/2, " people have passed")
                        esp.write(str(Count/2))
                        esp.write('\n')
                    utime.sleep(1)