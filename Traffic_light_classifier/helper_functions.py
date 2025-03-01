import cv2 # computer vision library
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # for loading in images
import os
import numpy as np

def standardize_input(image):
    """Pre-process an image by cropping, resizing, and normalizing."""

    # Ensure image has 3 channels (RGB)
    image = np.copy(image)
    
    # Define cropping values
    row_crop = 7
    col_crop = 8
    
    # Adjust cropping dynamically if the image is too small
    row_crop = min(row_crop, image.shape[0] // 2)
    col_crop = min(col_crop, image.shape[1] // 2)
    
    # Crop the image
    image_crop = image[row_crop:-row_crop, col_crop:-col_crop, :]
    
    # Resize to 32x32 with high-quality interpolation
    standard_im = cv2.resize(image_crop, (32, 32), interpolation=cv2.INTER_AREA)
    
    # Convert BGR to RGB only if necessary
    if image.shape[-1] == 3 and np.mean(image[:,:,0] - image[:,:,2]) > 0:  
        standard_im = cv2.cvtColor(standard_im, cv2.COLOR_BGR2RGB)

    # Normalize pixel values to range [0,1]
    standard_im = standard_im.astype(np.float32) / 255.0  

    return standard_im


# Standardize the output
# one-hot encoding
## Given a label - "red", "green", or "yellow" - return a one-hot encoded label

# Examples: 
# one_hot_encode("red") should return: [1, 0, 0]
# one_hot_encode("yellow") should return: [0, 1, 0]
# one_hot_encode("green") should return: [0, 0, 1]

def one_hot_encode(label):
    
    ## TODO: Create a one-hot encoded label that works for all classes of traffic lights
    # Initialize the one-hot encoded array as [0, 0, 0]
    one_hot_encoded = [0, 0, 0]
    
    # Map label to the corresponding index in the array
    if label == "red":
        one_hot_encoded[0] = 1
    elif label == "yellow":
        one_hot_encoded[1] = 1
    elif label == "green":
        one_hot_encoded[2] = 1
    
    return one_hot_encoded

# STANDARDIZED_LIST of input images and output labels
def standardize(image_list):
    # Empty image data array
    standard_list = []

    # Iterate through all the image-label pairs
    for item in image_list:
        image = item[0]
        label = item[1]

        # Check if the image is valid (not None and not empty)
        if image is None or image.size == 0:
            print(f"Error: Invalid image encountered with label {label}")
            continue  # Skip this image and move to the next one

        # Standardize the image
        standardized_im = standardize_input(image)

        # One-hot encode the label
        one_hot_label = one_hot_encode(label)

        # Append the image, and its one-hot encoded label to the full, processed list of image data 
        standard_list.append((standardized_im, one_hot_label))

    return standard_list

# Create a brightness feature that uses HSV color space
def create_feature(rgb_image):
    """Extracts brightness-based features for detecting traffic light colors."""
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    
    # Define crop regions for red, yellow, and green light positions
    red_region = hsv_image[:13, 10:-10, 2]    # Brightness (V) channel for red
    yellow_region = hsv_image[12:21, 10:-10, 2]  # Yellow
    green_region = hsv_image[21:, 10:-10, 2]  # Green

    # Compute features: Sum and Mean Brightness
    red_brightness = np.sum(red_region) / (red_region.size + 1e-5)  # Avoid division by zero
    yellow_brightness = np.sum(yellow_region) / (yellow_region.size + 1e-5)
    green_brightness = np.sum(green_region) / (green_region.size + 1e-5)

    # Compute contrast: Standard deviation of brightness for each region
    red_std = np.std(red_region)
    yellow_std = np.std(yellow_region)
    green_std = np.std(green_region)

    # Return feature vector
    feature = [red_brightness, red_std, yellow_brightness, yellow_std, green_brightness, green_std]
    
    return feature

# a complete classifier
def estimate_label(rgb_image):
    """
    Classifies a traffic light image as Red, Yellow, or Green based on brightness in specific regions.
    Returns a one-hot encoded label.
    """
    # Extract region-specific features
    features = create_feature(rgb_image)
    red_brightness, red_std, yellow_brightness, yellow_std, green_brightness, green_std = features

    # Define thresholds based on brightness values
    if red_brightness > yellow_brightness and red_brightness > green_brightness:
        predicted_label = [1, 0, 0]  # Red
    elif yellow_brightness > red_brightness and yellow_brightness > green_brightness:
        predicted_label = [0, 1, 0]  # Yellow
    elif green_brightness > red_brightness and green_brightness > yellow_brightness:
        predicted_label = [0, 0, 1]  # Green
    else:
        # Fallback: Choose the most confident brightness value
        max_brightness = max(red_brightness, yellow_brightness, green_brightness)
        if max_brightness == red_brightness:
            predicted_label = [1, 0, 0]
        elif max_brightness == yellow_brightness:
            predicted_label = [0, 1, 0]
        else:
            predicted_label = [0, 0, 1]

    return predicted_label

# Constructs a list of misclassified images given a list of test images and their labels
def get_misclassified_images(test_images):
    # Track misclassified images by placing them into a list
    misclassified_images_labels = []

    # Iterate through all the test images
    # Classify each image and compare to the true label
    for image in test_images:

        # Get true data
        im = image[0]
        true_label = image[1]
        assert(len(true_label) == 3), "The true_label is not the expected length (3)."

        # Get predicted label from your classifier
        predicted_label = estimate_label(im)
        assert(len(predicted_label) == 3), "The predicted_label is not the expected length (3)."

        # Compare true and predicted labels 
        if(predicted_label != true_label):
            # If these labels are not equal, the image has been misclassified
            misclassified_images_labels.append((im, predicted_label, true_label))
            
    # Return the list of misclassified [image, predicted_label, true_label] values
    return misclassified_images_labels

# Visualize misclassified example(s)
def visualize_misclassified(misclassified_list):
    # Ensure there are misclassified images
    if len(misclassified_list) == 0:
        print("No misclassified images.")
        return
    
    # Select the first misclassified example to visualize
    image, predicted_label, true_label = misclassified_list[0]
    
    # Convert the image from BGR to RGB for proper display with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Plot the image
    plt.imshow(image_rgb)
    plt.axis('off')  # Turn off axis labels
    plt.title(f"Predicted: {['red', 'yellow', 'green'][predicted_label.index(1)]} | True: {['red', 'yellow', 'green'][true_label.index(1)]}")
    plt.show()