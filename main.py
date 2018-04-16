from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y337keefret43sdg3sf'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(10000))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST','GET'])
def index():
    return redirect("/blog")

@app.route('/blog', methods=['POST','GET'])
def blog():
    entry_id = request.args.get('id')
    blog_posts = Blog.query.all()
    if entry_id:
        blog_post = Blog.query.filter_by(id=entry_id).first()
        return render_template('blog.html', title="Build A Blog", blog_post=blog_posts)
    return render_template("blog.html", title="Build A Blog", blog_posts=blog_posts)


#@app.route('/newpost', methods=['POST','GET'])

if __name__ == '__main__':
    app.run()

