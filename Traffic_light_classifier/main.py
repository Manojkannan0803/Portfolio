import cv2 # computer vision library
import helpers # helper functions

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # for loading in images
import os
import helper_functions
import test_functions

# Image data directories
IMAGE_DIR_TRAINING = "Traffic_light_classifier/traffic_light_images/training/"
IMAGE_DIR_TEST = "Traffic_light_classifier/traffic_light_images/test/"

# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TRAINING)

# Check whether IMAGE_LIST is updated correctly
print(os.path.abspath(IMAGE_DIR_TRAINING))
print(len(IMAGE_LIST))

# Visualize the input images
f, axes = plt.subplots(1, 3, figsize=(20, 10))

# Select three images
indices = [0, 750, 900]  # You can adjust these indices if needed

for i, idx in enumerate(indices):
    image, label = IMAGE_LIST[idx]  # Extract image and label
    axes[i].imshow(image)
    axes[i].set_title(f"Label: {label}\nShape: {image.shape}")
    axes[i].axis("off")

plt.show()

# Dynamically find a yellow traffic light
yellow_image = None
for img, lbl in IMAGE_LIST:
    if lbl == "yellow":
        yellow_image = img
        break

# Display the yellow traffic light if found
if yellow_image is not None:
    plt.figure(figsize=(5, 5))
    plt.imshow(yellow_image)
    plt.title("Yellow Traffic Light")
    plt.axis("off")
    plt.show()
else:
    print("No yellow traffic light found in the dataset.")

# Standardize all training images
STANDARDIZED_LIST = helper_functions.standardize(IMAGE_LIST)

# Visualize the standardized data
# Select a non-standardized image from IMAGE_LIST
non_standardized_image, _ = IMAGE_LIST[0]  # You can change the index to compare different images

# Select a standardized image from STANDARDIZED_LIST
standardized_image, _ = STANDARDIZED_LIST[0]  # You can change the index to compare different images

# Display the non-standardized image
plt.subplot(1, 2, 1)
plt.imshow(non_standardized_image)
plt.title("Non-Standardized Image")
plt.axis("off")

# Display the standardized image
plt.subplot(1, 2, 2)
plt.imshow(standardized_image)
plt.title("Standardized Image")
plt.axis("off")

# Show both images for comparison
plt.show()

# RGB to HSV conversion
# Visualize the individual color channels

image_num = 0
test_im = STANDARDIZED_LIST[image_num][0]
test_label = STANDARDIZED_LIST[image_num][1]

if test_im is None or test_im.size == 0:
    print("Error: Image is empty or invalid")
else:
    print("Image shape:", test_im.shape)

# Convert to HSV
hsv = cv2.cvtColor(test_im, cv2.COLOR_RGB2HSV)

# Print image label
print('Label [red, yellow, green]: ' + str(test_label))

# HSV channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Plot the original image and the three channels
f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20,10))
ax1.set_title('Standardized image')
ax1.imshow(test_im)
ax2.set_title('H channel')
ax2.imshow(h, cmap='gray')
ax3.set_title('S channel')
ax3.imshow(s, cmap='gray')
ax4.set_title('V channel')
ax4.imshow(v, cmap='gray')

# Testing the classifier
# Using the load_dataset function in helpers.py
# Load test data
TEST_IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TEST)

# Standardize the test data
STANDARDIZED_TEST_LIST = helper_functions.standardize(TEST_IMAGE_LIST)

# Shuffle the standardized test data
random.shuffle(STANDARDIZED_TEST_LIST)

# Find all misclassified images in a given test set
MISCLASSIFIED = helper_functions.get_misclassified_images(STANDARDIZED_TEST_LIST)

# Accuracy calculations
total = len(STANDARDIZED_TEST_LIST)
num_correct = total - len(MISCLASSIFIED)
accuracy = num_correct/total

print('Accuracy: ' + str(accuracy))
print("Number of misclassified images = " + str(len(MISCLASSIFIED)) +' out of '+ str(total))

# Call the function with your list of misclassified images
helper_functions.visualize_misclassified(MISCLASSIFIED)

# Test if any red lights as green are classified
# Importing the tests
tests = test_functions.Tests()

if(len(MISCLASSIFIED) > 0):
    # Test code for one_hot_encode function
    tests.test_red_as_green(MISCLASSIFIED)
else:
    print("MISCLASSIFIED may not have been populated with images.")