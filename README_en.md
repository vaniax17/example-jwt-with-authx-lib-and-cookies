# 🚀 FastAPI with AuthX for JWT

[Изменить язык на RU](README.md)

✅ Implementation of a FastAPI application using:

- `FastAPI`
- `SQLAlchemy`
- `AuthX` (for working with JWT and Cookies)
- `aiobcrypt`
- `aiosqlite`
- `Pydantic`

---
## VERY IMPORTANT!!!
```bash
Works fine only if you use localhost:8000 as specified in the authx config.
```


`When using localhost:8000/user/remove_my_info, you must have your own frontend that sends csrf_access_token to the API`


## ⚙️ How to run

```bash
{WHERE MY REPO}\.venv\Scripts\python.exe {WHERE MY REPO}\src\main.py
```

(replace `{WHERE MY REPO}` with the path to your project)

---

## 📌 5 endpoints implemented

> All work with JWT in **cookies**, with CSRF support

📸 Below are examples of how it works:

---

### 📥 GET endpoints

_Getting information about a JWT token localhost:8000/user/protected_

```json
{
  "success": true,
  "message": "protected endpoint",
  "username": "testuser"
}
```

---

### ❌ DELETE endpoints

_Deleting authorised user data localhost:8000/user/remove_my_info (From cookies)_

```json
{
  "success": true,
  "message": "User removed"
}
```

_Logging out a user localhost:8000/user/logout_
```json
{
  "success": true,
  "message": "logout success"
}
```
---

### ✏️ POST endpoints

_Creating a new user / login localhost:8000/user/create_user_

```json
{
  "success": true,
  "message": "User added"
}
```



## 🔐 Security

- JWT tokens are stored in **HttpOnly cookies**
- CSRF protection for `POST`, `PUT`, `DELETE`
- Token refresh is implemented via `refresh_token`

---

## 📧 Feedback

If you have any questions, create an issue or write to me at tg: @vaniax17.



---
