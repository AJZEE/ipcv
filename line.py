import cv2

# Load the image
image = cv2.imread('cat.jpg')

# Get the dimensions of the image
height, width, channels = image.shape

# Find the center of the image
center_x, center_y = width // 2, height // 2

# Draw a vertical line at the center
cv2.line(image, (center_x, 0), (center_x, height), (255, 0, 0), 1)  # blue vertical line

# Draw a horizontal line at the center
cv2.line(image, (0, center_y), (width, center_y), (255, 0, 0), 1)  # blue horizontal line

# Display the image with the lines
cv2.imshow('Image with Center Lines', image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
