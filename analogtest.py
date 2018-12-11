import RoboPiLib as RPL
import setup
import time

L = 1
R = 0
x = 1

while x == 1:
  reading = RPL.analogRead(7)
  if reading < 500:
    RPL.servoWrite(0, 1590)
    RPL.servoWrite(1, 1410)
  else:
    RPL.servoWrite(0, 1500)
    time.sleep(1.5)
    RPL.servoWrite(0, 1590)
