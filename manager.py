import api

app_key = "c06e0bd34326d21f2774a24793bf2c22"
app_id = "7bce7adc"

# per page 20 jobs 

fetcher = api.API()

for i in range (1, 51):  # Fetch jobs from page 1 to 50

    print(f"Fetching jobs from page {i}...")

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{i}?app_id={app_id}&app_key={app_key}"

    fetcher.get_jobs("jobs.json", url)

    print(f"Fetched jobs from page {i} and saved to jobs.json\n")