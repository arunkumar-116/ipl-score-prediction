from flask import Flask, render_template, request
import numpy as np
import joblib
import bz2

app = Flask(__name__)

def predict_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model):
    prediction_array = []
    # Batting Team
    teams = ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders',
             'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
    for team in teams:
        if batting_team == team:
            prediction_array.append(1)
        else:
            prediction_array.append(0)
    
    # Bowling Team
    for team in teams:
        if bowling_team == team:
            prediction_array.append(1)
        else:
            prediction_array.append(0)
    
    prediction_array += [runs, wickets, overs, runs_last_5, wickets_last_5]
    prediction_array = np.array([prediction_array])
    
    pred = model.predict(prediction_array)
    return int(round(pred[0]))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_score', methods=['POST'])
def predict():
    try:
        with bz2.BZ2File('forest_model.pbz2', 'rb') as f:
            model = joblib.load(f)
            if not hasattr(model, 'predict'):
                raise TypeError("The loaded object is not a valid model. It does not have a 'predict' method.")
    except FileNotFoundError:
        return "Model file not found. Please ensure 'forest_model.pbz2' exists."
    except Exception as e:
        return f"Error loading model: {str(e)}"

    batting_team = request.form['batting-team']
    bowling_team = request.form['bowling-team']
    runs = float(request.form['runs'])
    wickets = int(request.form['wickets'])
    overs = float(request.form['overs'])
    runs_last_5 = int(request.form['runs_in_prev_5'])
    wickets_last_5 = int(request.form['wickets_in_prev_5'])

    try:
        predicted_score = predict_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model)
        return render_template('result.html', my_prediction=predicted_score)
    except Exception as e:
        return f"Error making prediction: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
