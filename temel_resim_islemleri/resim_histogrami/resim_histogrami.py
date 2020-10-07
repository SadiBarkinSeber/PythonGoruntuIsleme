import cv2
import numpy as np
from matplotlib import pyplot as plt  # eğer yüklü değilse, cmd --> pip install matplotlib

img = cv2.imread("a40.jpg")
b, g, r = cv2.split(img)
cv2.imshow("img", img)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
