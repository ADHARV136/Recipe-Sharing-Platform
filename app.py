from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)
recipes = []

@app.route('/home')
def home():
     return  render_template('home.html')
 
@app.route('/manage')
def index():
    return render_template('index.html', recipes=recipes)
 
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        new_recipe = {
            "id": len(recipes) + 1,
            "title": request.form['title'],
            "ingredients": request.form['ingredients'],
            "instructions": request.form['instructions'],
        }
        recipes.append(new_recipe)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')
 
@app.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if request.method == 'POST':
        recipe['title'] = request.form['title']
        recipe['ingredients'] = request.form['ingredients']
        recipe['instructions'] = request.form['instructions']
        return redirect(url_for('index'))
    return render_template('edit_recipe.html', recipe=recipe)
 
@app.route('/delete_recipe/<int:recipe_id>',  methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    global recipes
    recipes = [recipe for recipe in recipes if recipe['id'] != recipe_id]
    return redirect(url_for('index'))
 
if __name__ == '__main__':
    app.run(debug=True)