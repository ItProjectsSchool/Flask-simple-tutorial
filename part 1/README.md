# Flask tutorial. Part 1. First simple Flask app. Quick example. <br>
In this article, we are going to start building a simple web app using Flask. <br>
If you want to know more about Flask, please, visit this link (https://flask.palletsprojects.com/en/1.1.x/)<br>

First of all, we will start with a basic "Hello World" app on your local development environment.<br>
<b>Step 1. Install Flask.</b> <br>
Open windows terminal or similar tools for Linux or Mac.<br>
Go to a folder with your project via cd command (if the folder isn't created, please create it). After that install Flask using pip.<br>
pip install Flask (if it is necessary you can add a version to the Flask -  pip install Flask==1.1.1)<br>
<b>Step 2. app.py</b><br>
Create app.py file and put it to your project folder. Then add the code below to the app.py file.<br>
```python
#in this part is created Flask object for future work<br>
from flask import Flask
app = Flask(__name__)

#In this part URLs are specified<br>
@app.route('/')
def start():
    return "Hello World!"

#This part is used to launch out app
if __name__ == '__main__':
    app.run()
```
<br>
<b>Step 3. Run app.</b|><br>
Type python app.py in the terminal. And after that, you should see your simple app on  http://localhost:5000/.<br>
That all for part 1:)<br>






