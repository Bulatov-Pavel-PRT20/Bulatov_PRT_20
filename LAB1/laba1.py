import cv2

# Load .png image
image = cv2.imread('image.png')

# Save .jpg image
cv2.imwrite('image.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
