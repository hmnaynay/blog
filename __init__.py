from flask import Flask, render_template
from models import Post

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja', posts=Post.get_all())

if __name__ == '__main__':
    app.run(debug=True)
