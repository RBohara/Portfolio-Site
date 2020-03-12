from flask import Flask, render_template, flash, redirect, url_for
from form import ContactForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '742331d211df56414159dd73cdc5bced'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    title = db.Column(db.String(30), nullable=False)
    technologies = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=False)
    github_link = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"Project('{self.image_file}', '{self.title}', '{self.technologies}', '{self.description}', '{self.github_link}')"

projects = [
    
    {
        'screenshot': 'picture',
        'title': 'Flask website',
        'technologies': 'Flask, Sqlite, HTML, CSS, Javascript',
        'description': 'This website is built for applying the learnings.',    
        'github_link': 'url to github repository',    
    },
    {
        'screenshot': 'picture',
        'title': 'Django website',
        'technologies': 'Django, Sqlite, HTML, CSS, Javascript',
        'description': 'This website is built for applying the learnings.',    
        'github_link': 'url to github repository',    
    }
]

@app.route("/")
def home():
    return render_template('home.html', title='About Me')

@app.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Your message was successfully sent!!!", 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', title='Contact Me', form=form)

@app.route("/projects")
def project():
    return render_template('projects.html', title='Projects', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)