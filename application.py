from flask import Flask, request, render_template, redirect
from flask_jsglue import JSGlue # used for url_for() working inside javascript which is help us to navigate the url
import utils
import difflib # This module provides classes and functions for comparing sequences.

application = Flask(__name__)


jsglue = JSGlue() # create an object of JsGlue
jsglue.init_app(application) # and assign the app as a init app to the instance of JsGlue

utils.loadArtfacts() # this function loads data,  model_data_frame and model from util


dishes_names, diet_of_dishes = utils.getDishNames()
search_dishes = dishes_names # Used in search bar- for finding keyword which are closer to dishes list
 

# here is home page route
@application.route("/")
def home():
    dishes_names, diet_of_dishes = utils.getDishNames()  

    # pagination logic (28 dishes in one page)
    total_pages = round(len(dishes_names) / 28) + 1
    dishes_names= dishes_names[0: 28]
    diet_of_dishes = ["all_diet"] * 28


    final_dishes = dict(zip(dishes_names, diet_of_dishes))
    # In final_dishes dictionary , dishes_name is key and diet_of_dishes is value


    return render_template("home.html", dishes = final_dishes, total_pages = total_pages, current_page = 1, page_type = "main", nav_active_home = "active", search_dishes = search_dishes)

# here is page route of home page
@application.route("/page/<int:pagenum>")
def page(pagenum):
    dishes_names, diet_of_dishes = utils.getDishNames 

    # pagination logic
    total_pages = round(len(dishes_names) / 28) 
    reminder = len(dishes_names) % 28  
    if reminder != 0:
        total_pages += 1 # if reminder is not 0 then increment total_pages by 1

    dishes_names = dishes_names[28 * (pagenum - 1): 28 * pagenum] 
    diet_of_dishes = ["all_diet"] * len (dishes_names) 

    final_dishes = dict(zip(dishes_names, diet_of_dishes))

    return render_template("home.html", dishes = final_dishes, total_pages = total_pages, current_page = pagenum, page_type = "main" , nav_active_home = "active", search_dishes = search_dishes)


# Route of diet of dishes in home page url
@application.route("/diet", defaults = {"name": "all", "pagenum": 1})
@application.route("/diet/<name>", defaults = {"pagenum": 1})
@application.route("/diet/<name>/<int:pagenum>") 
def diet(name, pagenum):
    dishes_names, diet_of_dishes = utils.getDietWiseDishes(name)  # This function returns dishes name of diet veg or non-veg or both
    # pagination logic
    total_pages = round(len(dishes_names) / 28)
    reminder = len(dishes_names) % 28
    if reminder != 0:
        total_pages += 1

    dishes_names = dishes_names[28 * (pagenum - 1): 28 * pagenum]

    # here if the url request is given for vegetarian or non-vegetarian then it will return this data other wise it will return all dishes data
    if name == "vegetarian" or name == "non-vegetarian":
        diet_of_dishes = diet_of_dishes[28 * (pagenum - 1): 28 * pagenum]
    else:
        diet_of_dishes = ["all_diet"] * len(dishes_names)

    final_dishes = dict(zip(dishes_names, diet_of_dishes))

    return render_template("home.html", dishes=final_dishes, current_diet = name, total_pages = total_pages, current_page = pagenum, page_type = "diet", nav_active_home = "active", search_dishes = search_dishes)
    

