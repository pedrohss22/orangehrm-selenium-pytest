# OrangeHRM Selenium Pytest Automation Framework

This project is an automation framework for testing the login functionality of the OrangeHRM demo site using Selenium and the Pytest framework. The framework follows the Page Object Model (POM) design pattern for better organization and maintainability of the test code.

## Project Structure

```
orangehrm-selenium-pytest
├── src
│   ├── pages
│   │   ├── login_page.py       # Contains the LoginPage class for page interactions
│   │   └── locators.py         # Defines locators for the login page elements
│   └── tests
│       └── test_login.py       # Test cases for login functionality
├── conftest.py                 # Pytest fixture for browser initialization and teardown
├── requirements.txt            # Project dependencies
├── pytest.ini                  # Pytest configuration settings
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd orangehrm-selenium-pytest
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the tests:**
   You can execute the test suite using the following command:
   ```
   pytest src/tests/test_login.py --html=report.html
   ```

   This command will run the tests and generate a report in HTML format named `report.html`.

## Test Cases

- **Successful Login Test:**
  - Validates the login functionality using valid credentials (Admin / admin123).

- **Failed Login Test:**
  - Checks for login failure using invalid credentials.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!