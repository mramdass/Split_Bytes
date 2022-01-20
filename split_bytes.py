# split_bytes.py

import os
import sys

def name_parts(path):
    base = os.path.basename(path)
    parts = os.path.splitext(base)
    return base, parts[0], parts[1]

def write_bytes(path, part):
    with open(path, 'wb') as writer:
        writer.write(part)

def split_bytes(path, size):
    with open(path, 'rb') as reader:
        part = reader.read(size)
        base, name, ext = name_parts(path)
        os.mkdir(name)
        counter = 0
        while part:
            write_bytes(f'{name}/{str(counter)}', part)
            counter = counter + 1
            part = reader.read(size)
    return

if __name__=='__main__':
    split_bytes(sys.argv[1], int(sys.argv[2]))
    print('fin')