from images import Image

def sharpen(image,degree,threshold):
  for i in range(image.getHeight()):
    for j in range(image.getWidth()):
      (red, green, blue) = image.getPixel(j,i)
      average_of_colors = (red+blue+green)//3
      if(average_of_colors>threshold):
        average_of_colors = int(average_of_colors*(1-degree/100))
      image.setPixel(j,i, (average_of_colors, average_of_colors,average_of_colors)) 

def main():
  image = Image("black_and_white_smokey.gif")
  sharpen(image, 50, 30)
  image.draw()

if __name__=="__main__":
  main()
