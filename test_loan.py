import pytest
from loan import app

@pytest.fixture
def client():
    return app.test_client()
def test_home(client):
    res=client.get('/') # send a get request
    assert res.status_code == 200
    assert res.text == "<h1>Hey this is get request</h1>"

def test_predict(client):
    data={
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 10000,
        "LoanAmount": 1200,
        "CreditHistory": 1
        }
    res=client.post('/predict',json=data)
    assert res.status_code ==200
    assert res.json == {"Loan Status":'Rejected'}

