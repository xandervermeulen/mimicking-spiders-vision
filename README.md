# Nope Cam
## How to use the project and make predictions with the Unity3d recordings

### Step 1: Install the required packages
```bash
pip install -r requirements.txt
```
### Step 2: Store Recordings
- Make recordings in Unity3d nope-cam project
- Store the recordings in a folder called `recordings_{date}` in the root directory of the project
  - The unity project also stores the position of the redball in a file `positions_{date}.csv`
### Step 3: Track the ball in the recordings
In the file [StoreDataOfAllRecordings.ipynb](DataProcessing%2FStoreDataOfAllRecordings.ipynb), at the top fill in the variables correctly and run the notebook.
This will store the position of the red ball in the recordings with the name and output location you gave in the variables
- note: In the notebook [TrackBallFromVideo.ipynb](DataProcessing%2FTrackBallFromVideo.ipynb) you can watch how the ball is tracked in the video.
### Step 4: Optional: Use interpolation to fill in missing values
If your data has some missing values, you can use the [TrajectoryPredictionInterpolation.ipynb](ball-prediction%2FTrajectoryPredictionInterpolation.ipynb) notebook to interpolate the missing values.
This will not always work, but if there are not too many it should work fine.
### Step 5: Train the model
In the [Neural_Network_Demo.ipynb](Demo%2FNeural_Network_Demo.ipynb) notebook, fill in the variables at the top and run the notebook.
This notebook uses a neural network to predict the position of the ball in the 3d space.
It is import to note that you need to put multiple trajectories in the training data to get a good result.
It is a good idea to concatenate the data from multiple recordings together into 1 large dataset (one for input X and one for out y).
As the test trajectory, ideally give a trajectory that is not in the training data.
At the end of the notebook you can see the result of the prediction.

## Research
##### In the folder [ball-prediction](ball-prediction)
- You can find the research we did on all different types of interpolation
- The [TrajectoryPredictionInterpolation.ipynb](ball-prediction%2FTrajectoryPredictionInterpolation.ipynb) notebook is the notebook that we used to interpolate the missing values in the data by using polynomial interpolation.
  This gave the best results for our data.
- In [TrajectoryPredictionLinear.ipynb](ball-prediction%2FTrajectoryPredictionLinear.ipynb), [TrajectoryPredictionSeperateLinear.ipynb](ball-prediction%2FTrajectoryPredictionSeperateLinear.ipynb), [TrajectoryPredictionSeperateSVM.ipynb](ball-prediction%2FTrajectoryPredictionSeperateSVM.ipynb)
  We tried to predict the position of the ball on one of the cameras by using the position of the ball on the other cameras as input. The results were not good. 

##### In the folder [GaussianProcess](GaussianProcess)
- You can find all the research and trying out of the Gaussian Process model.

##### In the folder [NeuralNetworks](NeuralNetworks)
- The date of the notebook is given in the name. Each notebook tries out a different neural network, a diffrent amount of cameras, pixels, angle or interpolation etc. 
- All the results are shown at the end of the notebook.

##### In the folder [DataProcessing](DataProcessing)
- The notebook [StoreDataOfAllRecordings.ipynb](DataProcessing%2FStoreDataOfAllRecordings.ipynb) is used to convert the recordings to the position of the ball on the screen.
- The notebook [TrackBallFromVideo.ipynb](DataProcessing%2FTrackBallFromVideo.ipynb) is used to track the ball in the video.
- The notebook [GeneratingEntireDataset.ipynb](DataProcessing%2FGeneratingEntireDataset.ipynb) can be used to create a large dataset from different files.

##### In the folder [Demo](Demo)
- The notebook [Neural_Network_Demo.ipynb](Demo%2FNeural_Network_Demo.ipynb) common notebook where you need to fill in the variables and it will instantly train the model and show the result of the prediction.
- All other notebooks are an overview of the results of the different models we tried out.

##### In the folder [results](results)
- We show a few graphs about the metrics of the models we tried out.