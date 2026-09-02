from matplotlib import pyplot as plt
from functions import loadData

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
!pip install -q imbalanced-learn
from imblearn.over_sampling import SMOTE


class BinaryClassifierCNN(nn.Module):
    def __init__(self):
        super(BinaryClassifierCNN, self).__init__()
        # Increasing the convolutional layers
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.conv5 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)

        self.pool = nn.AvgPool2d(2, 2)
        
        # Adjusting the fully connected layers to match the output size after added layers
        self.fc1 = nn.Linear(256 * 46 * 45, 1024) # 46 and 45 are the dimensions of the image after the last pool laye, 256 is the number of channels
        self.fc2 = nn.Linear(1024, 256) # 256 is the number of channels from the above linear layer
        self.fc3 = nn.Linear(256, 1)
        
        # Additional batch normalization layers for added conv layers
        self.bn1 = nn.BatchNorm2d(16)
        self.bn2 = nn.BatchNorm2d(32)
        self.bn3 = nn.BatchNorm2d(64)
        self.bn4 = nn.BatchNorm2d(128)
        self.bn5 = nn.BatchNorm2d(256)
        
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        # Shape of x is (10, 1, 1500, 1470)
        x = self.pool(F.relu(self.bn1(self.conv1(x)))) # Shape of x is (10, 16, 750, 735)
        x = self.pool(F.relu(self.bn2(self.conv2(x)))) # Shape of x is (10, 32, 375, 367)
        x = self.pool(F.relu(self.bn3(self.conv3(x)))) # Shape of x is (10, 64, 187, 183)
        x = self.pool(F.relu(self.bn4(self.conv4(x)))) # Shape of x is (10, 128, 93, 91)
        x = self.pool(F.relu(self.bn5(self.conv5(x)))) # Shape of x is (10, 256, 46, 45)
        x = torch.flatten(x, 1)  # Flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc3(x))
        return x
    

image_arrays, labels = loadData(method = 'resize')
image_arrays, labels = image_arrays.astype(float), labels.astype(float)
image_arrays = image_arrays / 255.0

tp, tn, fp, fn = 0, 0, 0, 0

for i in range(0, len(image_arrays)):
    single_image = image_arrays[i]
    # Define the transformation
    

    # Assuming 'single_image' is a numpy array with shape (1500, 1470)
    input_tensor = torch.from_numpy(single_image[None, :, :]).float()
    input_tensor = input_tensor.unsqueeze(0)  # Add batch dimension
    input_tensor = input_tensor.to('cpu')  # Move tensor to the same device as model

    # Make prediction
    with torch.no_grad():
        prediction = model(input_tensor)
        predicted_class = prediction  # Assuming binary classification

    print(f'Predicted class: {round(predicted_class.item())}, \nlabel: {labels[i]}')

    pred_val = round(predicted_class.item())
    true_val = labels[i]

    if pred_val == 1 and true_val == 1:
        print('True Positive')
        tp = tp + 1
    elif pred_val == 0 and true_val == 0:
        print('True Negative')
        tn = tn + 1
    elif pred_val == 1 and true_val == 0:
        print('False Positive')
        fp = fp + 1
    elif pred_val == 0 and true_val == 1:
        print('False Negative')
        fn = fn + 1
    else:
        print('Error')

print(f'TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}')