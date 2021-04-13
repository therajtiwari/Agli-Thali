from flask import Flask, url_for
from flask.templating import render_template
import utils

app = Flask(__name__)
utils.loadArtifacts()


@app.route("/")
def home():
    # return "Hello world"
    dishes_names, diet_of_dishes = utils.getDishNames()

    # pagination
    count = 21
    total_pages = round(
        len(dishes_names) /
        count) if round(len(dishes_names)) % count == 0 else round(
            len(dishes_names) / count) + 1
    dishes = dishes_names[0:count]
    diet = ["all_diet"] * count

    final_dishes = dict(zip(dishes, diet))

    return render_template("home.html",
                           dishes=final_dishes,
                           total_pages=total_pages,
                           current_page=1,
                           page_type="main")


@app.route("/diet", defaults={"name": "all", "pagenum": 1})
@app.route("/diet/<name>/<int:pagenum>")
@app.route("/diet/<name>", defaults={"pagenum": 1})
def diet(name, pagenum):
    count = 21
    dishes_names, diet = utils.getDietWiseDishes(name)
    total_pages = round(
        len(dishes_names) /
        count) if round(len(dishes_names)) % count == 0 else round(
            len(dishes_names) / count) + 1
    dishes = dishes_names[28 * (pagenum - 1):28 * pagenum]

    if name == "vegetarian" or name == "non-vegetarian":
        diet = diet[28 * (pagenum - 1):28 * pagenum]
    else:
        diet = ["all_diet"] * len(dishes)
    final_dishes = dict(zip(dishes, diet))
    print(final_dishes)
    return render_template(
        "home.html",
        dishes=final_dishes,
        current_diet=name,
        total_pages=total_pages,
        current_page=pagenum,
    )


if __name__ == "__main__":
    app.run(debug=True)