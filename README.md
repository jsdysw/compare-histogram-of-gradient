

# Abstract
* I’ll compare histograms of gradient between two different patches, catching same objects’ point, of different images 

# Experiement Process

1. select four pairs of patches of the same points (15 by 15)

<img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160585761-b23c4f2d-b7d1-4893-8682-c3e23cdf4afb.png"><img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160585782-be5236d8-17a4-4ade-8cda-9eac6d8b854c.png">

2. Sobel mask for each direction gx and gy (calculate gradient)
<img width="200" alt="image" src="https://user-images.githubusercontent.com/76895949/160586537-64bb2986-8745-4313-8904-2f9021b76dc2.png">

```python
gx = cv2.Sobel(x,cv2.CV_32F, 1, 0, ksize = 1)
gy = cv2.Sobel(x,cv2.CV_32F, 0, 1, ksize = 1)
```

3. With gx and gy, calculate gradient maginitude and angle per patch.
 
<img width="350" alt="image" src="https://user-images.githubusercontent.com/76895949/160587309-261737c2-6ffa-4b8f-97b7-5c36319f6041.png">

```python
mag, angle = cv2.cartToPolar(gx,gy, angleInDegrees=True)
```

4. Make the histogram of gradient. 
<img width="215" alt="image" src="https://user-images.githubusercontent.com/76895949/160588494-b39d3ff2-55e3-4f75-8668-8bb405907db6.png">


* histogram-of-gradient.py gets points' coordinates from users' mouth input at runtime but doesn't plot histogram
* histogram-of-gradient.ipynb gets points' coordinates at compile time but plots histogram

# Result
<img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160544822-bc5228b1-008d-4721-b300-795fc8287ff9.png"><img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160544838-777cc88d-37ea-41f8-8212-f9bb1b5224df.png">

* see how similar thoese patches' histogram of grandient are.
