from flask import Flask,render_template,Response
import os


app=Flask(__name__)
t = os.listdir("model/")
print(t)


@app.route('/')
def index():
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)

