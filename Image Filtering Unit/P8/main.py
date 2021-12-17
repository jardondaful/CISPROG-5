from images import Image

def sepia(image):
  for i in range(image.height):
    for j in range(image.width):
      #conversion to grayscale starts
      (red, green, blue) = image.getPixel(j, i)
      red = int(red * 0.299)
      green = int(green * 0.587)
      blue = int(blue * 0.114)
      sum_of_colors = red + green + blue
      image.setPixel(j, i, (sum_of_colors, sum_of_colors, sum_of_colors))
      #conversion to grayscale ends
      (red, green, blue) = image.getPixel(j, i)
      if red < 63:
        red = int(red * 0.9)
        blue = int(blue * 0.9)
      elif red < 192:
        red = int(red*1.15)
        blue = int(blue * 0.85)
      else:
        red=min(int(red*1.08), 255)
        blue=int(blue * 0.93)
      image.setPixel(j, i, (red, green, blue))


def main():
  image = Image("smokey.gif")
  sepia(image)
  image.draw()

main()
