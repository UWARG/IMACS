from Send import Send 

decoded_payload = {
    "x": 1.34343,
    "y": 4.6,
    "z": 5.324,
    "heading": 9.234,
}

encoded_payload = Send.send(decoded_payload)
print(f"encoded payload: {encoded_payload}")





