# 🐍 Mini Backend

> Two JSON endpoints — pure Python, zero dependencies, ~20 lines.

---

## 👤 About

| Field       | Details                          |
|-------------|----------------------------------|
| Author      | Abdullah                         |
| University  | Air University, Kamra            |
| Language    | Python 3 (built-in `http.server`) |
| Port        | `localhost:3000`                 |

---

## 🚀 Run It

```bash
# Step 1 — Clone the repo
git clone https://github.com/YOUR_USERNAME/mini-backend.git
cd mini-backend

# Step 2 — Start the server
python3 server.py

# Step 3 — Stop the server
Ctrl + C
```

---

## 📡 Endpoints

### `GET /hello`

```bash
curl http://localhost:3000/hello
```

```json
{ "message": "Hello, World!" }
```

---

### `GET /about`

```bash
curl http://localhost:3000/about
```

```json
{
  "name": "Mini Backend",
  "author": "Abdullah",
  "university": "Air University"
}
```

---

### Any other route → `404`

```json
{ "error": "Route not found" }
```

---

## 📁 Project Structure

```
mini-backend/
├── app.py     ← main server file
└── README.md     ← documentation
```

---


---

## ⚙️ How It Works

`HTTPServer` listens on port `3000`. Every incoming request hits the `Handler` class — `req.url` tells us which route was hit, we branch on it and write back JSON. That's the entire request → response loop.
