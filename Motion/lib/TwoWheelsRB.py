import yaml

from lib.Wheel import DC_Wheel


class TwoWheelsRB:
    def __init__(self, pi, file):
        config = yaml.load(file)
        self.__ros_connection = None
        self.__left_wheel  = DC_Wheel(pi,
                                      config["L_pin1"],
                                      config["L_pin2"],
                                      config["L_pwd_pin"],
                                      config["PWD_Frequency "],
                                      config["PWD_Range"])
        self.__right_wheel = DC_Wheel(pi,
                                      config["R_pin1"],
                                      config["R_pin2"],
                                      config["R_pwd_pin"],
                                      config["PWD_Frequency "],
                                      config["PWD_Range"])

    def move(self, speed):
        self.right_wheel.move(speed)
        self.left_wheel.move(speed)

    def brake(self):
        self.right_wheel.brake()
        self.left_wheel.brake()


    @property
    def left_wheel(self):
        return self.__left_wheel

    @property
    def right_wheel(self):
        return self.__right_wheel
