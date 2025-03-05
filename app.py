from flask import *
import requests

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_book",methods=["GET","POST"])
def get_book():
    if request.method=="POST":
        book_name=request.form["book_name"]
        url=f"https://freetestapi.com/api/v1/books?sort={book_name}"
        response=requests.get(url)
        data=response.json()
        if response.status_code==200:
            title=data[0]["title"]
            author=data[0]["author"]
            publication_year=data[0]["publication_year"]
            genre=data[0]["genre"]
            description=data[0]["description"]
            return render_template("index.html",title=title,author=author,publication_year=publication_year,genre=genre,description=description)
        else:
            return render_template("index.html",error="Book not found")

    



if __name__=="__main__":
    app.run()