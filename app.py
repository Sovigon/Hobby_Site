# To initialize a test, use "python -m flask run" from the folder

from flask import Flask, render_template
from os import walk
import calendar as cal

app = Flask(__name__)

# Routes for the site

@app.route('/')
def index():

    return render_template("landing_page.html")

@app.route('/<article_arg>')
def hobby(article_arg):

    articles = article_gen(article_arg)

    return render_template(
        "hobby.html",
        article_arg=article_arg,
        articles=articles
    )

# Functions

def article_gen(article_arg):
    article_folder = sorted(next(walk('/home/Sovigon/Hobby_Site/static/articles/' + article_arg))[1])
    print(article_folder)

    # 3 Character Code to Hobby Folder Lookup
    hobby_types = {
        'art':'art',
        'pgm':'coding',
        '3dp':'3d-printing'
    }

    article_list = []

    for article in article_folder:
        article_add = []

        hobby_type = article[0:3].lower()

        # 0 Article Type
        article_add.append(hobby_type)
        # 1 Hobby Folder
        article_add.append(hobby_types[hobby_type])
        # 2 Article Year
        article_add.append(article[3:7])

        month = article[7:9]

        # 3 Article Month (Numbers)
        article_add.append(month)
        # 4 Article Month (Letters)
        article_add.append(cal.month_name[int(month)])
        # 5 Article Day
        article_add.append(article[9:11])
        # 6 Article Name
        article_add.append((article[11:].replace("_", " ")).title())
        # 7 Article Folder Name
        article_add.append(article)

        article_list.append(article_add)

    return article_list

@app.context_processor
def file_reader():

    # Each folder has summary.txt and article.txt
    # Thumbnail image is first line of summary.txt

    def summary_reader(hobby, folder):

        f = open(
            "/home/Sovigon/Hobby_Site/static/articles/" +
            hobby + "/" +
            folder +
            "/summary.txt",
            "r"
        )

        thmbnl = ""
        summary = []
        count = 0

        while True:

            txt_line = f.readline()

            if count == 0:
                thmbnl = txt_line

            elif not txt_line:
                break

            else:
                summary.append(txt_line)

            count += 1

        f.close()

        return thmbnl, summary

    return dict(summary_reader=summary_reader)

