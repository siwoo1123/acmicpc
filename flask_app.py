from flask import Flask, jsonify
import requests as req
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/<problem>')
def getProblem(problem):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url = f'https://www.acmicpc.net/problem/{problem}'
    res = req.get(url, headers=headers)
    code = 200
    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.select_one('#problem_title').text
    else:
        name = 'ERROR'
        code = 404

    return jsonify({
        'problemNumber': problem,
        'url': url,
        'title': name,
        'statusCode': code
    }), code
