# Sparkify Capstone Project

## File Descriptions <a name="files"></a>

There are some variations of this dataset:

- A set with the first 2 million lines is available here:
    - https://brunobitencourt.com/data/udacity/sparkify/2m_rows_sparkify_event_data.csv

- The full dataset is available here:
    - https://brunobitencourt.com/data/udacity/sparkify/full_sparkify_event_data.json

- There are two more versions:
    - https://brunobitencourt.com/data/udacity/sparkify/mini_sparkify_event_data.json
    - https://brunobitencourt.com/data/udacity/sparkify/medium_sparkify_event_data.json

## Churn types

- Downgrade subscription
- Canceling the service

## Dataset

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