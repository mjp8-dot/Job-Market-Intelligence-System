import api


app_key = "c06e0bd34326d21f2774a24793bf2c22"
app_id = "7bce7adc"
page = 1
url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}?app_id={app_id}&app_key={app_key}"

# per page 20 jobs 

fetcher = api.API(app_key, app_id, url)

fetcher.get_jobs(20, "jobs.json")