

2D_Histogram_Filter
Refer: 2D_Histogram_filter_Python/Project_description.txt for the detailed description about 2D histogram filter implemented in python

Kalman_filter implementation
Refer: Kalman_filter/Project_description.txt for the detailed description about Kalman_filter implemented in python

Technologies Used:
Python 3.x
Matplotlib (for visualizing beliefs)
NumPy (for matrix and grid operations)
Random module (for simulating sensor errors)

Route_Planner:
🚀 A* Path Planning Implementation in Python
This project implements the A search algorithm* for pathfinding using a modular approach. The PathPlanner class dynamically integrates various helper functions from PathPlanner_functions.py, making it flexible and easily extendable.

🛠 Features
A Search Algorithm*: Efficient pathfinding from a start node to a goal node.
Modular Design: Functions are dynamically attached to PathPlanner for flexibility.
Predefined Maps: Supports map_10 and map_40 datasets.
Visualization: Option to visualize maps and computed paths.
Automated Testing: Includes test.py for validating correctness.

📂 Project Structure
📦 Project Root
├── helpers.py               # Helper functions for loading and visualizing maps
├── PathPlanner.py           # Main PathPlanner class for A* pathfinding
├── PathPlanner_functions.py # Collection of functions dynamically added to PathPlanner
├── test.py                  # Test suite for validating pathfinding logic
└── main.py                  # Entry point to run the A* algorithm

🚀 Quick Start
1. Clone the repository:
     git clone https://github.com/yourusername/a-star-path-planner.git
     cd a-star-path-planner
2. Install dependencies (if any).
3. Run the main script to test the path planner: python main.py
4. (Optional) Visualize the generated path by uncommenting the show_map calls.

🧪 Running Tests
To verify the implementation, run: python test.py

Running the planner on map_40 with start node 5 and goal node 34 should produce: great! Your code works for these inputs!

Traffic Light Classifier

Overview
This project implements a traffic light classifier using computer vision techniques. The classifier processes traffic light images, standardizes them, and applies HSV color space transformations to accurately distinguish between red, yellow, and green signals. The model is trained and tested using an image dataset of traffic lights.

Features
1. Loads and preprocesses traffic light images from a dataset.
2. Standardizes image dimensions for consistent processing.
3. Converts RGB images to HSV for better color-based classification.
4. Implements a classification algorithm to identify traffic light colors.
5. Evaluates performance and identifies misclassified images.
6. Provides visualization for analysis of misclassified images.

Project Structure
Traffic_light_classifier/
│── traffic_light_images/
│   ├── training/  # Training dataset
│   ├── test/  # Test dataset
│── helpers.py  # Helper functions for dataset loading and processing
│── helper_functions.py  # Standardization and classification functions
│── test_functions.py  # Functions for evaluating classification accuracy
│── classifier.py  # Main script to train and test the classifier

Dependencies
Ensure you have the following Python libraries installed: pip install opencv-python numpy matplotlib

Usage
1. Clone the repository:
   git clone https://github.com/yourusername/traffic-light-classifier.git
   cd traffic-light-classifier
2. Run the classifier script: python classifier.py
3. The program will:
     Load and preprocess training images.
     Standardize image dimensions.
     Convert images to HSV color space.
     Train and evaluate the classifier.
     Display classification accuracy and misclassified images.

Results
1. The classifier evaluates test images and calculates accuracy.
2. Misclassified images are visualized for further analysis

Future Improvements
1. Implement a deep learning model for improved accuracy.
2. Expand dataset for better generalization.
3. Integrate real-time traffic light detection using video feeds.

License
This project is open-source and available under the MIT License.
