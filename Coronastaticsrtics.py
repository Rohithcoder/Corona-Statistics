import requests
import json
API_KEY = ("tP5a-29H0s7T")
PROJECT_TOKEN = "tTyUWTsRqPu8"
RUN_TOKEN = "t2F2Zt5ksTU-"
params = {
  "api_key": "{tP5a-29H0s7T}",
  "format": "csv"
}
r = requests.get('https://www.parsehub.com/api/v2/projects/tTyUWTsRqPu8/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(r.text)

class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
                "api_key":self.api_key
                }
            


def get_total_cases(self):
    data = self.data['total']
    
    for content in data:
        if content['name'] == "Coronavirus Cases":
            return content['value']


data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_total_cases())
      
