**Error & solution log encountered and resolved respectively in this project** 
---

```markdown
# 🧰 Stage 0 — Error & Solution Log  
**Project:** Dynamic Profile Endpoint (HNG13 Backend Track)  
**Stack:** Python (Flask + Gunicorn)  
**Hosting:** Railway.app  

This section documents the common errors I faced during the setup, development, and deployment of my `/me` endpoint — and how I resolved each of them.  
It serves as a reference for my future projects and for anyone encountering similar issues.  

---

## ⚙️ Overview  
- **Endpoint:** `/me`  
- **Purpose:** Return dynamic JSON containing profile data, current timestamp, and a live cat fact from an external API.  
- **Files involved:** `app.py`, `Procfile`, `requirements.txt`, `README.md`  

---

## 🧩 1. Error — *“No repositories found” on Railway*  
**Cause:** Railway didn’t have permission to access my GitHub repositories.  
**Solution:**  
- Granted repository access under **GitHub → Settings → Applications → Authorized OAuth Apps → Railway**.  
- Reconnected Railway to GitHub.  
✅ Railway successfully fetched my repositories.

---

## 🧩 2. Error — *“Railway CLI not installed / Revoke access”*  
**Cause:** Old or incomplete GitHub–Railway connection.  
**Solution:** Revoked old access, reconnected Railway, and authorized the correct GitHub account.  
✅ Fixed by reconnecting the integration.

---

## 🧩 3. Error — *YAML syntax error in Procfile*  
**Error Message:**  
```

✖ Error reading Procfile as YAML: mapping values are not allowed in this context

````
**Cause:** Wrong format in `Procfile`.  
**Fix:**  
❌ Incorrect  
```yaml
web:
  gunicorn app:app
````

✅ Correct

```
web: gunicorn app:app
```

**Lesson:** `Procfile` must be a single line — no YAML indentation or colons.

---

## 🧩 4. Error — *“No matching distribution found for nginx”*

**Cause:** Added `nginx` in `requirements.txt`, which is not a Python package.
**Fix:** Removed `nginx`.
✅ Final `requirements.txt`:

```
Flask
gunicorn
requests
```

---

## 🧩 5. Error — *“/bin/bash: gunicorn: command not found”*

**Cause:** Gunicorn not installed because it wasn’t in `requirements.txt`.
**Fix:** Added `gunicorn` and redeployed.
✅ Application started successfully.

---

## 🧩 6. Error — *App deployed but URL showed “Not Found”*

**Cause:** I visited the base URL (`/`) instead of the defined route `/me`.
**Fix:** Accessed `https://yourappname.up.railway.app/me`.
✅ JSON response returned successfully.

---

## 🧩 7. Error — *App not binding to correct port*

**Log:**

```
Listening at: http://0.0.0.0:8080 (1)
```

**Cause:** Flask didn’t use the deployment port assigned by Railway.
**Fix:** Added this block to `app.py`:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
```

✅ App now listens correctly on Railway’s assigned port.

---

## 🧩 8. Error — *“Everything up to date” but GitHub didn’t show new code*

**Cause:** Forgot to stage files before committing.
**Fix:**

```bash
git add .
git commit -m "Updated code"
git push origin main
```

✅ Changes appeared on GitHub.

---

## 🧩 9. Error — *GitHub Authentication (Access Token Failure)*

**Cause:** GitHub no longer accepts passwords for HTTPS authentication.
**Fix:**

1. Created a **Personal Access Token (PAT)** under GitHub → Developer Settings → Tokens (Classic).
2. Set it as remote authentication:

   ```bash
   git remote set-url origin https://<YOUR_TOKEN>@github.com/<username>/<repo>.git
   ```
3. Re-pushed successfully.
   ✅ GitHub accepted authentication.

**Lesson:** Always use Personal Access Tokens (PAT) instead of passwords.

---

## 🧩 10. Error — *“Updates were rejected because the remote contains work you do not have locally”*

**Cause:** I had edited files directly on GitHub (README.md) while also modifying local files.
**Fix:**

1. Pulled latest remote changes:

   ```bash
   git pull origin main
   ```
2. Merged conflicts and committed again:

   ```bash
   git add .
   git commit -m "Merged remote changes"
   git push origin main
   ```

✅ Push succeeded after merge.

---

## 🧩 11. Final Working Endpoint

Once fixed, the `/me` endpoint returned a live JSON like this:

```json
{
  "status": "success",
  "user": {
    "email": "darethomas96@gmail.com",
    "name": "Osakinle Oluwadare Thomas",
    "stack": "Python / Flask"
  },
  "timestamp": "2025-10-17T15:43:32.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```

✅ Deployment confirmed working successfully.

---

## 🧾 **Key Takeaways**

| Error               | Cause                     | Solution                       |
| ------------------- | ------------------------- | ------------------------------ |
| Procfile YAML error | Wrong formatting          | Use `web: gunicorn app:app`    |
| Missing Gunicorn    | Not in `requirements.txt` | Add `gunicorn`                 |
| Nginx error         | Not a Python lib          | Remove from `requirements.txt` |
| “Not Found” page    | Accessed wrong route      | Use `/me`                      |
| Wrong port          | No env port handling      | Use `os.environ.get("PORT")`   |
| Git push rejected   | Remote ahead of local     | Run `git pull` first           |
| Login failed        | Password blocked          | Use Personal Access Token      |

---

### 💡 Lessons Learned

* Check Railway logs — they’re your best debugging tool.
* Keep `Procfile` clean and minimal.
* Always pull before pushing new commits.
* Use environment variables to handle deployment ports.
* Don’t add non-Python software to `requirements.txt`.
* Each error is a learning milestone — document them all!

---

📘 **Author:** *Osakinle Oluwadare Thomas (Dare)*
⚖️ Lawyer | Backend Developer (Flask/Python) | #HNG13 Cohort
🚀 Building at the intersection of Law & Technology.

```

---


