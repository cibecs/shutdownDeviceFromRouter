import json
import requests

filename = 'credentials.json'
url = "https://192.168.1.1"

def getCredentials (filename):
    with open(filename) as f:
        data = json.load(f)

    if "username" in data and "password" in data:
        return data["username"], data["password"]
    else:
        raise Exception("Invalid credentials file")

def getCsrfToken(url):
    headers = {
        "Host": "192.168.1.1",
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers, verify=False, allow_redirects=True)
    print("Status Code:", response.status_code)
    print("Response Content:", response.text)
    csrfToken = response.cookies.get("csrftoken", None)
    return csrfToken

username, password = getCredentials(filename)
csrfToken = getCsrfToken(url)
print(username, password, csrfToken)
