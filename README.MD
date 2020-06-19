# Sparkify Capstone Project

At this project, we predict churn for a fictional streaming service called Sparkify. 

The complete analysis and discussion are available [here](https://medium.com/@brunowdev/predicting-churn-with-pyspark-sparkify-capstone-project-5ad91781c491?source=friends_link&sk=26df5c31c0983f8d59f6d2939190511f).


<div align="center">
    <img src="https://brunobitencourt.com/public/images/sparkify_logo.png" width="200" height="200" />
    <p>Do you want to churn?
</p>
</div>

### Table of Contents

1. [Requirements](#requirements)
2. [Project Overview](#overview)
3. [File Descriptions](#files)
4. [Running the project](#running)
5. [Results](#results)

## Requirements <a name="requirements"></a>

- Python 3
- The comple list of requirents can be found at `requirements.txt`

## Project Overview <a name="overview"></a>

At this project, we try to predict if a user will churn (Canceling the service) given some information regarding the service interactions.

In the future, we can try to predict if the user will Downgrade the subscription (became a free user).

I've applied four classification algorithms and several techniques to work with the data. 

To allow an easy visualization, I've hosted the notebook HTML files online, so you will see a static version, without the need to open the .ipynb at the GitHub (which is usually slow and hangs for large files).

- [The notebook with the training process](https://brunobitencourt.com/data/udacity/sparkify/Sparkify.html);
- [The result analysis - For all the algorithms and metrics](https://brunobitencourt.com/data/udacity/sparkify/Results+-+Spark.html);
- [The data exploration (with the raw data and the final version with the new engineered features)](https://brunobitencourt.com/data/udacity/sparkify/Data+Exploration.html).

To a more complete analysis, I recommend check my article [here](https://medium.com/@brunowdev/predicting-churn-with-pyspark-sparkify-capstone-project-5ad91781c491?source=friends_link&sk=26df5c31c0983f8d59f6d2939190511f).


## File Descriptions <a name="files"></a>

<pre>
.
├── results/ # Folder with the static version of the notebooks - Also hosted online (See at the project overview)
├── pyspark.sh # The file to run and config PySpark for local mode
├── visualizations.py # The implementation of some visualizations on Plotly, for a more interactive heatmap (See on the data exploration notebook)
├── jupyter_utils.py # A script to config pandas for a standard view between all the notebooks
├── Data Exploration.ipynb # Notebook with the exploration of the raw data and after the feature engineering
├── Sparkify.ipynb # Notebook with the exploration and feature engineering
├── Results - Spark.ipynb # Notebook with all the visualizations related to the results of training and the GridSearch
├── requirements.txt # The project dependencies
</pre>

#### Dataset:

The dataset was given by Udacity. I've hosted on my S3 to make it more comfortable to download and work between my environments.

- The full dataset is available [here](https://brunobitencourt.com/data/udacity/sparkify/full_sparkify_event_data.json) - 12Gb:
  
- I've created a small version without some columns (firstName, lastName, location, userAgent), but with all the events - available [here](https://brunobitencourt.com/data/udacity/sparkify/sparkify_full_csv_data.csv) - 2Gb.


Raw Dataset features

- `ts`: Event timestamp in milliseconds 
- `gender`: M or F
- `firstName`: First name of the user
- `lastName`: Last name of the user
- `length`: Length of the song
- `level`: Level of subscription `free` or `paid.`
- `registration`: User registration timestamp 
- `userId`: User id at the service
- `auth`: If the user is logged
- `page`: Action of the event (next song, thumps up, thumbs down)
- `sessionId`: Id of the session
- `location`: Location of the event
- `userAgent`: Browser/web agent of the event
- `song`: Name of the song
- `artist`: Name of the artist
- `method`: HTTP method of the event
- `status`: HTTP status of the request (200, 404)


## Running the project <a name="running"></a>

To run the training code, you can run the `pyspark.sh.` file, then just go to the Sparkify notebook.
The next step is to decide which version of the data will fit you. For example, there are three variations of the load file.
The medium dataset, the entire dataset as JSON, or the entire dataset as CSV (my version of it, as I've mentioned at the [files section](#dataset)).

To running locally, I recommend downloading the dataset, so you won't need to download each time with Spark.

If you want to run the visualizations, don't forget to install the requirements, especially the plotly lib.

## Results <a name="results"></a>

<div align="center">
    <p>Best results for each model</p>
    <img src="https://s3-sa-east-1.amazonaws.com/brunobitencourt.com/data/udacity/sparkify/results_df.png" width="1694" height="266" />
</div>

---

<div align="center">
    <img src="https://s3-sa-east-1.amazonaws.com/brunobitencourt.com/data/udacity/sparkify/all_models.png" width="600" height="600" />
</div>

---

<div align="center">
    <p>Heatmap - Absolute value</p>
    <img src="https://s3-sa-east-1.amazonaws.com/brunobitencourt.com/data/udacity/sparkify/features_absolute.png" width="1000" height="1000" />
</div>

---

<div align="center">
    <p>Heatmap - Feature vs. music listening time</p>
    <img src="https://s3-sa-east-1.amazonaws.com/brunobitencourt.com/data/udacity/sparkify/newplot.png" width="1000" height="1000" />
</div>
