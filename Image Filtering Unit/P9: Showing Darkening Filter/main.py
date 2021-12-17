from images import Image

def darken(image, amount):
  for i in range(0,image.height):
    for j in range(0,image.width):
      (red, green, blue) = image.getPixel(j, i)
      red = red - amount
      green = green - amount
      blue = blue - amount
      if(red<0):
        red = 0
      if(green<0):
        green = 0
      if(blue<0):
        blue = 0
      image.setPixel(j, i, (red, green, blue))


def lighten(image, amount):
  for i in range(0,image.height):
    for j in range(0,image.width):
      (red, green, blue) = image.getPixel(j, i)
      red = red + amount
      green = green + amount
      blue = blue + amount
      if(red>255):
        red = 255
      if(green>255):
        green = 255
      if(blue>255):
        blue = 255
      image.setPixel(j, i, (red, green, blue))

#first entry of tuple represents red, second entry of tuple represents green, and the third entry of the tuple represents blue
def ColorFilter(image, RGBtuple):
  for i in range(0,image.height):
    for j in range(0,image.width):
      (red, green, blue) = image.getPixel(j, i)
      red = red + RGBtuple[0]
      if red >255:
        red = 255
      green = green + RGBtuple[1]
      if green > 255:
        green = 255
      blue = blue + RGBtuple[2]
      if blue > 255:
        blue = 255
      image.setPixel(j, i, (red, green, blue))

def main():
  image = Image("smokey.gif")
  darken(image, 125)
  image.draw()
  

if __name__=="__main__":
  main()
