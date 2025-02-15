from flask import Flask,render_template,request, redirect
from mbta_helper import find_stop_near
app = Flask(__name__)
 
@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        user = request.form["location_name"]
        return render_template('data.html', value = user, nearest_stop = find_stop_near(user))
    else:
        return render_template('website.html')
 
if __name__ == '__main__':
    app.run()
