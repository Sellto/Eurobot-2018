from lib.RollingBase import *
import yaml

from lib.Wheel import DC_Wheel


class TwoWheelsRB(RollingBase):
    def __init__(self, configfile):
        self.__ros_connection = None
        self.__left_wheel = None
        self.__right_wheel = None
        # Get content from configuration file
        self.config_file_split(configfile)
        # In this case ROS send velocity and angular_speed
        RollingBase.__init__(self.__ros_connection)

    def move(self, speed, angular_speed):
        right_wheel = self.right_wheel
        left_wheel = self.left_wheel
        right_wheel.move(speed * angular_speed)
        left_wheel.move(speed * -angular_speed)

    def config_file_split(self, file):
        config = yaml.load(file)
        self.__ros_connection = config["ROS_Connection"]
        self.__left_wheel = DC_Wheel(config["L_pin1"], config["L_pin2"], config["L_pwd_pin"], config["PWD_Frequency "])
        self.__right_wheel = DC_Wheel(config["R_pin1"], config["R_pin2"], config["R_pwd_pin"], config["PWD_Frequency "])

    @property
    def left_wheel(self):
        return self.__left_wheel

    @property
    def right_wheel(self):
        return self.__right_wheel
