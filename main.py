from Send import Send
from GroundReceive import GroundReceive 

decoded_payload = {
    "x": 1.34343,
    "y": 4.6,
    "z": 5.324,
    "heading": 9.234,
}
print(f"original payload:\n {decoded_payload}\n")

encoded_payload = Send.send(decoded_payload)
print(f"encoded payload:\n {encoded_payload}\n")

ground = GroundReceive()
redecoded_payload = ground.relative_movement_command(encoded_payload)
print(f"decoded payload:\n {redecoded_payload}\n")




