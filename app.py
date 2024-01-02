from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    name = "Shreyansh Tripathi"
    usn = "1BM20IS148"
    return f"Hello! My name is {name} and my USN is {usn}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
