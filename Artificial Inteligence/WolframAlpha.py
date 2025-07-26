import requests

# Replace with your own App ID
app_id = 'GOTCHA-GETYOUR-OWN-APP-ID'
question = input("Question: ")

url = f"http://api.wolframalpha.com/v1/result?appid={app_id}&i={question}"

response = requests.get(url)

if response.status_code == 200:
    print("Answer:", response.text)
else:
    print("Sorry, I couldn't find an answer.")