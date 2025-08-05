from flask import Flask, request, jsonify
import pdfplumber
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/process', methods=['POST'])
def process_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        doc = nlp(text)
        # Simple score: count of significant words (nouns, verbs)
        score = sum(1 for token in doc if token.pos_ in ['NOUN', 'VERB'])
        return jsonify({"filename": file.filename, "ats_score": score})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)