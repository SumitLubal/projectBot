# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

def setJointTo(leg_array,index):
    for leg_num in leg_array:
        val = leg_limits[leg_num][index]
        print('Servo num'+ str(leg_num)+' value'+str(val))
        pwm.set_pwm(leg_num, 0, val)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
# while True:
# 	for x in range(16):
# 		# Move servo on channel O between extremes.
# 		servoNum, val = [int(x) for x in raw_input("Enter servo number and value ").split()]
# 		pwm.set_pwm(servoNum, 0, val)
		#time.sleep(1)
		#pwm.set_pwm(x, 0, servo_max)
		#time.sleep(1)
# format is [leg][min,max,center]
leg_limits  = [[100,500,250],[100,550,340],[110,580,350],[110,580,350],[100,500,250],[100,500,330],[110,570,300],[120,580,280],[210,550,320],[120,550,330],[120,510,270],[170,570,350],[130,570,350],[130,540,280],[130,550,350],[140,540,350]]
ancle_right = [0,4,7]
knee_right = [1,5,8]
pelvic_right = [2,3,6]
ancle_left = [13,10]
knee_left = [14,9]
pelvic_left = [15,12,11]
#bring all to center
#bring ancle righ to center
setJointTo(ancle_left,2)
setJointTo(ancle_right,2)
setJointTo(knee_left,2)
setJointTo(knee_right,2)
setJointTo(pelvic_left,2)
setJointTo(pelvic_right,2)
#jump all knees
setJointTo(knee_left,0)
setJointTo(knee_right,0)