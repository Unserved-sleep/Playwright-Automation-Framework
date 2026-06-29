# Playwright Automation Framework - SauceDemo

## Overview

This project is an end-to-end web automation framework developed using **Playwright, Python, and Pytest**. The framework automates critical user journeys of the SauceDemo e-commerce application while following industry-standard automation practices and design principles.

### Key Features

* Browser Automation
* Page Object Model (POM)
* Pytest Fixtures
* Parameterizations
* Assertions and Validations
* Screenshots
* Video Recording
* Trace Viewer
* HTML Reporting
* Data-Driven Testing
* Scalable and Maintainable Framework Design

---

## Application Under Test

**Website:** https://www.saucedemo.com/

**Test Credentials**

* Username: `standard_user`
* Password: `secret_sauce`

---

## Project Features

### Login Automation

* Launch browser and navigate to the application
* Login using valid credentials
* Verify successful login

### Inventory Validation

* Count available products
* Validate product count

### Cart Validation

* Add products to the cart
* Verify cart badge count
* Verify selected products in the cart

### Checkout Flow

* Complete the checkout process
* Verify checkout completion page

### Reporting and Debugging

* Automatic screenshots
* Video recording of test execution
* Playwright tracing
* HTML reports

---

## Tech Stack

* Python 3.x
* Playwright
* Pytest
* Pytest-HTML
* Pytest-Playwright

---

## Project Structure

```text
Playwright-Automation/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── data/
│   └── users.json
│
├── artifacts/
│   ├── screenshots/
│   ├── videos/
│   └── traces/
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Framework Design

### Page Object Model (POM)

* Separation of locators and test logic
* Improved maintainability
* Better code reusability
* Reduced code duplication

### Fixtures

Reusable fixtures are implemented for:

* Browser setup
* Browser context creation
* Page creation
* Application navigation
* Resource cleanup

---

## Data-Driven Testing

Login scenarios are executed using test data stored in:

```text
data/users.json
```

Supported scenarios:

* Standard User Login
* Locked User Login

---

## Reports Generated

### Generate HTML Report

```bash
pytest -v --html=reports/report.html
```

### View Trace

```bash
playwright show-trace artifacts/traces/trace.zip
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Playwright-Automation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Run a specific test:

```bash
pytest tests/test_login.py
```

Generate HTML report:

```bash
pytest -v --html=reports/report.html
```

---

## Learning Outcomes

This project demonstrates practical experience with:

* Playwright Automation Framework
* Python Testing using Pytest
* Web UI Automation
* Framework Design Patterns
* Test Reporting and Debugging
* Industry-Standard Test Automation Practices
