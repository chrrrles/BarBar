from PIL import Image
from sys import argv

if __name__ == "__main__":
    fname = argv[1]
    im = Image.open(fname)
    w,h = im.size

    image_const = "const CRGB image[RESOLUTION][NUM_LEDS] = {\n"
    pic = im.load()
    for x in range(w):
        column = []
        for y in range(h):
            rgb = pic[x,y]
            if rgb[0:3] == (0,0,0):
                RGB = "CRGB::Black"
            else:
                RGB = "CRGB( %d, %d, %d)" % (rgb[0], rgb[1], rgb[2])
            column.append(RGB)
        image_const += "    { %s },\n" % ", ".join(str(x) for x in column)
    image_const += "};\n"

    print "#define NUM_LEDS %d" % h
    print "#define RESOLUTION %d" % w
    print "CRGB leds[%d];" % h
    print ""
    print image_const
