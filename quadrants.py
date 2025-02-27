import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('tree.jpg')

# Get the dimensions of the image
height, width, channels = image.shape

# Find the center of the image
center_x, center_y = width // 2, height // 2

# Slice the image into four quadrants
top_left = image[:center_y, :center_x]
top_right = image[:center_y, center_x:]
bottom_left = image[center_y:, :center_x]
bottom_right = image[center_y:, center_x:]

# Display the quadrants using matplotlib
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot each quadrant
axs[0, 0].imshow(cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB))
axs[0, 0].axis('off')

axs[0, 1].imshow(cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB))
axs[0, 1].axis('off')

axs[1, 0].imshow(cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB))
axs[1, 0].axis('off')

axs[1, 1].imshow(cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB))
axs[1, 1].axis('off')

# Show the plot
plt.show()
