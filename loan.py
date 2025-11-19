from flask import Flask,request,render_template,redirect,url_for
import pickle
import pandas as pd

app=Flask(__name__)
with open("classifier.pkl","rb") as f:
    model=pickle.load(f)

@app.route("/",methods=['GET'])
def index():
    #return render_template("form.html")
    return "<h1>Hey this is get request</h1>"

@app.route("/predict",methods=['POST'])
def predict():
    data=request.get_json()
    ApplicantIncome =data['ApplicantIncome']    #int(request.form.get("ApplicantIncome"))
    LoanAmount = data['LoanAmount']             #int(request.form.get("LoanAmount"))
    CreditHistory =data['CreditHistory']          #int(request.form.get("CreditHistry"))
    
    #loan_req=request.get_json()
    if data['Gender']=="Male":
        Gender=0
    else:
        Gender=1
    
    if  data['Married']=="No":
        Married=0
    else:
        Married=1
    input_data=[Gender,Married,ApplicantIncome,LoanAmount,CreditHistory]
    
    res=model.predict([input_data])
    
    print("RAW JSON:", data)
    print("Processed Input:", input_data)
    print("Prediction :", res[0])
    print("Data :", input_data)
    

    if res[0]==1:
        pred="Approved"
    else:
        pred="Rejected"
    
    submitted = {
        "ApplicantIncome": ApplicantIncome,
        "CreditHistry": CreditHistory,
        "Gender": Gender,
        "LoanAmount": LoanAmount,
        "Married":Married,
        "pred":pred

    }
    return {"Loan Status":pred}  #render_template("result.html", data=submitted)
 

