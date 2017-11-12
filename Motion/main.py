try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from lib.TwoWheelsRB import *

if __name__ == '__main__':
    with TwoWheelsRB("TwoWheelsRB.yaml") as my_base:
        my_base.move(20, 20)
