try:
    import pigpio
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

import time

from lib.TwoWheelsRB import *

if __name__ == '__main__':
    myRB = TwoWheelsRB(pigpio.pi(), "TwoWheelsRB.yaml")
    TwoWheelsRB.move(75)
    time.sleep(5)
    TwoWheelsRB.brake()


