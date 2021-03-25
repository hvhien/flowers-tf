
from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

# Khởi tạo Flask
app = Flask(__name__)
# run_with_ngrok(app)

# Hàm xử lý request
@app.route("/", methods=['GET'])
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
