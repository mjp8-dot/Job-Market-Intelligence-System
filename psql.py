from fileinput import filename

import psycopg2

class Database:

        def __init__(self):
            self.conn = None
            self.cur = None

        def is_booted(self):
            try : 
                self.cur.execute("SELECT COUNT(*) FROM jobs_data")
                count = self.cur.fetchone()[0]
                if count > 0:
                    return True
                else:
                    return False
            except psycopg2.ProgrammingError as e:
                print(f"Error checking if database is booted: {e}")
                return False
            except Exception as e:
                print(f"Error checking if database is booted: {e}")
                
                return False

        def make_connection(self):
            try:
                self.conn = psycopg2.connect(
                    host = "127.0.0.1",
                    database = "postgres",
                    user = "preetham",
                    password = "secret"
                    )

                self.cur = self.conn.cursor()

                print("Database connection established successfully!")

                

            except Exception as e:
                print(f"Error connecting to the database: {e}")
                self.conn = None
                self.cur = None
                

        def initialize_table(self):
            self.cur.execute('''
                    CREATE TABLE IF NOT EXISTS jobs_data (
                    id SERIAL PRIMARY KEY,
                    job_id BIGINT UNIQUE,
                    title TEXT,
                    company TEXT,
                    category TEXT,
                    location TEXT,
                    description TEXT,
                    contract_time TEXT,
                    created TIMESTAMP,
                    salary_min NUMERIC,
                    redirect_url TEXT
            )''')

            self.conn.commit()

            print("Table created successfully!")
              

        def insert_job(self, job):

            try: 
                  self.cur.execute('''
                    INSERT INTO jobs_data(
                        job_id, 
                        title,
                        company,
                        category,
                        location,
                        description,
                        contract_time,
                        created,
                        salary_min,
                        redirect_url
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (job["id"],
                          job["title"],
                          job["company"],
                          job["category"],
                          job["location"],
                          job["description"],
                          job["contract_time"],
                          job["created"],
                          job["salary_min"],
                          job["redirect_url"]))
                  
                  self.conn.commit()
                  print(f"Job {job['id']} inserted successfully!")

            except Exception as e:
                print(f"Error inserting job {job['id']}: {e}")
                self.conn.rollback()

        def create_gin(self):
            self.cur.execute('''
                CREATE INDEX IF NOT EXISTS jobs_gin ON jobs_data
                USING gin(to_tsvector('english', title));
                ''')

            print("GIN index created successfully!")

        def search_database(self, keyword, location, category):

            search_results = []

            try:
                self.cur.execute('''
                    SELECT * FROM jobs_data
                    WHERE to_tsvector('english', title) @@ plainto_tsquery('english', %s)
                    AND location ILIKE %s
                    AND category ILIKE %s
                ''', (keyword, f'%{location}%', f'%{category}%'))

                results = self.cur.fetchall()
                for row in results:
                    search_results.append(row)

                return search_results

            except psycopg2.ProgrammingError as e:
                print(f"Error searching database: {e}")
                return []
                    

            except Exception as e:
                print(f"Error searching database: {e}")
                return []

        def get_all_jobs(self):
            all_jobs = []

            try:
                self.cur.execute('''
                    SELECT * from jobs_data;''')

                search_results = self.cur.fetchall()
                for row in search_results:
                    all_jobs.append(row)
                return all_jobs
            
            except psycopg2.ProgrammingError as e:
                print(f"Error retrieving all jobs: {e}")
                return []
                    
            except Exception as e:
                print(f"Error retrieving all jobs: {e}")
                return []