import json


# Function to read the configuration from the JSON file
def read_config(file_path):
    with open(file_path) as f:
        return json.load(f)


# Load the configuration from the JSON file
config = read_config("config.json")

# Get the projects and associated hours from the configuration
projects = config["projects"]

# Define the order of days
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Iterate over the days and select the appropriate project for each day
for day in days_of_week:
    print("Day:", day)
    project_hours = projects[day]
    for project, hours in project_hours.items():
        if hours > 0:
            print("Project:", project)
            print("Hours:", hours)
            # Perform actions with project and hours, such as selecting them in the UI
            # Assume you have functions to perform actions with project and hours

# Continue with the remaining steps of your Selenium script
