from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    movie_name = request.form['movie_name']
    url = f'http://www.omdbapi.com/?apikey=5b39c85&t={movie_name}'
    response = requests.get(url)
    movie_data = response.json()
    if movie_data['Response'] == 'False':
        return render_template('index.html', error='No se encontró la película.')
    else:
        rating = movie_data['imdbRating']
        return render_template('results.html', movie_name=movie_name, rating=rating)


if __name__ == '__main__':
    app.run(debug=True)
