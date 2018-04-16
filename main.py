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

    def is_valid(self):

        if self.title and self.body:
            return True
        else:
            return False

@app.route('/', methods=['POST','GET'])
def index():
    return redirect("/blog")

@app.route('/blog', methods=['POST','GET'])
def blog():
    post_id = request.args.get('id')
    if post_id:
        blog = Blog.query.filter_by(id=post_id).first()
        return render_template('individualblog.html', title=blog.title, body=blog.body)
    else:
        posts = Blog.query.all()
        return render_template("blog.html", title="Build A Blog", posts=posts)

@app.route('/newpost', methods=['POST','GET'])
def newpost():
    if request.method == 'POST':
        blog_title = request.form['title']
        blog_body = request.form['body']
        new_post = Blog(blog_title, blog_body)

        if new_post.is_valid():
            db.session.add(new_post)
            db.session.commit()
            url = '/blog?id=' + str(new_post.id)
            return redirect(url)
        else:
            flash("Both a title and body are required for the blog.")
            return render_template('newpost.html',
            title='Add A Blog Entry', 
            blog_title=blog_title, 
            blog_body=blody_body)
    else:
        return render_template('newpost.html', title='Add a  Blog Entry')

if __name__ == '__main__':
    app.run()

