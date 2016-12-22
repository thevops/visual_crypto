# python 3

"""
change opt to (1,2) - this look better
"""
from PIL import Image
import sys
from random import randint

image = Image.open(sys.argv[1])
image = image.convert('1')

outfile1 = Image.new("1", (2 * image.size[0], 2 * image.size[1]))
outfile2 = Image.new("1", (2 * image.size[0], 2 * image.size[1]))

black = 0
white = 255

for x in range(image.size[0]):
    for y in range(image.size[1]):
        sourcepixel = image.getpixel((x, y))
        opt = randint(1,6)
        if sourcepixel == 0:
            if opt==1:
                """
                255  0
                 0  255
                """
                outfile1.putpixel((x * 2, y * 2), white)
                outfile1.putpixel((x * 2 + 1, y * 2), black)
                outfile1.putpixel((x * 2, y * 2 + 1), black)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), white)

                outfile2.putpixel((x * 2, y * 2), black)
                outfile2.putpixel((x * 2 + 1, y * 2), white)
                outfile2.putpixel((x * 2, y * 2 + 1), white)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), black)
            elif opt==2:
                """
                 0  255
                255  0
                """
                outfile1.putpixel((x * 2, y * 2), black)
                outfile1.putpixel((x * 2 + 1, y * 2), white)
                outfile1.putpixel((x * 2, y * 2 + 1), white)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), black)

                outfile2.putpixel((x * 2, y * 2), white)
                outfile2.putpixel((x * 2 + 1, y * 2), black)
                outfile2.putpixel((x * 2, y * 2 + 1), black)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), white)
            elif opt==3:
                """
                255  0
                255  0
                """
                outfile1.putpixel((x * 2, y * 2), white)
                outfile1.putpixel((x * 2 + 1, y * 2), black)
                outfile1.putpixel((x * 2, y * 2 + 1), white)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), black)

                outfile2.putpixel((x * 2, y * 2), black)
                outfile2.putpixel((x * 2 + 1, y * 2), white)
                outfile2.putpixel((x * 2, y * 2 + 1), black)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), white)
            elif opt==4:
                """
                0  255
                0  255
                """
                outfile1.putpixel((x * 2, y * 2), black)
                outfile1.putpixel((x * 2 + 1, y * 2), white)
                outfile1.putpixel((x * 2, y * 2 + 1), black)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), white)

                outfile2.putpixel((x * 2, y * 2), white)
                outfile2.putpixel((x * 2 + 1, y * 2), black)
                outfile2.putpixel((x * 2, y * 2 + 1), white)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), black)
            elif opt==5:
                """
                 0   0
                255 255
                """
                outfile1.putpixel((x * 2, y * 2), black)
                outfile1.putpixel((x * 2 + 1, y * 2), black)
                outfile1.putpixel((x * 2, y * 2 + 1), white)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), white)

                outfile2.putpixel((x * 2, y * 2), white)
                outfile2.putpixel((x * 2 + 1, y * 2), white)
                outfile2.putpixel((x * 2, y * 2 + 1), black)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), black)
            elif opt==6:
                """
                255 255
                 0   0
                """
                outfile1.putpixel((x * 2, y * 2), white)
                outfile1.putpixel((x * 2 + 1, y * 2), white)
                outfile1.putpixel((x * 2, y * 2 + 1), black)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), black)

                outfile2.putpixel((x * 2, y * 2), black)
                outfile2.putpixel((x * 2 + 1, y * 2), black)
                outfile2.putpixel((x * 2, y * 2 + 1), white)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), white)
        else:  # sourcepixel==250
            if opt==1:
                outfile1.putpixel((x * 2, y * 2), white)
                outfile1.putpixel((x * 2 + 1, y * 2), black)
                outfile1.putpixel((x * 2, y * 2 + 1), black)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), white)

                outfile2.putpixel((x * 2, y * 2), white)
                outfile2.putpixel((x * 2 + 1, y * 2), black)
                outfile2.putpixel((x * 2, y * 2 + 1), black)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), white)
            elif opt==2:
                outfile1.putpixel((x * 2, y * 2), black)
                outfile1.putpixel((x * 2 + 1, y * 2), white)
                outfile1.putpixel((x * 2, y * 2 + 1), white)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), black)

                outfile2.putpixel((x * 2, y * 2), black)
                outfile2.putpixel((x * 2 + 1, y * 2), white)
                outfile2.putpixel((x * 2, y * 2 + 1), white)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), black)
            elif opt==3:
                outfile1.putpixel((x * 2, y * 2), white)
                outfile1.putpixel((x * 2 + 1, y * 2), black)
                outfile1.putpixel((x * 2, y * 2 + 1), white)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), black)

                outfile2.putpixel((x * 2, y * 2), white)
                outfile2.putpixel((x * 2 + 1, y * 2), black)
                outfile2.putpixel((x * 2, y * 2 + 1), white)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), black)
            elif opt==4:
                outfile1.putpixel((x * 2, y * 2), black)
                outfile1.putpixel((x * 2 + 1, y * 2), white)
                outfile1.putpixel((x * 2, y * 2 + 1), black)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), white)

                outfile2.putpixel((x * 2, y * 2), black)
                outfile2.putpixel((x * 2 + 1, y * 2), white)
                outfile2.putpixel((x * 2, y * 2 + 1), black)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), white)
            elif opt==5:
                outfile1.putpixel((x * 2, y * 2), black)
                outfile1.putpixel((x * 2 + 1, y * 2), black)
                outfile1.putpixel((x * 2, y * 2 + 1), white)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), white)

                outfile2.putpixel((x * 2, y * 2), black)
                outfile2.putpixel((x * 2 + 1, y * 2), black)
                outfile2.putpixel((x * 2, y * 2 + 1), white)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), white)  
            elif opt==6:
                outfile1.putpixel((x * 2, y * 2), white)
                outfile1.putpixel((x * 2 + 1, y * 2), white)
                outfile1.putpixel((x * 2, y * 2 + 1), black)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), black)

                outfile2.putpixel((x * 2, y * 2), white)
                outfile2.putpixel((x * 2 + 1, y * 2), white)
                outfile2.putpixel((x * 2, y * 2 + 1), black)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), black)  

outfile1.save('out1.jpg')
outfile2.save('out2.jpg')