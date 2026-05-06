#!/usr/bin/env python3
"""Generate simple BudgetIO PNG icons."""
import struct, zlib, math

def make_png(size, bg=(13,13,13), accent=(200,255,0)):
    img = [bg]*size*size
    cx, cy = size//2, size//2
    r = int(size * 0.38)
    thick = max(2, size//24)
    # Draw circular ring
    for y in range(size):
        for x in range(size):
            dx, dy = x-cx, y-cy
            dist = math.sqrt(dx*dx+dy*dy)
            if r-thick <= dist <= r+thick:
                img[y*size+x] = accent
            # Draw dollar sign bars (simplified B letter)
            elif abs(dx) < size*0.06 and abs(dy) < r*0.55:
                img[y*size+x] = accent
            elif abs(dy) < size*0.04 and -size*0.02 < dx < r*0.28:
                img[y*size+x] = accent
    # Build PNG
    def chunk(t,d):
        c=struct.pack('>I',len(d))+t+d
        return c+struct.pack('>I',zlib.crc32(c[4:])&0xffffffff)
    rows=b''.join(b'\x00'+bytes(c for px in img[i*size:(i+1)*size] for c in px) for i in range(size))
    return (b'\x89PNG\r\n\x1a\n'
        +chunk(b'IHDR',struct.pack('>IIBBBBB',size,size,8,2,0,0,0))
        +chunk(b'IDAT',zlib.compress(rows,9))
        +chunk(b'IEND',b''))

for sz in [192,512]:
    with open(f'icon-{sz}.png','wb') as f:
        f.write(make_png(sz))
    print(f'icon-{sz}.png created')
