from flask import Flask, request

app = Flask(__name__)

@app.route('/index', methods=['POST','GET'])
def index():
    print request.headers
    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)