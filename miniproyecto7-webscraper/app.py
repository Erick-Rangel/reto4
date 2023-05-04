from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    url = request.form['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Obtenemos los títulos y fechas de publicación de las noticias
    news_titles = []
    news_dates = []
    for article in soup.find_all('article', {'class': 'post'}):
        title = article.find('h2', {'class': 'entry-title'}).text.strip()
        date = article.find('time', {'class': 'entry-date'}).text.strip()
        news_titles.append(title)
        news_dates.append(date)
    # Devolvemos los resultados en una página HTML usando la plantilla result.html
    return render_template('result.html', news_titles=news_titles, news_dates=news_dates)

if __name__ == '__main__':
    app.run()
