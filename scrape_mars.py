from splinter import Browser
from bs4 import BeautifulSoup 
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

  
def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Create a dict to store 
    mars_dict = {}


    # The Mars News url
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Return all the HTML on our page
    html = browser.html

    #Create BeautifulSoup object and parse
    soup = BeautifulSoup(browser.html, 'html.parser')
    slide_elem = soup.select_one('div.list_text')
    
    #Find the latest news title and remove newline characters
    news_title = slide_elem.find("div", class_='content_title').get_text()

    #Find the latest news paragraph text and remove newline characters
    news_p =slide_elem.find('div',class_='article_teaser_body').get_text()

    #Add to dict
    mars_dict['news_title'] = news_title
    mars_dict['news_p'] = news_p


    # '''JPL Mars Space Images - Featured Image'''

    #JPL Mars images url
    mars_url ='https://spaceimages-mars.com/'
    browser.visit(mars_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #Retrieve
    image = soup.find('img', class_="headerimage fade-in")['src']
    featured_image_url =mars_url+image
    
    
    #Add to dict
    mars_dict['featured_image_url'] = featured_image_url

   
    # '''Mars Facts'''

    #Mars space facts url
    facts_url = 'https://galaxyfacts-mars.com'

    #Use Pandas to scrape the planet profile
    mars_facts_df = pd.read_html(facts_url)[0]
    
    #Set columns
    mars_facts_df.columns = ('Description','Mars','Earth')
   
    #Set index to the 0 column
    mars_facts_df.set_index('Description', inplace =True)

    #Convert to a HTML table string
    mars_facts_tr_html = mars_facts_df.to_html()

    #Clean 
    mars_facts_tr_html = mars_facts_tr_html.replace('\n', '')
        
    #Add to dict
    mars_dict['html_table'] = mars_facts_tr_html

    # '''Mars Hemispheres'''

    #Hemispheres url
    hemi_url ='https://marshemispheres.com/'

    #visit
    browser.visit(hemi_url)

    #create BeautifulSoup object and parse
    soup = BeautifulSoup(browser.html, 'html.parser')

    #get the 4 hemispheres (class of 'item')
    hemispheres = soup.select('div.item')

    #Loop through each hemisphere

    hemisphere_image_urls = []

    for h in hemispheres:
        title = (h.find('h3').text).replace(' Enhanced', '')
          
        #click the hemisphere
        browser.links.find_by_partial_text('Hemisphere').click()

        #make new soup of that page
        soup = BeautifulSoup(browser.html, 'html.parser')

        #find the full image
        full = soup.find('a', text='Sample')

        #get the img url
        img_url = full['href']

        #make a dict and append to the list
        hemispheres = {}
        hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
        hemispheres['title'] = title
        hemisphere_image_urls.append(hemispheres)

        #go back 
        browser.back()

    #close browser
    browser.quit()    

    #add to dict
    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_dict

if __name__=="__main__":
    print(scrape())