import requests
import json
import pandas as pd

req_sample = {"age": 45,"sex": 0,"cp": 2,"trestbps": 155,"chol": 258,"fbs": 1,"restecg": 0,"thalach":180,"exang":2, \
              "oldpeak": 2.5,"slope": 1,"ca": 2,"thal": 1}
    
def test_ml_service(scoreurl):
    assert scoreurl != None
    headers = {'Content-Type':'application/json'}
    resp = requests.post(scoreurl, json=json.loads(json.dumps(req_sample)), headers=headers)
    assert resp.status_code == requests.codes["ok"]
    assert resp.text != None
    assert resp.headers.get('content-type') == 'application/json'
    assert int(resp.headers.get('Content-Length')) > 0

def test_prediction(scoreurl):
    assert scoreurl != None
    headers = {'Content-Type':'application/json'}
    resp = requests.post(scoreurl, json=json.loads(json.dumps(req_sample)), headers=headers)
    resp_json = json.loads(resp.text)
    assert resp_json['output']['predicted_target'] == "1"