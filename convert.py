import cv2
import numpy as np
from matplotlib import pyplot as plt

fig, axes = plt.subplots(3,2)

for i in range(3):
  fileName = f'bird_{i+1}.jpg'

  img = cv2.imread(f'img/{fileName}',0)

  axes[i,0].hist(img.ravel(),256,[0,256])

  converted_img = (img - np.mean(img))/np.std(img)*16 + 64
  print(converted_img.mean())

  axes[i,1].hist(converted_img.ravel(),256,[0,256])
  cv2.imwrite(f'result/{fileName}', converted_img)
plt.show()
