from endpoint import EndPoint


class ControlGear(EndPoint):
    """Represents a Control Gear Object or rather called Luminaire from a general DALI object"""

    def __init__(self):
        super().__init__()
        self.actualLevel = 0x00
        self.minLevel = 0x00
        self.maxLevel = 0xFE
        self.fadeRate = 7
        self.fadeTime = 0
        self.group = 0x00

    # Sets the light level between values 0x00 and 0xFE
    def set_light_level(self, light_level):
        self.actualLevel = light_level

    def get_light_level(self):
        return self.actualLevel
