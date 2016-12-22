# python show.py plik1.png plik2.png
from PIL import Image
import sys

black = 0
white = 255

infile1 = Image.open(sys.argv[1])
infile2 = Image.open(sys.argv[2])

outfile = Image.new('1', (infile1.size[0]//2,infile1.size[1]//2))

for x in range(0, infile1.size[0]-1, 2):
    for y in range(0, infile1.size[1]-1, 2):
        pix = [
        		min(infile1.getpixel((x,y)),infile2.getpixel((x,y))),
        		min(infile1.getpixel((x+1,y)),infile2.getpixel((x+1,y))),
        		min(infile1.getpixel((x,y+1)),infile2.getpixel((x,y+1))),
        		min(infile1.getpixel((x+1,y+1)),infile2.getpixel((x+1,y+1))) 
        		]
        if 255 in pix:
        	outfile.putpixel((x//2, y//2), white)
        else:
        	outfile.putpixel((x//2,y//2), black)

outfile.save("clean.png")
#outfile.show()
