from flask import Flask, request, jsonify
from model.survey_automation import automate_survey
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/submit-survey', methods=['POST'])
def analyze():
    data = request.json
    survey_code = data['survey_code']
    result = automate_survey(survey_code)
    return jsonify({"Result": result})


if __name__ == '__main__':
    app.run(port=5000)
