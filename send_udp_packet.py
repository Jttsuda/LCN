import socket
import codecs

# Sends raw data via UDP protocol to specified IP & PORT
# Monitor wireshark for a response
IP = '0.0.0.0'
PORT = 0

data = "1337ffffffffaaaaaaaaaaaaaaaa1111111111111111" # Hex representation of Bin Data
data = codecs.decode(data, "hex_codec") # Decode the binary string into normal form

listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listener.sendto(data, (IP, PORT))