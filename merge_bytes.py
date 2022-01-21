# merge_bytes.py

import os
import sys

def name_parts(path):
    base = os.path.basename(path)
    parts = os.path.splitext(base)
    return base, parts[0], parts[1]

def read_bytes(path):
    with open(path, 'rb') as reader:
        return reader.read()

def merge_bytes(path):
    path_base, path_name, path_ext = name_parts(path)
    for root, dirs, files in os.walk(path):
        try:
            base, name, ext = name_parts(os.path.join(root, files[0]))
        except Exception as e:
            print(f'merge_bytes.py: {str(e)}')
            exit(1)
        with open(f'{path_name}{ext}', 'wb') as writer:
            for f in files:
                part = read_bytes(os.path.join(root, f))
                writer.write(part)
    return

if __name__=='__main__':
    merge_bytes(sys.argv[1])
    print('fin')
