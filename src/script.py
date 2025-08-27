#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tabulate import tabulate 
import re
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://parents.kletech.ac.in/")

driver.find_element(By.ID, "username").send_keys("01FE22BCS264")  # Replace with your USN

Select(driver.find_element(By.CLASS_NAME, "inputselectday")).select_by_visible_text("09")
Select(driver.find_element(By.CLASS_NAME, "inputselectmon")).select_by_visible_text("Feb")
Select(driver.find_element(By.CLASS_NAME, "inputselectyear")).select_by_visible_text("2004")

driver.find_element(By.CLASS_NAME, "cn-login-btn").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cn-cie-stat")))

cie_script = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[6]/div[1]/div/script"))
)
cie_text = cie_script.get_attribute("innerText")
cie_matches = re.findall(r'\["([A-Z0-9]+)",\s*(\d+)\]', cie_text)

tbody = driver.find_element(By.XPATH, "/html/body/div/div/div[8]/div/div/div/table/tbody")
rows = tbody.find_elements(By.TAG_NAME, "tr")
course_names = {}

for row in rows:
    tds = row.find_elements(By.TAG_NAME, "td")
    if len(tds) >= 2:
        code = tds[0].text.strip()
        name = tds[1].text.strip()
        course_names[code] = name

cie_data = {}
for code, mark in cie_matches:
    subject = course_names.get(code, "Unknown")
    cie_data[subject] = int(mark)

attendance_script = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[6]/div[2]/div/script"))
)
attendance_text = attendance_script.get_attribute("innerText")
attendance_matches = re.findall(r'\["([A-Z0-9]+)",\s*(\d+)\]', attendance_text)

attendance_data = {}
for code, percent in attendance_matches:
    subject = course_names.get(code, "Unknown")
    attendance_data[subject] = int(percent)

table = []

all_subjects = set(cie_data.keys()) | set(attendance_data.keys())
for subject in sorted(all_subjects):
    cie = cie_data.get(subject, "-")
    att = attendance_data.get(subject, "-")
    table.append([subject, cie, f"{att}%" if att != "-" else "-"])

print("\nFinal Report Table:\n")
print(tabulate(table, headers=["Subject", "CIE Marks", "Attendance %"], tablefmt="grid"))

driver.quit()
