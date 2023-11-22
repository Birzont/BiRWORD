# pip install Flask

from flask import Flask, render_template, request
from collections import Counter
import re

app = Flask(__name__)


def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    word_count = Counter(words)
    word_count['Total words'] = len(words)
    return word_count


@app.route('/', methods=['GET', 'POST'])
def word_counter():
    word_count = None
    input_text = None

    if request.method == 'POST':
        input_text = request.form['input_text']
        word_count = count_words(input_text)

    return render_template('index.html', word_count=word_count, input_text=input_text)


if __name__ == '__main__':
    app.run(debug=True)
