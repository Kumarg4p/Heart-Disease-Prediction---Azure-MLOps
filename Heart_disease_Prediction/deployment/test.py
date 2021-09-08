import requests

url = "http://1161e797-86d9-48a9-bc66-e132f190c003.eastus.azurecontainer.io/score"

payload="{\"age\": 40, \"sex\": 1, \"cp\": 2, \"trestbps\": 140, \"chol\": 280, \"fbs\": 1, \"restecg\": 0, \"thalach\": 140, \
          \"exang\": 1, \"oldpeak\": 2.3, \"slope\": 2, \"ca\": 140, \"thal\": 2}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.content)
print(response.text)