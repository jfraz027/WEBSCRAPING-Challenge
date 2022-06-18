# WEBSCRAPING-Challenge
# Mission to Mars

The goal of the project is to build a web application that scrapes multiple websites for data related to the Mission to Mars and then displays the information in a single HTML page. The following information outlines steps in the process.

## Key Steps 

The primary tasks include two parts: 

1. Scraping 

2. MongoDB and Flask Application

## Part  1: Scraping

Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb`. 
* Use this file to complete all your scraping and analysis tasks. 
    
## The following information outlines what data to scrape.

### NASA Mars News

* Scrape the [Mars News Site](https://redplanetscience.com/)
* Collect the latest News Title and Paragraph Text. 
* Assign the text to variables that later reference.

```python

# Examples of News Title and News paragraph text:
news_title = "NASA Administrator Statement on Moon to Mars Initiative, FY 2021 Budget"

news_p = "Jim Bridenstine addresses NASA's ambitious plans for the coming years, including Mars Sample Return."
```
![image](https://user-images.githubusercontent.com/99145651/174455016-541abdda-d558-4092-b91e-5de403c03fbf.png)

### JPL Mars Space Images—Featured Image

* Visit the URL for the Featured Space Image site [here](https://spaceimages-mars.com).

* Utilize Splinter to navigate the site and find the image URL for the current Featured Mars Image.
* Assign the URL string to a variable called `featured_image_url`.
*   Find the image URL to the full-sized `.jpg` image.
*   Save a complete URL string for this image.

```python
# Featured Image:
```
![image](https://user-images.githubusercontent.com/99145651/174454475-2df31782-2c7a-40bc-a613-d65ddfa9892e.png)

### Mars Facts

* Visit the [Mars Facts webpage](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

* Use Pandas to convert the data to a HTML table string.

![image](https://user-images.githubusercontent.com/99145651/174455211-08cc3446-bb7a-481a-a0cb-ccf5f9b6e51d.png)


### Mars Hemispheres

* Visit the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.

* Click each of the links to the hemispheres in order to find the image URL to the full-resolution image.

* Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. 
*   Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image URL string and the hemisphere title to a list. 
*   This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```
![image](https://user-images.githubusercontent.com/99145651/174454548-31b235dd-a85b-4541-a900-b5f4c12b753f.png)


- - -

## Part 2: MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

* Start by converting the Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. 
*   This function should  execute all the scraping code and return one Python dictionary containing all the scraped data.

* Next, create a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query the Mongo database and pass the Mars data into an HTML template for displaying the data.

* Create a template HTML file called `index.html` that will take the Mars data dictionary and display all the data in the appropriate HTML elements. 
*   The final product should look similar to:

![final_app_part1.png](Images/final_app.png)

- - -

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use PyMongo for CRUD applications for the database. 
* Overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure HTML template.
