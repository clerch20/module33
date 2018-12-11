import RoboPiLib as RPL
import setup
x = [0,1]
for off in x:
  RPL.servoWrite(off,1500)
  print('pin %s is disabled' % (off))
