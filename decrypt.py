def hex_byte(hex):
    return bin(int(hex, 16))[2:].zfill(8)

def c_left_shift(n, d, N):  
    return ((n << d) % (1 << N)) | (n >> (N - d))

with open('../input/input10.txt', 'r') as f:
    num_bytes = int(f.readline())
    hex_string = f.readline().strip().split(' ')

byte_hex_string = [hex_byte(hex) for hex in hex_string]
byte_shifted = [
    chr(c_left_shift(int(bytes_hex, 2), count % 8, 8))
    for count, bytes_hex in enumerate(byte_hex_string)
]
print("".join(byte_shifted))