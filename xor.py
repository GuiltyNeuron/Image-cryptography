import cv2
import numpy as np
from numpy import random
from scipy import signal


# Load original image
demo = cv2.imread("images/test2.png")
r, c, t = demo.shape

# Create random key
key = random.randint(256, size = (r, c, t))

# Encryption
enc = demo ^ key

# decryption
dec = enc ^ key

cv2.imwrite("encrypted.png", enc)
cv2.imwrite("decrypted.png", dec)
cv2.imwrite("key.png", key)
