import re
import string 
from collections import Counter 
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def preprocess_txt(text):
    text = text.translate(str.maketrans('','', string.punctuation))
    text = text.lower()
    return text 

def calculate_word_frequencies(text):
    words = re.findall(r'\b\w+\b',text)
    return Counter(words)


def calculate_cosine_similarity(freq1, freq2):
    intersection = set(freq1.keys()) & set(freq2.keys())
    numerator = sum([freq1[word]* freq2[word] for word in intersection])

    sum_squared_freq1 = sum([freq1[word]** 2 for word in freq1.keys()])
    sum_squared_freq2 = sum([freq2[word]** 2 for word in freq2.keys()])

    denominator = (sum_squared_freq1 ** 0.5) * (sum_squared_freq2 ** 0.5)

    if not denominator:
        return 0.0 
    return round((float(numerator) / denominator),2) 

def similarity_score(text1,text2):
    text1 = preprocess_txt(text1)
    text2 = preprocess_txt(text2)
    freq1 = calculate_word_frequencies(text1)
    freq2 = calculate_word_frequencies(text2)
    similarity = calculate_cosine_similarity(freq1,freq2)
    return similarity


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare',methods=['POST'])
def compare_texts():
    data = request.get_json()
    if 'text1' not in data or 'text2' not in data:
        return jsonify({'error':'Missing text1 or Text2 in the request body'})
    
    text1 = data['text1']
    text2 = data['text2']

    score = similarity_score(text1,text2)
    return jsonify({'similarity_score': score})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)





