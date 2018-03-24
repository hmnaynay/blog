from flask import Flask, render_template, request, redirect, url_for
from models import Post

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja', posts=Post.get_all())

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('new.jinja')

    # Get data from request.
    title = request.form['title']
    content = request.form['content']

    Post.new(title, content)

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
