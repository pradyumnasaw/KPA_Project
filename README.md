# 📌 KPA API Assignment - Django + MySQL

This project is a backend API developed using **Django REST Framework** and **MySQL** as part of the KPA assignment. It implements two endpoints as defined in the provided Postman collection from Suvidhaen's Swagger documentation.

---
## 🚀 Project Setup Instructions

#### django-admin startproject kpa_project
#### cd kpa_project
#### python -m venv env
#### source env\Scripts\activate
#### pip install django djangorestframework 
#### mysqlclient python-decouple


## 🚀 Features Implemented

| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| POST   | `/kpa-form/`           | Create new KPA form entry    |
| GET    | `/kpa-form/<int:pk>/`  | Retrieve KPA form by ID      |

---

## 🧰 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- MySQL
- Postman
- dotenv (`python-decouple`)

---

## 🧪 Sample Request Format

### 🔹 POST `/kpa-form/`
```json
{
  "name": "Pradyumna",
  "age": 22,
  "phone": "9876543210",
  "email": "pradyumna@example.com"
}


