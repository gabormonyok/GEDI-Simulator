import random


class EndPoint:
    """Represents general DALI endpoints. Common properties and functions for both Control Devices and Control Gears"""

    def __init__(self):
        self.status = 0x00
        self.shortAddress = 0x00
        self.searchAddress = 0x000000
        self.randomAddress = 0xFFFFFF
        self.DTR0 = 0x00
        self.DTR1 = 0x00

    # Generates a real random number as randomAddress between 1 and 0xFFFFFE
    def set_random_address_random(self):
        self.randomAddress = random.randint(0x000001, 0xFFFFFE)

    # Sets a fake "random" number as randomAddress
    def set_random_address_manual(self, random_address):
        self.randomAddress = random_address

    def get_random_address(self):
        return self.randomAddress

    # Sets a shortAddress to a certain device instance
    def set_short_address(self, short_address):
        self.shortAddress = short_address

    def get_short_address(self):
        return self.shortAddress
