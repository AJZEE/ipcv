
import cv2
import numpy as np

# Read image
image = cv2.imread('image.jpg')

# Get image dimensions
(h, w) = image.shape[:2]

# 1. Scaling
fx = 1.5  # Scale factor in x direction
fy = 1.5  # Scale factor in y direction
scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

# 2. Rotation
center = (w // 2, h // 2)  # Rotation center (center of the image)
angle = 45  # Degrees of rotation
scale = 1.0  # No scaling during rotation
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# 3. Translation
tx = 100  # Shift in x direction
ty = 50   # Shift in y direction
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

# Display the results in three windows
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.imshow("Scaled Image", scaled_image)
cv2.waitKey(0)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.imshow("Translated Image", translated_image) 

cv2.waitKey(0)
cv2.destroyAllWindows()
