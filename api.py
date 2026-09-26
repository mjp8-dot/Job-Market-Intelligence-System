import requests
import json

class API:  # needs api_id, api_key, url to initialize object

    def get_jobs(self, filename, url):

        jobs = []

        success = False

        while success == False:

            try:

                response = requests.get(url)

                response = response.json()

                for result in response['results']:

                        job = {
                            "id": result["id"],
                            "title": result["title"],
                            "company": result["company"]["display_name"],
                            "category": result["category"]["label"],
                            "location": result["location"]["display_name"],
                            "description": result["description"],
                            "contract_time": result.get("contract_time", None),
                            "created": result["created"],
                            "salary_min": result["salary_is_predicted"],
                            "redirect_url": result["redirect_url"]
                        }

                        jobs.append(job)

                success = True

                return jobs
                
                

            except FileNotFoundError as e:

                print(f"File {filename} not found, creating {filename}: {e}")

                with open(filename, "w") as f:
                    f.write("[]")  # create an empty list in the file if it doesn't exist



            






    

    

    
    

    
        



