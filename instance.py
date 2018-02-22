from controlgear import ControlGear
from controldevice import ControlDevice


# This function creates as man Control Gear Objects as given by the input
def create_control_gears(number_of_control_gears):
    return [ControlGear() for _ in range(number_of_control_gears)]


# This function creates as man Control Device Objects as given by the input
def create_control_device(number_of_control_devices):
    return [ControlDevice() for _ in range(number_of_control_devices)]
