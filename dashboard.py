global choice
import exceptions

def display_dashboard():
    print('''
        \n------------------------------
        \nJob Market Intelligence System'
        \n------------------------------
        \n1. Search for jobs
        \n2. View all jobs
        \n3. Exit
        \n------------------------------
        ''')

    choice = input("Enter your choice (1-3): ")
    return choice


def handle_choice(choice):

    match choice:
        case "1":

            while True:

                try: 

                    keyword = input("\nEnter a keyword to search for jobs: ").title()
                    location = input("\nEnter a location to search for jobs: ").title()
                    category = input("\nEnter a category to search for jobs: ").title()

                    if not keyword or not location or not category:
                        raise exceptions.fillAllFields("Please fill in all fields.")

                except exceptions.fillAllFields as e:
                    print(f"Error: {e}")

                else: 
                    return keyword, location, category
                    
        case "3":
            print("Exiting the dashboard...")
            exit()




