import cv2
import numpy as np


# load images
print("reading images")
img1 = cv2.imread('one.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, dsize=(460, 640), interpolation=cv2.INTER_AREA)

img2 = cv2.imread('two.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, dsize=(460, 640), interpolation=cv2.INTER_AREA)

img1_patches = []
img2_patches = []

# draw square
def mouse_event1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN	:
        if len(img1_patches) == 4 :
          print("all points are fully selected")
        else :
          print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
          cv2.rectangle(param, (x-7, y-7), (x+7, y+7), (255,0,0), 1)
          img1_patches.append(img1[y-7-1:y+7, x-7-1:x+7])
          cv2.imshow('img1', param)

def mouse_event2(event, x, y, flags, param):    
    if event == cv2.EVENT_LBUTTONDOWN	:
        if len(img2_patches) == 4 :
          print("all points are fully selected")
        else :
          print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
          cv2.rectangle(param, (x-7, y-7), (x+7, y+7), (255,0,0), 1)
          img2_patches.append(img2[y-7-1:y+7, x-7-1:x+7])
          cv2.imshow('img2', param)

# get user inputs
cv2.imshow('img1', img1)
cv2.setMouseCallback('img1', mouse_event1, img1)

cv2.imshow('img2', img2)
cv2.setMouseCallback('img2', mouse_event2, img2)

# calculate img1_patches's gradient direction and gradient magnitude
img1_gradient_direction = []
img1_gradient_magnitude = []

cv2.waitKey(0)


for x in img1_patches:
  # x = np.float32(x)/255.0
  gx = cv2.Sobel(x, cv2.CV_32F, 1, 0, ksize = 1)
  gy = cv2.Sobel(x, cv2.CV_32F, 0, 1, ksize = 1)

  mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
  img1_gradient_direction.append(angle)
  img1_gradient_magnitude.append(mag)

# calculate img2_patches's gradient direction and gradient magnitude
img2_gradient_direction = []
img2_gradient_magnitude = []

for x in img2_patches:
  # x = np.float32(x)/255.0
  gx = cv2.Sobel(x, cv2.CV_32F, 1, 0, ksize = 1)
  gy = cv2.Sobel(x, cv2.CV_32F, 0, 1, ksize = 1)

  mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
  img2_gradient_direction.append(angle)
  img2_gradient_magnitude.append(mag)

cv2.destroyAllWindows()

# fill vector bins
def add_count_histogram(vector, dir, mag):
  if dir >= 180:
    dir = dir - 180
  share = int(dir/20)
  remainder = dir%20

  if remainder == 0:
    vector[0][share] += mag  
  elif share == 8:
    vector[0][share] += mag/20.0 * (20 - remainder)
    vector[0][0] += mag/20.0 * remainder
  else :
    vector[0][share] += mag/20.0 * (20 - remainder)
    vector[0][share+1] += mag/20.0 * remainder

# draw histograms of gradient
print("img1 histograms of gradient")
img1_histograms = []
for i in range(0,4):
  vector = np.zeros((1,9))
  for x in range(0,15):
    for y in range(0,15):
      add_count_histogram(vector, img1_gradient_direction[i][x][y], img1_gradient_magnitude[i][x][y])

  img1_histograms.append(vector)
  print(vector)

print("img2 histograms of gradient")
img2_histograms = []
for i in range(0,4):
  vector = np.zeros((1,9))
  for x in range(0,15):
    for y in range(0,15):
      add_count_histogram(vector, img2_gradient_direction[i][x][y], img2_gradient_magnitude[i][x][y])

  img2_histograms.append(vector)
  print(vector)



