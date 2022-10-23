class Protocol:
    def __init__(self, time: int, payload_type: int, CRC: int):
        self.time = time
        self.payload_type = payload_type
        self.CRC = CRC

class GroundToAir(Protocol):
    def __init__(self, time: int, payload_type: int, CRC: int, \
                 lat: float, long: float, altitude: float, yaw: float, pitch: float, \
                 roll: float, outputs_12: int):
        super().__init__(time, payload_type, CRC)

class AirToGround(Protocol):
    def __init__(self, time: int, payload_type: int, CRC: int, \
                 lat: float, long: float, altitude: float):
        super().__init__(time, payload_type, CRC)


