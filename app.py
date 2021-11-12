#To start the server:
#python3 -m flask run

from flask import Flask, render_template, request
import re

import os

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def on_index():
    return render_template("index.html")


@app.route("/ch<num>")

def on_chapter(num):

    num = re.search("\d+", num).group(0)
    title, content = get_chapter(num)
    return render_template("chapter.html", title=title, chapter_text=content)


@app.route("/registration")

def on_registration():
    return render_template("registration.html")



@app.route("/registration_complete", methods=["GET", "POST"])
def on_reg_compl():
    form = request.form
    print(form)
    return "done!"




def get_chapter(num):
    
    with app.open_resource("static/chapter_"+str(num)+".txt", "rt") as f:
        content = f.read()
        
    title = ""
    with app.open_resource("static/chapter_names.txt", "rt") as f:
        for line in f:
            m = re.search("\d+", line)
            parsed_num = m.group(0)
            if parsed_num==num:
                title = line
                break
        
    return title, content    

        




