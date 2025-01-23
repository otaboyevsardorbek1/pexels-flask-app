from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

# Pexels API orqali ma'lumot qidirish
def data_search(query: str, page: int, per_page: int):
    headers = {
        'Authorization': 'Nr27imlsXUtEaeM90TWGtJqtpuuv01o7KLOa1uUpHcxsvkAgRSqe8M3s',
    }
    params = {
        'query': query,
        'page': page,
        'per_page': per_page,
    }
    response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
    if response.status_code != 200:
        return None
    return response.json()

# API asosiy sahifasi
@app.route('/')
def index():
    return render_template('index.html')

# Rasmlarni qidirish API
@app.route('/api/v1/search')
def api_search():
    query = request.args.get('query', default='python')
    page = int(request.args.get('page', default=1))
    per_page = int(request.args.get('per_page', default=15))

    data = data_search(query=query, page=page, per_page=per_page)
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "Ma'lumot olishda xato yuz berdi"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3090)
