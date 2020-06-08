# Sparkify Capstone Project


At this project, we predict churn for a fictional streaming service called Sparkify. 

The complete analysis and discussion are available [here](https://medium.com/@brunowdev/predicting-churn-with-pyspark-sparkify-capstone-project-5ad91781c491?source=friends_link&sk=26df5c31c0983f8d59f6d2939190511f).


<div align="center">
    <img src="https://brunobitencourt.com/public/images/sparkify_logo.png" width="200" height="200" />
</div>


### Table of Contents

1. [Requirements](#requirements)
2. [Project Overview](#overview)
3. [File Descriptions](#files)
4. [Running the project](#running) 

## Requirements <a name="requirements"></a>

- Python 3
- The comple list of requirents can be found at `requirements.txt`

## Project Overview <a name="overview"></a>

- TODO

Churn types

- Downgrade subscription
- Canceling the service


## File Descriptions <a name="files"></a>

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



