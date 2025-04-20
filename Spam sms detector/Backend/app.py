from flask import Flask, request, jsonify
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from flask_cors import CORS

# nltk.download('punkt')
# nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

# Load the model and vectorizer
tfidf = pickle.load(open('transform.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
ps = PorterStemmer()

# Text preprocessing function
def transformation(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    l = [i for i in text if i.isalnum()]
    l = [i for i in l if i not in stopwords.words('english') and i not in string.punctuation]
    l = [ps.stem(i) for i in l]

    return " ".join(l)

# API route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'email' not in data:
        return jsonify({'error': 'No email content provided'}), 400

    email = data['email']
    transformed_text = transformation(email)
    vector_input = tfidf.transform([transformed_text])
    result = model.predict(vector_input)[0]

    return jsonify({'prediction': 'Spam' if result == 1 else 'Not Spam'})

if __name__ == '__main__':
    app.run(debug=True)
# Congratulations on completing the project successfully!
# We’re excited to have you on board for the next phase.
# Please let me know when you’re available to meet.
# You have been selected to receive $1000 cash!
# Click here to claim your money right now.
# This offer is valid for a limited time only