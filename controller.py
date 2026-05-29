import serial
import pyvjoy
import time

ser = serial.Serial('COM3', 9600)
j = pyvjoy.VJoyDevice(1)
time.sleep(2)

while True:
    line = ser.readline()
    parts = line.split(b',')
    if len(parts) == 3:
        steering = int(parts[0])
        gas      = int(parts[1])
        brake    = int(parts[2])

        center = 511
        deadzone = 20
        if abs(steering - center) < deadzone:
            steering = center
        j.data.wAxisX = int(steering / 1023 * 32768)
        buttons = 0
        if gas == 1:
            buttons |= 1
        if brake == 1:
            buttons |= 2
        j.data.lButtons = buttons
        j.update()
        print(f"S:{steering} G:{gas} B:{brake}", flush=True)