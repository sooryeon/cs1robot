import nxt
import nxt.bluesock
import cs1robot
from nxt.motor import *
brick = nxt.bluesock.BlueSock('00:16:53:0A:90:46').connect()

def main():
    left_motor = Motor(brick, PORT_A)
    right_motor = Motor(brick, PORT_B)
    both_motor = SynchronizedMotors(left_motor, right_motor, 0)

    both_motor.run()


main()

##right_motor.turn(100, 360)	#turn(power, tacho_counter)
##right_motor.brake()	        #stop & brake 
##both_motor.idle()
