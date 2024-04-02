# QRS Complex ALgorithm
This repository holds the code for an QRS complex detection algorithms based on finding the rate of change of the acquired signal and add it as a feature column. 
Once this feature is appende to the dataset, a binary encoding of the rate of change represents a detected QRS complex.
Following this, a machine learning algorithm is trained on this mathematical model.

# The Datasets
The signal acquired is a time-domain electrocardiagram with the y-axis being the voltage meassured in the ECG. 
This signal has been retreieve at a laboratory using an MP36/35 unit, performing an electrocardiogram.
There are two dataset (one for training, another for testing).

# Mathematical Model
The mathematical model follows two functions:

## Rate of Change Function
- Take the first and second derivative of the signal
- Add the absolute values of these two results.
- Transform the signal from time domain to frequency domain.
- Apply a low pass filter
- return the signal to the time domain

## QRS Detection
- Randomly select 4 windows (500 ms [approximate QRS coomplex length]) in the dataset and calcualtes their maximum values from this
- Finds the mean value from the these and stores it as threshold parameter.
- Iterates through the data and binary encodes and stores the indexes in which a QRS complex was detected.

# Training the Machine Learning Model
Before applying the both the Rate of Change function and the QRS one, we clean the training dataset and create a preprocessing pipeline using sklearn.
Pass the dataset into the pipeline and train a machine learning model, in this case a support vector classifier model, using the dataset.

# Testing the Model on Other Datasets
Finally, once we have a trained model, we perform a prediction by using our second subject's dataset.

## Before Prediction
![image](https://github.com/Joas329/QRS-Complex-Dection-Algoirthm/assets/51135069/6659c313-9f05-42b2-9ec6-08790598a8d3)


## After Prediction
![image](https://github.com/Joas329/QRS-Complex-Dection-Algoirthm/assets/51135069/4f4d7b38-1db2-4669-b673-10437b7c3649)
