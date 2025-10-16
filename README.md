##  Backend Wizards — Stage 0 Task: Dynamic Profile Endpoint

###  Project Overview

This project was built as part of the **HNG13 Backend Track (Stage 0)** challenge.
It is a simple RESTful API built with **Python (Flask)** that returns dynamic user information along with a random cat fact fetched from a third-party API — [Cat Facts API](https://catfact.ninja/fact).

The purpose of this project is to demonstrate backend development skills such as:

* Creating RESTful endpoints
* Fetching and handling external API data
* Formatting dynamic JSON responses
* Deploying APIs to a live hosting platform (Railway)

---

### Live Endpoint

**Base URL:**

```
https://web-production-49b5.up.railway.app
```

**GET /me:**

```
https://web-production-49b5.up.railway.app/me
```

---

###  Example Response

```json
{
  "status": "success",
  "user": {
    "email": "Thomasdreh@gmail.com",
    "name": "Dare Thomas Osakinle",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-16T15:48:02.657Z",
  "fact": "Cats sleep for about 70% of their lives."
}
```



###  Tech Stack

* **Language:** Python
* **Framework:** Flask
* **Web Server:** Gunicorn
* **Hosting:** Railway
* **External API:** [Cat Facts API](https://catfact.ninja/fact)

---

###  Installation & Local Setup

Follow these steps to run the project locally:

```bash
# Clone the repository
https://github.com/Thomas-byt/hng13-backend-task.git
cd https://github.com/Thomas-byt/hng13-backend-task.git

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

# Install dependencies
pip install -r requirements.txt

# Run the Flask app locally
python app.py
```

The app will start running on:

```
http://127.0.0.1:8000/me
```

---

### Deployment

The project is deployed on **Railway.app** using the following setup:

* `Procfile` → `web: gunicorn app:app`
* `runtime.txt` → `python-3.10.13`
* `requirements.txt` includes Flask, Gunicorn, and Requests
* Port handled dynamically via:

  ```python
  port = int(os.environ.get("PORT", 8000))
  app.run(host="0.0.0.0", port=port)
  ```

---

###  Author

**Name:** Osakinle Oluwadare Thomas, Esq
**Email:** [Darethomas96@gmail.com](mailto:Darethomas96@gmail.com)
**Stack:** Python/Flask
**LinkedIn:** [Your LinkedIn Profile](https://linkedin.com/in/)
**GitHub:** [Your GitHub Profile](https://github.com/)



### What I Learned

Through this project, I learned:

* How RESTful APIs communicate and serve JSON data.
* How to integrate external APIs dynamically.
* How to deploy Python Flask apps on a live server (Railway).
* The importance of error handling and dynamic environment configuration.



### Acknowledgements

* [Cat Facts API](https://catfact.ninja/fact) — for providing random cat facts.
* [HNG Internship](https://hng.tech) — for organising this backend learning challenge.


