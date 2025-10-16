# 🐱 Meow Profile API

A simple Django-based API that exposes a `/me` endpoint returning user profile data and a random cat fact.

---

## 🚀 Features
- `/me` endpoint that returns:
  - Developer’s info
  -Timestamp
  - Random cat fact (fetched dynamically from the [Cat Facts API](https://catfact.ninja/fact))
- JSON response with `Content-Type: application/json`
- CORS enabled (allows all origins)

---

## 🧩 Tech Stack
- **Python 3.12+**
- **Django 5+**

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/a-deola/meow-profile.git
cd meow-profile
```


### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python manage.py runserver
```
### The app will start on:

http://127.0.0.1:8000/

---

### 🧪 Test the /me Endpoint
Visit:

http://127.0.0.1:8000/me

 
### Expected response:

```json
{
  "status": "success",
  "user": {
    "email": "my_email@example.com",
    "name": "<first_name last_name>",
   "stack": "Python/Django"
  },
  "timestamp": "2025-10-16T13:37:53.267516Z",
  "fact": "Cats sleep for 70% of their lives."
}
```