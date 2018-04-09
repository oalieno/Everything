#!/usr/bin/env python3
"""Usage: ./everything.py [-h] [-s SCALE] [-o FILE] [-p PATTERN] [INPUT]

-h --help    show this
-s SCALE     scale factor of image
-o FILE      specify output file [deault: ./output.bmp]
-p PATTERN   some well known pattern [ex: origin, matt]

"""
from docopt import docopt
from PIL import Image
import pattern

BLACK = (0, 0, 0)

def pad(data, s):
    L = len(data)
    return data.rjust(L + -L % s, '0')

def decode(k, scale = None, filename = None):
    # default value
    if scale == None:
        scale = 10
    if filename == None:
        filename = "output.bmp"

    # process k
    k //= 17
    k = pad(bin(k)[2:], 17)

    # write to image
    img = Image.new( 'RGB', (106 * scale + 2, 17 * scale + 2), "white")
    pixels = img.load()
    for i, b in enumerate(k):
        if b == '1':
            xx = (i // 17)
            yy = (16 - i % 17)
            for x in range(xx * scale, (xx + 1) * scale):
                for y in range(yy * scale, (yy + 1) * scale):
                    pixels[x + 1, y + 1] = BLACK

    # save image
    img.save(filename)

if __name__ == '__main__':
    args = docopt(__doc__)
    if args['-p'] == 'origin':
        args['INPUT'] = pattern.origin
    elif args['-p'] == 'matt':
        args['INPUT'] = pattern.matt
    elif args['INPUT'] == None:
        args['INPUT'] = pattern.origin
    decode(int(args['INPUT']), scale = args['-s'], filename = args['-o'])