# Route of state page
@application.route("/state", defaults = {"name": "Gujarat", "diet": "all", "pagenum": 1})
@application.route("/state/<name>", defaults = {"diet": "all","pagenum": 1})
@application.route("/state/<name>/<diet>", defaults = {"pagenum": 1})
@application.route("/state/<name>/<diet>/<int:pagenum>") # here it expect state, name of the state, diet of dish and page num
def state(name, diet, pagenum):
    state = utils.getStateNames() # A function that returns all unique state names from data
    selected_state = name # selected state name by default is Gujarat
    dishes_names, diet_of_dishes = utils.getStateWiseDishes(name, diet) # A function that returns dish names of a particular state and diet 
    # pagination logic
    total_pages = round(len(dishes_names) / 28)
    reminder = len(dishes_names) % 28
    if reminder != 0:
        total_pages+= 1

    dishes_names = dishes_names[28 * (pagenum - 1): 28 * pagenum]

    # here if the url request is given for vegetarian or non-vegetarian then it will return this data other wise it will return all dishes data
    if diet == "vegetarian" or diet == "non-vegetarian":
        diet_of_dishes = diet_of_dishes[28 * (pagenum - 1): 28 * pagenum]
    else:
        diet_of_dishes = ["all_diet"] * len(dishes_names)

    # here i zip two list and make a dictionary of dishes as key and diet of a that dishes as a value
    final_dishes = dict(zip(dishes_names, diet_of_dishes))

    return render_template("state.html", state = state, selected_state = selected_state, dishes = final_dishes, current_diet = diet, total_pages = total_pages, current_page = pagenum, nav_active_state = "active", search_dishes = search_dishes)
   

# Route of region page
@application.route("/region", defaults = {"name": "all regions", "diet": "all", "pagenum": 1})
@application.route("/region/<name>", defaults = {"diet": "all", "pagenum": 1})
@application.route("/region/<name>/<diet>", defaults = {"pagenum": 1})
@application.route("/region/<name>/<diet>/<int:pagenum>") 
def region(name, diet, pagenum):
    selected_region = name 
    dishes_names, diet_of_dishes = utils.getRegionWiseDishes(name, diet) # A function that returns dishes of a particular region and diet.
    # pagination logic
    total_pages = round(len(dishes_names) / 28)
    reminder = len(dishes_names) % 28
    if reminder != 0:
        total_pages += 1

    dishes_names = dishes_names[28 * (pagenum - 1): 28 * pagenum]

    if diet == "vegetarian" or diet == "non-vegetarian":
        diet_of_dishes = diet_of_dishes[28 * (pagenum - 1): 28 * pagenum]
    else:
        diet_of_dishes = ["all_diet"] * len(dishes_names)

    # here i zip two list and make a dictionary of dishes as key and diet of a that dishes as a value
    final_dishes = dict(zip(dishes_names, diet_of_dishes))

    return render_template("region.html", dishes = final_dishes, selected_region = selected_region, current_diet = diet, total_pages = total_pages, current_page = pagenum, nav_active_region = "active", search_dishes = search_dishes)
    
# Route of recipe
@application.route("/recipe", defaults = {"name": "all"})
@application.route("/recipe/<name>") 
def recipe(name):
    if name == "all":
        return redirect("/")
    name = name.lower() 
    all_dishes = dishes_names 
    if name in all_dishes:
        recommended_dishes = utils.getRecommendation(name) # Getting recommendation for that dish
        recipe_id = utils.getRecipe(name)
        return render_template("recipe.html", current_dish = name, recommended_dishes = recommended_dishes, recipe_id = recipe_id, search_dishes = search_dishes)
       
    return render_template("recipe.html") 

# Route of search functionality .
@application.route("/search", methods = ["GET"])
def search():
    if request.method == "GET": # The below code works only if the request is Get.
        search_query = request.args.get("searchquery") # here is a search keyword or dish which will be getting from user side
        search_result = difflib.get_close_matches(search_query.lower(), search_dishes) # here i finding closest match of searchquery in my dishes list or records using difflib module of python
        if len(search_result) > 0: # if i found records in search result then below code work
            return render_template("search.html", dishes = search_result , search_dishes = search_dishes, current_search = search_query)
        else: # other wise it will show no record found message
            return render_template("search.html", dishes = search_result , search_dishes = search_dishes, current_search = search_query, no_record_found = True)
    else: # if i didn't get a GET request then i will redirect it to home page
        return redirect("/")

# here is route of 404 means page not found error
@application.errorhandler(404)
def page_not_found(e):
       return render_template("404.html", search_dishes = search_dishes), 404

if __name__ == "__main__":
    application.run()
    