# IPL Score Prediction ML Web Application

This web application predicts the total score of an IPL match based on the input of the current score, runs, and wickets. It utilizes machine learning algorithms to make these predictions.

## Dataset

The dataset used for training the model comprises over-by-over details of matches and runs from 2008 to 2020.

- **mid**: Match ID
- **date**: Date of the match
- **venue**: Venue of the match
- **bat_team**: Batting team
- **bowl_team**: Bowling team
- **batsman**: Batsman
- **bowler**: Bowler
- **runs**: Runs scored
- **wickets**: Wickets
- **overs**: Overs
- **run_last_5**: Runs scored in the last 5 overs
- **wicket_last_5**: Wickets in the last 5 overs
- **striker**: Batsman playing as main (1)
- **non-striker**: Batsman playing as runner-up, not main (0)
- **total**: Total score (target variable)

## Project Overview

The Indian Premier League (IPL) is a professional Twenty20 cricket league in India contested during April and May of every year by teams representing Indian cities. With the increasing popularity of the IPL, there is a growing interest in predicting match outcomes, including the total score.

This project aims to predict the total score of an IPL match based on various factors such as the current score, number of runs, and wickets. By leveraging machine learning algorithms, the application provides users with an estimate of the final score, helping cricket enthusiasts and analysts make informed decisions.

## Exploratory Data Analysis (EDA)

The dataset used for training the model comprises over-by-over details of matches and runs from 2008 to 2020. Before building the prediction model, an Exploratory Data Analysis (EDA) was performed to gain insights into the dataset. The EDA included:

- Analysis of the distribution of runs scored and wickets taken in matches.
- Identification of trends in runs scored and wickets taken over the years.
- Examination of the relationship between the total score and other variables such as runs in the last 5 overs and wickets in the last 5 overs.
- Visualization of the data using plots such as histograms, scatter plots, and line plots.

The EDA helped in understanding the dataset better and provided valuable insights for building the prediction model.

## Model Algorithms

The following machine learning algorithms were evaluated for predicting the total score:

- Decision Tree
- Linear Regression
- Random Forest Regression
- Lasso Regression
- Support Vector Machine (SVM)
- Neural Network

The Random Forest Regression algorithm was selected as the best performing model, achieving an accuracy of 93.11%.

## Dependencies

- blinker==1.8.2
- click==8.1.7
- colorama==0.4.6
- Flask==3.0.3
- gunicorn==22.0.0
- itsdangerous==2.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- packaging==24.0
- Werkzeug==3.0.3
- numpy==1.26.4
- joblib==1.2.0
- scikit-learn==1.5.0

## Development Process
- **Data Cleaning**: The dataset was cleaned to remove missing values and ensure consistency.
- **Data Preprocessing and Encoding**: Categorical variables were encoded, and data was normalized for model training.
- **Model Building**: Various machine learning algorithms were trained and evaluated for evaluation you can refer to
  'ipl-score-predictor.ipynd' in this repository.
- **Best Model Selection**: Random Forest Regression was selected as the best performing model.

## Usage

To use the web application, run the following link in your browser:

```bash
https://bit.ly/3V7JbVs
