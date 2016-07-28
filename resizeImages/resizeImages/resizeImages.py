import PIL
from PIL import Image
import glob, os


def makeSmaller(org):
    basewidth = 500
    img = Image.open(org)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('small_'+org)


if __name__ == "__main__":
    os.chdir(".")
    for file in glob.glob("*.jpg"):
        print(file)
        makeSmaller(file)

    print "DONE"

