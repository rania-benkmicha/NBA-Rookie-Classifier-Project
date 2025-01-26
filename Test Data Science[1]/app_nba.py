from flask import Flask, render_template, request, jsonify
from joblib import load


app = Flask(__name__)
modele = load('trained_model.pkl')
loaded_scaler = load('scaler_model.pkl')
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

def predict(player_data):
    prediction = modele.predict(player_data)
    
    return prediction.tolist()

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        classe=''
        data = request.form.to_dict()
        print(data)
        print(type(data))
        player_data = {key: float(value) for key, value in data.items()}
        normalized_data = loaded_scaler.transform([list(player_data.values())])
        result = predict(normalized_data)
        print("result",result)
        if result[0]==0:
            classe="Ce joueur ne vaut pas le coup d’investir sur lui"
        elif result[0]==1:
            classe="Ce joueur vaut le coup d’investir sur lui"
        return render_template('result.html', prediction=classe)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
