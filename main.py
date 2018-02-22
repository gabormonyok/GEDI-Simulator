import instance

endpointMatrix = instance.create_control_gears(20)
controlDevice = instance.create_control_device(10)

print("%06x" % endpointMatrix[1].get_random_address())
endpointMatrix[1].set_random_address_random()
print("%06x" % endpointMatrix[1].get_random_address())
endpointMatrix[1].set_random_address_manual(0xFEFEFE)
print("%06x" % endpointMatrix[1].get_random_address())

print("%02x" % endpointMatrix[1].actualLevel)
endpointMatrix[1].set_light_level(0x5A)
print("%02x" % endpointMatrix[1].actualLevel)

for endpoints in endpointMatrix:
    print("%02x" % endpoints.shortAddress)

i = 0
for sensors in controlDevice:
    sensors.set_input_value(i)
    print("%02x" % sensors.inputValue)
    i += 1
