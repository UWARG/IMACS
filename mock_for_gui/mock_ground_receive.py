import random

class GroundReceive():
    def receive_mock_gui(self):
        # Mocks actual data coming from RFD
        while True:
            if random.randint(0, 100000) == 1:
                TEST_PAYLOAD = {
                    "x": random.random() * 10,
                    "y": random.random() * 10,
                    "z": random.random() * 10,
                    "heading": random.random() * 10,
                }
                print("new test payload", TEST_PAYLOAD)
                self.payload = TEST_PAYLOAD
