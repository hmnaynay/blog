from flask import Flask, render_template, request, redirect, url_for
from models import Post
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja', posts=Post.find())

@app.route('/post/<oid>')
def post(oid):
    return render_template('post.jinja', post=Post(ObjectId(oid)))

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('new.jinja')

    Post.new(
        title=request.form['title'],
        content=request.form['content']
    )

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
