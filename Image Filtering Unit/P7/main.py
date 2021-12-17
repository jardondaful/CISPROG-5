from images import Image

def invert(image):
  for i in range(image.height):
    for j in range(image.width):
      (red, green, blue) = image.getPixel(j, i)
      red = 255-red
      green = 255-green
      blue = 255 - blue
      image.setPixel(j, i, (red, green, blue))

def main(): 
  image = Image("smokey.gif")
  invert(image)
  image.draw()

if __name__=="__main__":
  main()
