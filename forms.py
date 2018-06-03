from InstagramLib import GetImages
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/a')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():

   if request.method == 'POST':
      result = request.form
      Name = str(result['Name'])
      Number  = result['Number']
      inputArray = GetImages.GetImageJson(Name, Number)

      # inputArray = GetImages.GetImageJson('zuck')


      return render_template('imageCatalog.html', Images=inputArray)
      # return render_template("result.html",result = result)



if __name__ == '__main__':
   app.run(debug = True)