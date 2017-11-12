class DC_Wheel:
    def __init__(self, pin1, pin2, pwd_pin, pwd_freq):
        self._conn = {"cmd1": pin1, "cmd2": pin2, "pwd": pwd_pin}
        for pin_num in self._conn.values():
            GPIO.setup(pin_num, GPIO.OUT)
        self._PWD = GPIO.PWM(pwd_pin, pwd_freq)

    # Try with the pwm on the enable and keep pin1 and pin2 in the same state during the movement
    # Advantage only 1 PWMs - Disadvantage 3 pins needed for each wheels.
    def move(self, value):
        if value > 0:
            # Forward Move
            GPIO.outpout(self._conn["cmd1"], GPIO.HIGH)
            GPIO.outpout(self._conn["cmd2"], GPIO.LOW)
        else:
            # Reverse Move
            GPIO.outpout(self._conn["cmd1"], GPIO.LOW)
            GPIO.outpout(self._conn["cmd2"], GPIO.HIGH)
        self._PWD.start(abs(value))
