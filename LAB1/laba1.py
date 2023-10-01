import cv2

# Load .png image
image = cv2.imread('scene.png')

# Save .jpg image
cv2.imwrite('scene.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
