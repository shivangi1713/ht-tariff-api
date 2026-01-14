# HT Tariff API

A Django REST API for **High Tension (HT) tariff categorization and consumer drill-down**.  
The project reads data from an existing PostgreSQL database and provides
tariff-wise summaries and consumer-level drill-down APIs.

---

## 📌 Features

- PostgreSQL-backed Django REST API
- Tariff-wise aggregation (summary view)
- Consumer-level drill-down
- Hierarchical tariff filtering
- Filter support by year, month, division, subdivision
- Tested using VS Code (Postman)

---

## 🛠 Tech Stack

- Python 3.12
- Django 6.x
- Django REST Framework
- PostgreSQL
- VS Code

---

## 📂 Project Structure

<img width="221" height="789" alt="image" src="https://github.com/user-attachments/assets/59040490-1190-4656-9d52-07f9d607d3ca" />

---

## ⚙️ Setup Instructions
 1. Create virtual environment.
**python -m venv venv**
2. Activate:
Windows:
**venv\Scripts\activate**
Linux / macOS:
**source venv/bin/activate**
3. Install dependencies
**pip install django djangorestframework psycopg2-binary python-dotenv**

4. Configure environment variables
Create a .env file in project root:

**DB_NAME=HT_DATA_PGVCL**
**DB_USER=postgres**
**DB_PASSWORD=your_password**
**DB_HOST=localhost**
**DB_PORT=5432**

5. Run database migrations
**python manage.py migrate**

Note: The main data table (ht_data) already exists in PostgreSQL and is
mapped using managed = False.

6. Start the server
**python manage.py runserver**

Server will run at:

**http://127.0.0.1:8000/**

