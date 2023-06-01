from flask import Flask, render_template

app = Flask(__name__)


class Item:
    def __init__(self,
                 name,
                 price):
        self.name = name
        self.price = price


items = [Item("Product 1", 100),
         Item("Product 2", 200),
         Item("Product 3", 300),
         Item("Product 4", 400),
         Item("Product 5", 500),
         Item("Product 6", 600),
         Item("Product 7", 700),
         Item("Product 8", 800),
         Item("Product 9", 900),
         Item("Product 10", 1000)]


@app.route("/items")
def view_items():
    return render_template("items.html",
                           items=enumerate(items))


@app.route("/items/<int:item_number>")
def index(item_number):
    item = items[item_number]
    return render_template("page.html", item=item)


@app.route("/hello")
def hello():
    return "NO"


@app.route("/user/<user_name>")
def hello_user(user_name):
    return f"Hello {user_name}"


if __name__ == "__main__":
    app.run()
