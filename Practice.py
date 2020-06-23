from flask import Flask,render_template,request,flash
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
app=Flask(__name__)
app.secret_key="kunu_pintu"
@app.route("/")
def home():
    return render_template("home2.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
  #  data = pd.read_csv("Salary_Data.csv")
  #  x = data.iloc[:, :-1].values
  #  y = data.iloc[:, -1].values
  #  regressor = LinearRegression()
  #  regressor.fit(x, y)
   # with open("lucky.pkl", "wb") as f:
  #      pickle.dump(regressor, f)
    #    pass
    if request.method=="POST":
        year=request.form["year"]
        with open("lucky.pkl","rb") as f:
            regressor=pickle.load(f)

        for i in regressor.predict([[int(year)]]):
            pred=int(i)
        flash(f"You may have a salary of {pred}$", "info")
        return render_template("home2.html")
    else:
        return render_template("home2.html")
if __name__ == "__main__":
    app.run(debug=True)