from flask import Flask
app = Flask(__name__)

# index page route
@app.route('/')
def board():
    return "Example Web Page"

# read parameter and write in page
@app.route('/<article_idx>')
def board_view(article_idx):
    return article_idx

app.run(host='0.0.0.0',port=80)