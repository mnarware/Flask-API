from flask import Flask,request,render_template,redirect,url_for
import pickle
import pandas as pd

app=Flask(__name__)
with open("classifier.pkl","rb") as f:
    model=pickle.load(f)

@app.route("/",methods=['GET'])
def index():
    return render_template("form.html")


@app.route("/predict",methods=['POST'])
def predict():
    ApplicantIncome = int(request.form.get("ApplicantIncome"))
    LoanAmount = int(request.form.get("LoanAmount"))
    CreditHistry = int(request.form.get("CreditHistry"))
    Gender = request.form.get("Gender")
    Married = request.form.get("Married")

    #loan_req=request.get_json()
    if Gender=="Male":
        Gender=1
    else:
        Gender=0
    
    if  Married=="No":
        Married=0
    else:
        Married=1
    input_data=[ApplicantIncome,CreditHistry,Gender,LoanAmount,Married]
    input_data=
    res=model.predict([input_data])

    print("Prediction :", res[0])
    print("Data :", input_data)
    

    if res==1:
        pred="Approved"
    else:
        pred="Rejected"
    
    submitted = {
        "ApplicantIncome": ApplicantIncome,
        "CreditHistry": CreditHistry,
        "Gender": Gender,
        "LoanAmount": LoanAmount,
        "Married":Married,
        "pred":pred

    }
    return render_template("result.html", data=submitted)
if __name__=="__main__":
    app.run(debug=True)

