# 🚀 FastAPI with AuthX for JWT

[Change lang to EN](README_en.md)

✅ Реализация FastAPI-приложения с использованием:

- `FastAPI`
- `SQLAlchemy`
- `AuthX` (для работы с JWT и Cookie)
- `aiobcrypt`
- `aiosqlite`
- `Pydantic`

---
## ОЧЕНЬ ВАЖНО!!!
```bash
Работает нормально только если использовать localhost:8000 так-как так прописано в конфиге от authx
```


`При использовании localhost:8000/user/remove_my_info вы должны иметь свой frontend который отправляет csrf_access_token к api`


## ⚙️ Как запустить

```bash
{WHERE MY REPO}\.venv\Scripts\python.exe {WHERE MY REPO}\src\main.py
```

(замени `{WHERE MY REPO}` на путь к твоему проекту)

---

## 📌 Реализовано 5 эндпоинтов 

> Все работают с JWT в **куках**, с поддержкой CSRF

📸 Ниже примеры работы:

---

### 📥 GET endpoints

_Получение информации по JWT токену localhost:8000/user/protected_

```json
{
  "success": true,
  "message": "protected endpoint",
  "username": "testuser"
}
```

---

### ❌ DELETE endpoints

_Удаление данных авторизованного пользователя localhost:8000/user/remove_my_info (Из кук)_

```json
{
  "success": true,
  "message": "User remoevd",
}
```

_Разлогинивание пользователя localhost:8000/user/logout_
```json
{
  "success": true,
  "message": "logout success"
}
```
---

### ✏️ POST endpoints

_Создание нового пользователя / логин localhost:8000/user/create_user_

```json
{
  "success": true,
  "message": "User added"
}
```



## 🔐 Безопасность

- JWT токены хранятся в **HttpOnly куках**
- Защита от CSRF при `POST`, `PUT`, `DELETE`
- Обновление токенов реализуемо через `refresh_token`

---

## 📧 Обратная связь

Если у тебя есть вопросы — создавай issue или пиши мне tg: @vaniax17.



---
