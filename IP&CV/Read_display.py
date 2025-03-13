import cv2;
import matplotlib.pyplot as plt;
import numpy as np;
silverhand=cv2.imread("johnny.jpg")

resized=cv2.resize(silverhand,(750,500))

grayTest = cv2.cvtColor(silverhand, cv2.COLOR_BGR2GRAY)
edgeTest = cv2.Canny(silverhand, 50, 50)

# cv2.imshow("JS", silverhand)
# cv2.imshow("JS", grayTest)
# cv2.imshow("JS", edgeTest)
# cv2.imshow("JS",resized)


silverhandSmall = cv2.resize(silverhand, (0, 0), fx = .05, fy = (.1*.5)) 
grayTest = cv2.resize(grayTest, (200, 400)) 
  
edgeTest = cv2.resize(edgeTest, (780, 540)) 

titles=["JS","small js","JS resize","gray JS","edged JS"]
total_list=[silverhand,silverhandSmall,resized,grayTest,edgeTest]

# for i in range(len(total_list)):
#     plt.subplot(2,3,i+1)
#     plt.title(titles[i])
#     plt.imshow(total_list[i])

# plt.show()

m = np.random.randn(4,4)

# apply the cv2.transform to perform matrix transformation
img_tr = cv2.transform(silverhand, m, None)

# display the transformed image 
cv2.imshow("Transformed Image", img_tr)
cv2.waitKey(0)