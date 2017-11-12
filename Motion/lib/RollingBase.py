from lib.Verbose import *


class RollingBase:
    def __init__(self, ros_connection):
        self.__ros_connection = ros_connection
        for pin_num in ros_connection:
            GPIO.setup(pin_num, GPIO.IN)

    def __enter__(self):
        try:
            GPIO.setmode(GPIO.BCM)
            ok()
        except Exception:
            fail()
        print("Set GPIO Mode to BCM")

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            GPIO.cleanup()
            ok()
        except Exception as e:
            fail()
        print("Clean Up the GPIO")

    @property
    def ros_connection(self):
        return self.__ros_connection
