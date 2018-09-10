import requests
url_0 = "https://jira-uat.us.oracle.com/jira"
url = "https://jira-uat.us.oracle.com/jira"
data = {"username": "sainath.gorige@oracle.com", "password": "*****"}

s = requests.session()
s.get(url_0)
r = s.post(url, data)
print(r.text)
