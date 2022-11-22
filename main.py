from Send import Send
from GroundReceive import GroundReceive 

decoded_payload = {
    "x": 1.34343,
    "y": 4.6,
    "z": 5.324,
    "heading": 9.234,
}

encoded_payload = Send.send(decoded_payload)
print(f"encoded payload: {encoded_payload}")

ground = GroundReceive()
ground.relative_movement_command(encoded_payload)





