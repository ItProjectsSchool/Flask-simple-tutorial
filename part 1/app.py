# in this part is created Flask object for future work
from flask import Flask
app = Flask(__name__)

# In this part URLs are specified
@app.route('/')
def start():
    return "Hello World!"

# This part is used to launch out app
if __name__ == '__main__':
    app.run()
