class NetworkSwitch:
    def __init__(self) -> None:
        # Hardware Specifications
        self.name: str = None
        self.layer = None
        self.speed_duplex = None
        # Networked Specifications
        self.ip_address = None

    def __str__(self) -> str:
        return f"{self.name} is set to layer: {self.layer}"

class NetworkSwitchBuilder:
    def __init__(self) -> None:
        self.network_switch = NetworkSwitch()

    def build(self):
        return self.network_switch

class NetworkSwitchHardwareBuilder(NetworkSwitchBuilder):
    def named(self, name):
        self.network_switch.name = name
        return self

    def set_to_layer(self, layer):
        self.network_switch.layer = layer
        return self

    def has_speed_duplex_of(self, duplex):
        self.network_switch.speed_duplex = duplex
        return self

class NetworkedSwitchAttributeBuilder(NetworkSwitchHardwareBuilder):
    def has_ip_address(self, ip_address):
        if self.network_switch.layer != 3:
            raise ValueError("Cannot set IP Address for a non-layer 3 switch")
        self.network_switch.ip_address = ip_address
        return self

if __name__ == '__main__':
    switch_hardware = NetworkSwitchHardwareBuilder()

    only_hardware = switch_hardware\
        .named("BLDG-1-Example")\
        .set_to_layer(3)\
        .has_speed_duplex_of("10-half")\
        .build()

    print(only_hardware)

    networked_switch = NetworkedSwitchAttributeBuilder()
    network_specifications = networked_switch\
                                .named("BLDG-1-Active-Example")\
                                .set_to_layer(3)\
                                .has_speed_duplex_of("auto")\
                                .has_ip_address("192.158.1.38")\
                                .build()
    print(network_specifications)
