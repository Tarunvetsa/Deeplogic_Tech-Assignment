from flask import Flask, jsonify, request
import requests
import re

app = Flask(__name__)

def latest_stories(num_stories=6):
    url = "https://time.com"
    response = requests.get(url)
    html_text = response.text
    tag = r'<div class="partial latest-stories" data-module_name="Latest Stories">(.*?)</div>'
    match = re.search(tag, html_text, re.DOTALL)
    
    if match:
        div_items=match.group(1)
        story_pattern = r'<li class="latest-stories__item">\s*<a href="([^"]+)">\s*<h3 class="latest-stories__item-headline">(.*?)</h3>\s*</a>'
        stories = re.findall(story_pattern, div_items)[:num_stories]
        stories_json=[]
        for link, title in stories:
            stories_json.append({"title": title.strip(), "link": "https://time.com"+link}) 
        return stories_json
    else:
        return []

@app.route('/getTimeStories')
def get_latest_stories():
    no_of_stories = request.args.get('no_of_stories', type=int)
    result_stories = latest_stories(no_of_stories)
    return jsonify(result_stories)

if __name__ == '__main__':
    app.run(debug=True)

