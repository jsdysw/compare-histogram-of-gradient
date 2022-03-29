

# Abstract
* I’ll compare histograms of gradient between two different patches, catching same objects’ point, of different images 

# Experiement Process

* 1) select four pairs of patches of the same points (15 by 15)
* 
<img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160585761-b23c4f2d-b7d1-4893-8682-c3e23cdf4afb.png"><img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160585782-be5236d8-17a4-4ade-8cda-9eac6d8b854c.png">

* Sobel mask for each direction gx and gy (calculate gradient)
<img width="156" alt="image" src="https://user-images.githubusercontent.com/76895949/160586537-64bb2986-8745-4313-8904-2f9021b76dc2.png">

```python
gx = cv2.Sobel(x,cv2.CV_32F, 1, 0, ksize = 1)
gy = cv2.Sobel(x,cv2.CV_32F, 0, 1, ksize = 1)
```
  
구한 gx, gy를 가지고 patch를 구성하는 각 픽셀에 대해서 gradient의 magnitude와 angle을 구한다. 
 
이제Gradient의 histogram을 만들어보자. direction의 범위는 [0,180]이다. Gradient의 화살표와 180도 반대 방향의 화살표는 동일하게 간주한다. Bin의 크기는 20이다. 붉은 원으로 표시한 픽셀의 경우 10은 0, 20 범위의 중간에 있고 magnitude는 4이므로 2, 2씩 나뉘어 0, 20 bin에 값이 더해진다.
![image](https://user-images.githubusercontent.com/76895949/160586383-0e69c564-f765-4cc6-8c0a-f44945c77aa6.png)


* histogram-of-gradient.py gets points' coordinates from users' mouth input at runtime but doesn't plot histogram
* histogram-of-gradient.ipynb gets points' coordinates at compile time but plots histogram



# Hisogram of Gradient

# Result
<img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160544822-bc5228b1-008d-4721-b300-795fc8287ff9.png"><img width="150" alt="image" src="https://user-images.githubusercontent.com/76895949/160544838-777cc88d-37ea-41f8-8212-f9bb1b5224df.png">

* see how similar thoese patches' histogram of grandient are.
