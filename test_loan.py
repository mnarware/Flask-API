import pytest
from loan import app
from hello import app

@pytest.fixture
def client():
    return app.test_client()
def test_home(client):
    res=client.get('/') # send a get request
    assert res.status_code == 200
    assert res.text == "<h1>Hey this is get request</h1>"

def test_predict(client):
    data={
        "ApplicantIncome": 100000,
        "CreditHistory": 1,
        "Gender": "Male",
        "LoanAmount": 1200,
        "Married": "No"
        }
    res=client.post('/predict',json=data)
    assert res.status_code ==200
    assert res.json == {"Loan Status":'Rejected'}

