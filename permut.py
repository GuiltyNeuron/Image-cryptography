import cv2
import numpy as np
from numpy import random
from scipy import signal


# Load original image
demo = cv2.imread("images/test2.png")
r, c, d= demo.shape

# keys
l1 = np.arange(0, c)
l1 = np.take(l1,np.random.permutation(l1.shape[0]),axis=0,out=l1)

l2 = np.arange(0, r)
l2 = np.take(l2,np.random.permutation(l2.shape[0]),axis=0,out=l2)

# Encryption
encrypted_image = np.zeros((r, c, d), np.uint8)
encrypted_image2 = np.zeros((r, c, d), np.uint8)
x = 0
for i in l1:
    encrypted_image[x,:,:] = demo[i,:,:]
    x += 1

x = 0
for i in l2:
    encrypted_image2[:,x,:] = encrypted_image[:,i,:]
    x += 1

cv2.imwrite("encrypted.png",encrypted_image2)


# Decryption
decrypted_image = np.zeros((r, c, d), np.uint8)
decrypted_image2 = np.zeros((r, c, d), np.uint8)

x = 0
for i in l2:
    decrypted_image[:,i,:] = encrypted_image2[:,x,:]
    x += 1

x = 0
for i in l1:
    decrypted_image2[i,:,:] = decrypted_image[x,:,:]
    x += 1


cv2.imwrite("decrypted.png",decrypted_image2)

