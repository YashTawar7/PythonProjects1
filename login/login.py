from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime, timedelta
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

# Set path to the ChromeDriver executable
chrome_driver_path = "C:/chromedriver.exe"

# Initialize ChromeDriver with options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the window
chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome()

# Open the website
driver.get("https://ehof.login.us2.oraclecloud.com/oam/server/obrareq.cgi?encquery%3DN5rHqTk5Ohg9%2B2NoVV8zR%2FF"
           "%2BLffmS5yLKmxDyIe%2FZ5QpU9zosBfgnFhY%2B91V3KX196b31xMPRkii9XVJwWN%2FHpBuNGrAFz8rPVNA%2FFJ5sJn6ZOXzPZ"
           "%2F4kB2Q9%2BDduUoVT0hzMUu2lP%2BoJiWi91h%2FbdsiLu4cZMZ7419FHTy78"
           "%2BFuKkEiXDX5rboH2DhjJ9Pqu43M7KsYVEmAx29cibe8u2cygRRyei81iSUzV6o2OQA27lEXiZsUKTr2psLDMnXPHiuT13i4emKUHlXM6N4MWQ1zwtIOQG9ySPwxLFQukhhrw%2B4MTBKcQXGYmM7z99ckjAaFhR4wy2QJySa4m7X6OiJf%2BmuxEOCpEnvVufIEomMSPwNb60U7OOt4%2FDVbJn9HZ%2B43Y8HcUKMCtzB6tEPPbPnOADGjuPywHRglVciERDo%3D%20agentid%3DOraFusionApp_11AG%20ver%3D1%20crmethod%3D2%26cksum%3Dc9633f7b3ec5f607d9d070a66e588d3eb421fa10&ECID-Context=1.0064r1Fr34n23VQLqaP5iY0003Oo0001Ho%3BkXjE")

# Find the username input field and enter the username
username_field = driver.find_element(By.ID, "userid")
username_field.send_keys("533904")

# Find the password input field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("PYash@1007")

# Find the login button and click it
login_button = driver.find_element(By.ID, "btnActive")
login_button.click()

# Wait for the login process to complete
time.sleep(5)  # Wait for 5 seconds

# Maximize the window (if not already maximized)
driver.maximize_window()

# Click on the timesheet link
timesheet_link = driver.find_element(By.XPATH, '//*[@id="itemNode_my_information_absences1"]')
timesheet_link.click()

# Wait for the page to load
wait = WebDriverWait(driver, 10)
current = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "partial-container")))
current.click()

# Click on the add button
add_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "svg-bkgd02")))
add_button.click()

# Assume 'project' is a dropdown element
wait = WebDriverWait(driver, 10)
project = wait.until(EC.visibility_of_element_located(
    (By.ID, "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:n1Sis:aN1Srh::btn")))

# Click on the dropdown to reveal the options
project.click()

# Find and click on the desired option
wait = WebDriverWait(driver, 10)
desired_option_project = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:n1Sis:aN1Srh::item1"]')))
desired_option_project.click()

time.sleep(5)

# Assume 'task' is a dropdown element
wait = WebDriverWait(driver, 10)
task = wait.until(EC.visibility_of_element_located(
    (By.ID, "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:n2Sis:aN2Srh::btn")))

# Click on the dropdown to reveal the options
task.click()

# Find and click on the desired option
wait = WebDriverWait(driver, 10)
desired_option_task = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:n2Sis:aN2Srh::item0"]')))
desired_option_task.click()

# Assume 'expenditure_type' is a dropdown element
wait = WebDriverWait(driver, 10)
exp_type = wait.until(EC.visibility_of_element_located(
    (By.ID, "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:a12Sis:aA12Srh::btn")))

# Click on the dropdown to reveal the options
exp_type.click()

# Find and click on the desired option
wait = WebDriverWait(driver, 10)
desired_option_exp_type = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:a12Sis:aA12Srh::item0"]')))
desired_option_exp_type.click()

# Assume 'select date' is a dropdown element
wait = WebDriverWait(driver, 10)
sdate = wait.until(EC.visibility_of_element_located(
    (By.ID, "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:dtItr:0:teMdp:mdp_cil1::icon")))

# Click on the dropdown to reveal the options

sdate.click()


# Function to find the next occurrence of a day of the week
# Function to find the next occurrence of a day of the week
def next_weekday(d, weekday):
    days_until_target = weekday - d.weekday()
    if days_until_target <= 0:  # Target day already happened this week
        days_until_target += 7
    return d + timedelta(days=days_until_target)


# Define the starting day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
start_day_of_week = 0  # Assuming Monday is the starting day of the week

# Get today's date
today = datetime.today()

# Find the next occurrence of the starting day of the week
start_date = next_weekday(today, start_day_of_week)

# Calculate the dates for the current week until Friday
dates = [start_date + timedelta(days=i) for i in range(5)]

# Format the dates as needed (assuming date format like "DD-MM-YYYY")
formatted_dates = [date.strftime("%d-%m-%Y") for date in dates]

calendar = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:dtItr:0:teMdp:mdp_cd1::cg"]/tbody')))

# Get all the date elements for the current week

date_elements = calendar.find_elements(By.XPATH, './tr[5]/td[position() > 1]')
# Initialize a counter to keep track of selected dates
selected_dates = 0

# Iterate over the date elements and click on each date until 5 dates are selected
for date_element in date_elements:
    # Check if the date element is enabled
    if "rw-state-disabled" not in date_element.get_attribute("class"):
        # Click on the date element if it is enabled
        date_element.click()
        selected_dates += 1  # Increment the counter

        # Check if 5 dates have been selected
        if selected_dates == 5:
            break

quantity = driver.find_element(By.ID,
                               "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:dtItr:0:mInp::content")
quantity.send_keys("8")


comments = driver.find_element(By.ID,
                               "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:elcInp::content")
comments.send_keys("Working in ODC")

wait = WebDriverWait(driver, 10)
ok_type = wait.until(EC.visibility_of_element_located(
    (By.ID, "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:tcePce:tcdLv:0:stePse:PSEcb2")))

# Click on the dropdown to reveal the options
ok_type.click()

wait = WebDriverWait(driver, 10)
submit_type = wait.until(EC.visibility_of_element_located(
    (By.ID, "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:teUpl:UPsp1:SPsb2")))

# Click on the dropdown to reveal the options
submit_type.click()

# Sleep to prevent the window from closing immediately
time.sleep(10)
