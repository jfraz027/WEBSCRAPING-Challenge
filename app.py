from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    
    # find one document from our mongo db and return it.
    mars_dict = mongo.db.mars_dict.find_one()
    # pass that listing to render_template
    return render_template('index.html', mars_dict=mars_dict)
 
 # Route that will trigger the scrape function
@app.route('/scrape')
def scrape():
    # Run the scrape function and save the results to a variable
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mars_dict.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)




