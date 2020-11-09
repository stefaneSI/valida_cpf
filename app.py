from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#roda a aplicação localhost na porta 9095
if __name__ == '__main__':
    app.run(port=9095, host = '', debug=True)