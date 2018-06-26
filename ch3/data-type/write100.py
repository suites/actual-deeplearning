filename = 'a.bin'
data = 100

with open(filename, 'wb') as f:
    f.write(bytearray([data]))