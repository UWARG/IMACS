class PIDValues:
    def __init__(self, P, I, D):
        self.P = P
        self.I = I
        self.D = D


class PIDController:
    def PIDValues(self, axes):
        self.axes = axes # array of size 6 of PID values

class GroundStationData:
    def __init__(self, header, motor_outputs, data, battery_voltages, controller_values, crc):
        self.header = header
        self.motor_outputs = motor_outputs
        self.data = data
        self.battery_voltages = battery_voltages
        self.controller_values = controller_values
        self.crc = crc

class SensorData:
    def __init__(self, latitude, longitude, altitude, climb_rate, heading, air_speed, ground_speed, roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate):
        self.latitude = latitude;
        self.longitude = longitude;
        self.altitude = altitude;
        self.climb_rate = climb_rate;
        self.heading = heading;
        self.air_speed = air_speed;
        self.ground_speed = ground_speed;
        self.roll = roll;
        self.pitch = pitch;
        self.yaw = yaw;
        self.roll_rate = roll_rate;
        self.pitch_rate = pitch_rate;
        self.yaw_rate = yaw_rate;

class Header:
    def __init__(self, flag, length, type):
        self.flag = flag
        self.length = length
        self.type = type

class GroundStationPIDSetResponse:
    def __init__(self, header, controller_number, controller, crc):
        self.header = header
        self.controller_number = controller_number
        self.controller = controller
        self.crc = crc
