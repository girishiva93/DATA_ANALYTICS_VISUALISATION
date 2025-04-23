
# Dataset link: 
# https://www.kaggle.com/datasets/jakewright/2m-daily-weather-history-uk?select=all_weather_data.csv

import kagglehub

path = kagglehub.dataset_download("jakewright/2m-daily-weather-history-uk")
print("Path to dataset files:", path)