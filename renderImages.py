from flask import Flask
from InstagramLib import GetImages
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'




# @app.route('/image')
# def RenderImages():
#
#     inputArray = GetImages.GetImageJson('zuck', 20)
#
#
#     return render_template('imageCatalog.html', Images=inputArray)
#
#






if __name__ == '__main__':
    app.run()

