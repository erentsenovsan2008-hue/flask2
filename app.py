from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

dishes = [
    {
        "id": 1,
        "name": "Джомба",
        "description": "Калмыцкий чай с молоком и солью"
    },
    {
        "id": 2,
        "name": "Борцоки",
        "description": "Традиционная калмыцкая выпечка"
    },
    {
        "id": 3,
        "name": "Бёрики",
        "description": "Тесто с мясной начинкой"
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dishes")
def all_dishes():
    return render_template("dishes.html", dishes=dishes)


@app.route("/dish/<int:id>")
def dish(id):
    for item in dishes:
        if item["id"] == id:
            return render_template("dish.html", dish=item)

    return "Блюдо не найдено"


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        name = request.form["name"]
        description = request.form["description"]

        if name and description:
            new_dish = {
                "id": len(dishes) + 1,
                "name": name,
                "description": description
            }

            dishes.append(new_dish)

            return redirect(url_for("all_dishes"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)