import random

class GroundReceive():
    def receive(self):
        # Mocks actual data coming from RFD
        while True:
            if random.randint(0, 100000) == 1:
                TEST_PAYLOAD = {
                    'motor_outputs': [random.random() * 10 for i in range(0,12)],
                    'gps_data': {
                        'lat': random.random() * 10,
                        'lon': random.random() * 10,
                        'alt': random.random() * 10,
                    },
                    'climb_rate': random.random() * 10,
                    'track': random.random() * 10,
                    'heading': random.random() * 10,
                    'air_speed': random.random() * 10,
                    'ground_speed': random.random() * 10,
                    'imu_data': {
                        'yaw': random.random() * 10,
                        'pitch': random.random() * 10,
                        'roll': random.random() * 10,
                    },
                    'roll_rate': random.random() * 10,
                    'pitch_rate': random.random() * 10,
                    'yaw_rate': random.random() * 10,
                    'batery_voltages': [random.random() * 10 for i in range(0, 13)],
                    'pitch_rate': [random.random() * 10 for i in range(0, 13)],
                }
                print("new test payload", TEST_PAYLOAD)
                self.payload = TEST_PAYLOAD
