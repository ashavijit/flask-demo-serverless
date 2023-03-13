from flask import Flask, jsonify, request

app =  Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/ip')
def ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/info')
def info():
    return jsonify({'ip': request.remote_addr, 'user_agent': request.headers.get('User-Agent')}), 200