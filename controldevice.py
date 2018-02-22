from endpoint import EndPoint


class ControlDevice(EndPoint):
    """Represents a Control/Input Device (Sensor or Push Button) from a general DALI Object"""

    def __init__(self):
        super().__init__()
        self.numberOfInstances = 0
        self.instanceType = 0
        self.instanceNumber = 0
        self.inputValue = 0x00

    def set_input_value(self, input_value):
        self.inputValue = input_value

    def get_input_value(self):
        return self.inputValue
