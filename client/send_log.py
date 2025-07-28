import requests
import json

ENDPOINT = "https://wixtuzdx77.execute-api.ap-northeast-1.amazonaws.com/SaveLogToS3"

log_data = {
    "user": "masaki",
    "action": "login",
    "timestamp": "2025-07-28T13:00:00Z"
}

try:
    response = requests.post(
        ENDPOINT,
        data=json.dumps(log_data),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        print("✅ Log sent successfully")
        print("Response:", response.json())
    else:
        print("❌ Failed to send log")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

except Exception as e:
    print("❌ Exception occurred:", str(e))

