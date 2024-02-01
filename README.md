# Deeplogic_Tech-Assignment
A simple Flask web application that scrapes and retrieves the top 6 latest stories from https://time.com. This application uses web scraping techniques to extract the latest stories' titles and links without using any internal or external libraries/packages.

## How it Works
* The Flask application includes an endpoint /getTimeStories that accepts an optional query parameter no_of_stories to specify the number of latest stories to retrieve (default is 6). <br>
* The application then sends a request to https://time.com, scrapes the HTML for the latest stories, and returns a JSON response containing the titles and links of the requested number of stories.

### Setup

Clone the Repository
```
git clone https://github.com/Tarunvetsa/Deeplogic_Tech-Assignment
```

Create Virtual Environment and activate it. 
```
virtualenv env
source env/bin/activate (For mac/Linux)
venv\Scripts\activate (For Windows)
```
Install the requirements of the project.
```
pip install -r requirements.txt
```

### Run the Flask Application

```
python deep.py
```

### Accessing Latest Stories
* Retrieve the latest stories from https://time.com by making a GET request to the /getTimeStories endpoint of this Flask application.<br>
By accessing URL `http://<localhost>:<portnumber>/getTimeStories` we get top 6 latest stories as default.

* Optionally, you can specify the number of stories to retrieve by appending `?no_of_stories=<number>` to the URL.<br>
To get the top 3 latest stories, access the following URL:
`http://<localhost>:<portnumber>/getTimeStories?no_of_stories=3`
