from flask import Flask, url_for, redirect
from flask.templating import render_template
from flask_jsglue import JSGlue
import utils

app = Flask(__name__)

jsglue = JSGlue()
jsglue.init_app(app)

utils.loadArtifacts()

dishes, diet_of_dishes = utils.getDishNames()


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
    if (len(dishes_names) % count) == 0:
        total_pages = (len(dishes_names) / count)
    else:
        total_pages = round(len(dishes_names) / count) + 1
    dishes = dishes_names[count * (pagenum - 1):count * pagenum]

    if name == "vegetarian" or name == "non-vegetarian":
        diet = diet[count * (pagenum - 1):count * pagenum]
    else:
        diet = ["all_diet"] * count
    final_dishes = dict(zip(dishes, diet))
    print(final_dishes)
    return render_template("home.html",
                           dishes=final_dishes,
                           current_diet=name,
                           total_pages=total_pages,
                           current_page=pagenum,
                           page_type="diet")


@app.route("/page/<int:pagenum>")
def page(pagenum):
    count = 21
    dishes_names, diet_of_dishes = utils.getDishNames()
    if (len(dishes_names) % count) == 0:
        total_pages = (len(dishes_names) / count)
    else:
        total_pages = round(len(dishes_names) / count) + 1
    dishes = dishes_names[count * (pagenum - 1):count * pagenum]
    diet = ["all_diet"] * count
    final_dishes = dict(zip(dishes, diet))
    return render_template("home.html",
                           dishes=final_dishes,
                           total_pages=total_pages,
                           current_page=pagenum,
                           page_type="main")


@app.route("/recipe", defaults={"name": "all"})
@app.route("/recipe/<name>")
def recipe(name):
    if name == "all":
        return redirect("/")
    name = name.lower()
    all_dishes = dishes
    if name in all_dishes:
        recommended_dishes = utils.getRecommendation(name)
        recipe_id = utils.getRecipe(name)

        return render_template(
            "recipe.html",
            current_dish=name,
            recommended_dishes=recommended_dishes,
            recipe_id=recipe_id,
        )

    return render_template("recipe.html")


if __name__ == "__main__":
    app.run(debug=True)