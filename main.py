class dataparsing:

    def __init__(self, Ground_station_data, PID_set_response):
        self.Ground_station_data = Ground_station_data
        self.PID_set_response = PID_set_response


    def update_Ground_station_data(self, Ground_station_data_object):
        self.Ground_station_data = {
            'motor_outputs' : Ground_station_data_object.GroundStationData.motor_outputs,
            'gps_data': {
                'Latitude' : Ground_station_data_object.SensorData.latitude,
                'Longitude' : Ground_station_data_object.SensorData.longitude,
                'Altitude' : Ground_station_data_object.SensorData.altitude,
            },  
            'climb_rate': Ground_station_data_object.SensorData.climb_rate,
            'track': None,
            'heading': Ground_station_data_object.SensorData.heading,
            'air_speed': Ground_station_data_object.SensorData.air_speed,
            'ground_Speed': Ground_station_data_object.SensorData.ground_speed,
            'imu_data':{
                'roll': Ground_station_data_object.SensorData.roll,
                'pitch': Ground_station_data_object.SensorData.pitch,
                'yaw': Ground_station_data_object.SensorData.yaw,
            },
            'roll_rate': Ground_station_data_object.SensorData.roll_rate,
            'pitch_rate': Ground_station_data_object.SensorData.pitch_rate,
            'yaw_rate': Ground_station_data_object.SensorData.yaw_rate,
            'Battery_Voltages': Ground_station_data_object.GroundStationData.battery_voltages,
            'Controller_Values':  Ground_station_data_object.GroundStationData.controller_values,
        }
    
    def update_PID_set_response(self, PID_set_response_object):
        self.PID_set_response = {
            'controller_number': None,
        }