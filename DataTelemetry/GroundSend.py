import serial
from digi.xbee.devices import XBeeDevice


class GroundSend:
    def __init__(self, id):  # ID is temporary. This will be discussed and updated.
        """
        Initializes parameters for Ground Send module.

        Parameters
        ----------
        type: int
            Integer to uniquely identify each data send packet.
        """
        self.data_id = id

    def GroundSendWorker(
        self,
        data,  # The data to be sent.
        frame_type,  # Can be 10 for transit frame, 90 for receive frame, and 8B for a transit response frame.
        address_64,  # 64-bit target address.
        broadcast_radius=0x00,  # Limit on how many times the message should hop before giving if target is not reached.
        options=0x00,
        frame_id=0x01,  # Optional but allows ordering of frames with their responses.
        address_16=0xFFFE,  # 16-bit address; FF FE is the default address.
    ):
        """
        Takes in data required to send to the UAV.
        Encodes it to an array of bytes.
        """
        start_delimiter = 0x7E
        message_length = hex(14 + len(data.encode("utf-8")))
        checksum = hex(message_length + 3)


class XBeeInterface:
    def __init__(self):
        """
        Initializes a new XBee interface with an empty func_dict and device_dict.
        """
        self.func_dict = dict()
        self.device_dict = dict()
        self.id_counter = 0

    def read_callback(self, device_id):
        def callback(xbee_message):
            data = xbee_message.data.decode("utf8")
            self.func_dict[device_id](data)

        return callback

    def write(self, device_id, data):
        self.device_dict[device_id].send_data_broadcast(data)

    def create_device(self, read_function, device_port):
        device = XBeeDevice(device_port, 9600)
        device.open()
        device.add_data_received_callback(self.read_callback(self.id_counter))
        self.func_dict[self.id_counter] = read_function
        self.device_dict[self.id_counter] = device
        self.id_counter += 1
