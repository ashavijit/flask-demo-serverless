from flask import Flask, jsonify, request

app =  Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/ip')
def ip():
    return jsonify({'ip': request.remote_addr}), 200