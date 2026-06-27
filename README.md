# Rivyou Product Search Platform - Backend Assignment

## Overview

This project is a Django REST Framework backend developed as part of the **Backend Developer Intern Assignment** for **Rivyou**.

The application provides secure JWT-based authentication and a product search platform with relevance-based search functionality.

---

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* JWT Logout (Token Blacklisting)
* Password Hashing
* Protected API Endpoints

### Product APIs

* Get Product by ID
* Get Products by Category
* Product Search API
* Case-insensitive Search
* Category-based Relevance Ranking (Tier 1)

---

## Tech Stack

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* drf-yasg (Swagger API Documentation)

---

## Project Structure

```
rivyou_backend/
│
├── backend/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── analytics/
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd rivyou_backend
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows

```bash
env\Scripts\activate
```

Linux/macOS

```bash
source env/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=rivyou_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run the Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

### Authentication

| Method | Endpoint              | Description   |
| ------ | --------------------- | ------------- |
| POST   | `/api/auth/register/` | Register User |
| POST   | `/api/auth/login/`    | Login User    |
| POST   | `/api/auth/logout/`   | Logout User   |

---

### Products

| Method | Endpoint                             | Description              |
| ------ | ------------------------------------ | ------------------------ |
| GET    | `/api/products/<id>/`                | Get Product by ID        |
| GET    | `/api/products/category/<category>/` | Get Products by Category |
| GET    | `/api/products/search/?q=smartphone` | Search Products          |

---

## Authentication

Include the JWT access token in the request header.

```
Authorization: Bearer <access_token>
```

---

## Search Ranking

Current implementation supports:

### Tier 1

* Category Match
* Case-insensitive matching
* Relevance Score
* Rank Reason

Example:

```
GET /api/products/search/?q=smartphone
```

Products belonging to the **Smartphones** category are returned with the highest priority.

---

## Sample Response

```json
{
    "query": "smartphone",
    "total_results": 330,
    "results": [
        {
            "id": 1,
            "product_name": "iPhone 15 Pro",
            "category": "Smartphones",
            "relevance_score": 0.95,
            "rank_reason": "Category match"
        }
    ]
}
```
---

## Author

**Ajin**

Backend Developer | Python | Django | PostgreSQL

---

## Assignment

Backend Developer Intern Assignment

Rivyou Product Search Platform
