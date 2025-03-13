import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a low-contrast image (use your own low contrast image file here)
image = cv2.imread('low_contrast_image.jpg', cv2.IMREAD_GRAYSCALE)

# Step 1: Enhance the image using CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_image = clahe.apply(image)

# Step 2: Compute the histograms of the original and enhanced images
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_enhanced = cv2.calcHist([enhanced_image], [0], None, [256], [0, 256])

# Step 3: Plot the histograms and images
plt.figure(figsize=(12, 6))

# Plot histogram for the original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Low-Contrast Image')
plt.axis('off')

# Plot histogram for the original image
plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Histogram of Original Low-Contrast Image')
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Plot histogram for the enhanced image
plt.subplot(2, 2, 3)
plt.imshow(enhanced_image, cmap='gray')
plt.title('Enhanced Image (CLAHE)')
plt.axis('off')

# Plot histogram for the enhanced image
plt.subplot(2, 2, 4)
plt.plot(hist_enhanced, color='black')
plt.title('Histogram of Enhanced Image (CLAHE)')
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Show the images and histograms
plt.tight_layout()
plt.show()
