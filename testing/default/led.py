from hardware import gpio

class LED:

    def __init__(self, pinid, onLevel):
        self.onLevel = onLevel
        self.pinid = pinid
        self.gpio = gpio(pinid, gpio.GPIO_MODE_OUTPUT_PULLDOWN)
        self.gpio.write(1 - self.onLevel)

    def ON(self):
        print("LED ON\r\n")
        self.gpio.write(self.onLevel)

    def OFF(self):
        print("LED OFF\r\n")
        self.gpio.write(1 - self.onLevel)
