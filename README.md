# CIE & Attendance Scraper

This project automates the extraction of CIE marks and attendance data from the [KLE Tech Parents Portal](https://parents.kletech.ac.in/) using Selenium and Python.


## Features

- Logs into the portal using your USN and date of birth.
- Scrapes CIE marks and attendance for all subjects.
- Displays the data in a formatted table using `tabulate`.


## Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (download and place the path in the script if needed)
- Install Python dependencies:
  ```sh
  pip install selenium tabulate
  ```
- **Note:** This script is currently written for Unix-based systems (Linux/macOS). For Windows, you may need to adjust the ChromeDriver path (e.g., `Service('C:/path/to/chromedriver.exe')`).


## Setup & Usage

1. **Clone this repository** and navigate to the project folder:
    ```sh
    git clone https://github.com/a9irudhh/cie-scraper.git
    cd cie-scraper
    ```


2. **Edit your credentials in the script:**

    Open `src/script.py` in your editor.  
    Find the following lines and replace the placeholders with your actual details:

    ```python
    driver.find_element(By.ID, "username").send_keys("ENTER_YOUR_USN")
    Select(driver.find_element(By.CLASS_NAME, "inputselectday")).select_by_visible_text("ENTER_DAY")
    Select(driver.find_element(By.CLASS_NAME, "inputselectmon")).select_by_visible_text("ENTER_MONTH")
    Select(driver.find_element(By.CLASS_NAME, "inputselectyear")).select_by_visible_text("ENTER_YEAR")
    ```

    - Replace `"USN"` with your University Seat Number (e.g., `"01FE20BCS069"`).
    - Replace `"dd"` with your birth day (e.g., `"14"`).
    - Replace `"mm"` with your birth month (e.g., `"Feb"`).
    - Replace `"yyyy"` with your birth year (e.g., `"2000"`).

    **Example:**
    ```python
    driver.find_element(By.ID, "username").send_keys("01FE20BCS069")
    Select(driver.find_element(By.CLASS_NAME, "inputselectday")).select_by_visible_text("14")
    Select(driver.find_element(By.CLASS_NAME, "inputselectmon")).select_by_visible_text("Feb")
    Select(driver.find_element(By.CLASS_NAME, "inputselectyear")).select_by_visible_text("2000")
    ```


3. **Run the script:**
    ```sh
    python src/script.py
    ```

    The script will open a browser, log in, fetch your CIE and attendance data, and print a table like:

    ```
    +----------------------+------------+---------------+
    | Subject              | CIE Marks  | Attendance %  |
    +----------------------+------------+---------------+
    | Mathematics          | 45         | 92%           |
    | Computer Networks    | 38         | 88%           |
    | Data Structures      | 50         | 95%           |
    | Operating Systems    | 42         | 90%           |
    | ...                  | ...        | ...           |
    +----------------------+------------+---------------+
    ```

## Notes

- Make sure the ChromeDriver version matches your installed Chrome browser version.
- If you get a `chromedriver` error, download the correct version from [here](https://chromedriver.chromium.org/downloads) and update the path in the script:
    ```python
    service = Service('/path/to/chromedriver')
    ```
- **This script is Unix-specific by default.** For Windows, update the ChromeDriver path as needed.


## License

This project is licensed under the MIT License.

## Credits

- Developed by [Anirudh Hanchinamani](https://github.com/a9irudhh) and  [Pavan H Bhakta](https://github.com/bPavan16)
- Inspired by the need to automate academic data retrieval for KLE Tech students
- Uses [Selenium](https://selenium.dev/) and [tabulate](https://pypi.org/project/tabulate/) for web scraping and data formatting
