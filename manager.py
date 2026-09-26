import api
import psql
import dashboard
import time 

app_key = "c06e0bd34326d21f2774a24793bf2c22"
app_id = "7bce7adc"

global result

# per page 20 jobs 

class Manager:

    def __init__(self):
        self.fetcher = api.API()
        self.db = psql.Database()

    def start(self):
        self.db.make_connection()
        self.db.initialize_table()

        if self.db.is_booted() == False:
            print("Booting the Job Market Intelligence System...")
            
            status = False  # false the system is not booted yet, so it will fetch jobs and insert into the database
            self.fetch_jobs()
            print("\nAll jobs have been fetched and inserted into the database successfully!")
            self.handle_dashboard()
            
        else:
            print("Job Market Intelligence System is already booted and ready with fetched jobs!")
            status = True # true the system is already booted, so it will not fetch jobs and insert into the database
            self.handle_dashboard()

    
    def fetch_jobs(self):    
        for i in range (1, 11):  # Fetch jobs from page 1 to 50

            print(f"Fetching jobs from page {i}...")

            url = f"https://api.adzuna.com/v1/api/jobs/in/search/{i}?app_id={app_id}&app_key={app_key}"

            jobs = self.fetcher.get_jobs("jobs.json", url)

            for job in jobs:
                self.db.insert_job(job)

        self.db.create_gin()  # Create a GIN index on the title column

    boot_status = True

    def handle_dashboard(self):
        choice = dashboard.display_dashboard()

        if choice == '1':
            params = dashboard.handle_choice(choice)

            keyword, location, category = params

            print(f"\nSearching for jobs with keyword: {keyword}, location: {location}, category: {category}...")   
            time.sleep(2)  # Simulate a delay for searching

            if keyword and location and category:
                results = self.db.search_database(keyword, location, category)
                self.display_results(results)

        elif choice == '2':
            results = self.db.get_all_jobs()
            time.sleep(2)  # Simulate a delay for fetching all jobs
            self.display_results(results)


    def display_results(self, results):

        print("\n" + "-" * 150)
        print("Search Results")
        print("-" * 150)

        print(
            f"{'#':<4} | "
            f"{'Job Title':<35} | "
            f"{'Company':<35} | "
            f"{'Location':<35} | "
            f"{'Category':<35}"
        )

        print("-" * 150)

        for i, job in enumerate(results, start=1):
            print(
                f"{i:<4} | "
                f"{job[2]:<35} | "
                f"{job[3]:<35} | "
                f"{job[5]:<35} | "
                f"{job[4]:<35} "
            )

        print("-" * 150)