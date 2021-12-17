from images import Image

def posterize(image, RGBtuple):
  for i in range(image.height):
    for j in range(image.width):
      white = (255,255,255)
      (red, green, blue) = image.getPixel(j, i)
      average_color = (red + green + blue)//3
      if average_color < 128:
        image.setPixel(j,i, (RGBtuple))
      else:
        image.setPixel(j, i, white)

def main():
  red = int(input("Enter an integer from 0 to 255 for red: "))
  green = int(input("Enter an integer from 0 to 255 for green: "))
  blue = int(input("Enter an integer from 0 to 255 for blue: "))    
  image = Image("smokey.gif")
  posterize(image, (red, green, blue))
  image.draw()

if __name__=="__main__":
  main()
