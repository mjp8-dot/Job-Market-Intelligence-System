import requests
import json

class API:  # needs api_id, api_key, url to initialize object

    def __init__(self, app_key, app_id, url):
        self.app_id = app_id
        self.app_key = app_key
        self.url = url

    def get_jobs(self, limit, filename):

        count = 0;

        while(count < limit) :

            try:

                response = requests.get(self.url)

                job = {
                    "id" : response["results"]["id"],
                    "title" : response["results"]["title"],
                    "description" : response["results"]["description"],
                    "company" : response["results"]["company"]["display_name"],
                    "location" : response["results"]["location"]["display_name"],
                    "category" : response["results"]["category"]["label"],
                    "contract_type" : response["results"]["contract_type"],
                    "contract_time" : response["results"]["contract_time"],
                    "salary_min" : response["results"]["salary_min"],
                    "salary_max" : response["results"]["salary_max"],
                    "posted_at" : response["results"]["created"],
                    "redirect_url" : response["results"]["redirect_url"]
                }

                with open(filename, "w") as f: 
                    json.dumps(job, f, indent=4)

                count += 1

            except FileNotFoundError as e:
                with open(filename, "w") as f:
                    f.write("[]")  # create an empty list in the file if it doesn't exist

            






    

    

    
    

    
        



