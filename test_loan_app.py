from loan_status import app
import json
import pytest

# making something that mimics the server for testing
@pytest.fixture
def client():
    return app.test_client()

def test_pinger(client):
    resp = client.get("/ping")
    assert resp.json == {'message':'Hi, I am pinging'}

def test_home(client):
    resp  = client.get("/")
    assert resp.json == {'message':'Hi, Welcome to Loan Status Classification Model!'}

def test_prediction(client):

    resp = client.post("/predict", json={    
    "Gender": "Male",
    "Married": "No",
    "ApplicantIncome": 5000000,
    "LoanAmount": 500000,
    "Credit_History": 4.0})
    assert resp.json == {"Loan_approval_status": 0}
    assert resp.status_code == 200