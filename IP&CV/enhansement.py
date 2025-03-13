import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a low-contrast image (for demonstration, a sample image is used)
image = cv2.imread('low_contrast_image.jpg', cv2.IMREAD_GRAYSCALE)

# Step 1: Image Enhancement using CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_image = clahe.apply(image)

# Step 2: Image Enhancement using Histogram Equalization
hist_eq_image = cv2.equalizeHist(image)

# Step 3: Image Enhancement using Gamma Correction
gamma = 1.5
gamma_corrected_image = np.array(255*(image / 255) ** gamma, dtype='uint8')

# Step 4: Segmentation using Otsu's Thresholding
_, otsu_thresholded = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Step 5: Edge Detection using Canny
edges = cv2.Canny(enhanced_image, 100, 200)

# Step 6: Displaying the images
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Original Low Contrast Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(enhanced_image, cmap='gray')
axes[0, 1].set_title('Enhanced Image (CLAHE)')
axes[0, 1].axis('off')

axes[0, 2].imshow(hist_eq_image, cmap='gray')
axes[0, 2].set_title('Histogram Equalized')
axes[0, 2].axis('off')

axes[1, 0].imshow(gamma_corrected_image, cmap='gray')
axes[1, 0].set_title('Gamma Corrected Image')
axes[1, 0].axis('off')

axes[1, 1].imshow(otsu_thresholded, cmap='gray')
axes[1, 1].set_title('Otsu Thresholding Segmentation')
axes[1, 1].axis('off')

axes[1, 2].imshow(edges, cmap='gray')
axes[1, 2].set_title('Edge Detection (Canny)')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()
