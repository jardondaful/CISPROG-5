from images import Image

def grayscale1(image):
  for i in range(image.getHeight()):
    for j in range(image.getWidth()):
      (red, green, blue) = image.getPixel(j, i)
      red = int(red * 0.299)
      green = int(green * 0.587)
      blue = int(blue * 0.114)
      sum_of_colors = red+green+blue
      image.setPixel(j, i, (sum_of_colors, sum_of_colors, sum_of_colors))

def grayscale2(image):
  for i in range(image.getHeight()):
    for j in range(image.getWidth()):
      (red, green, blue) = image.getPixel(j, i)
      average_color = (red + green + blue) // 3
      image.setPixel(j, i, (average_color, average_color, average_color))

def main():
  image = Image("smokey.gif")
  grayscale2(image)
  image.draw()

if __name__ == "__main__":
  main()
