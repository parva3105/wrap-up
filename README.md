# 🧠 Wrap-Up: AI Windows Assistant

> Turn natural language into safe PowerShell commands — executed **locally** on your own Windows machine.

---

## ✨ Features

- 💬 Type what you want to do → see the actual PowerShell command
- 🛡️ Secure execution with validation checks
- 💻 Commands run **only on your own machine**, not on a server
- ⚡ Built using FastAPI + React + Vite for a smooth dev experience

---

## 🧱 Tech Stack

- 🖥️ Frontend: React + Vite + TypeScript
- ⚙️ Backend: FastAPI (Python)
- 📡 Axios: Frontend-backend communication
- 🪟 PowerShell: Native command execution
- 🔐 Runs locally — no cloud execution involved

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have the following installed:

- 🟢 **Node.js (v18+)** → [Download](https://nodejs.org/)
- 🐍 **Python 3.10+** → [Download](https://www.python.org/downloads/)
- 🪟 **Windows OS with PowerShell**

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/parva3105/wrap-up.git
cd wrap-up
```

---

### 3️⃣ Backend Setup (Python + FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  

pip install -r requirements.txt
uvicorn main:app --reload
```

In another Terminal
```bash
cd backend
ollama run llama3
```

This will start your backend on:  
**http://localhost:8000**

---

### 4️⃣ Frontend Setup (React + Vite)

Open a new terminal window/tab:

```bash
cd frontend
npm install
npm run dev
```

This will start the frontend on:  
**http://localhost:5173**

---

## 🌐 Access the App

Open your browser and go to:  
👉 [http://localhost:5173](http://localhost:5173)

---

## 🧪 Sample Prompts to Try

- `List all running processes`
- `Create a folder named TestFolder on Desktop`
- `Get IP address of this machine`
- `Get all connected Wi-Fi networks`
- `Show PowerShell version`

---

## 📦 Requirements

### `backend/requirements.txt`

Make sure this file includes:

```
fastapi
uvicorn
pydantic
```

Generate with:

```bash
pip intsall -r requirements.txt
```

---

## 🔐 Privacy & Security

- All commands are executed locally
- Nothing is sent to a remote server
- You are fully in control of your data

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

---

## 📬 Contact

Parth Varu  
📧 ps7384@rit.edu
🔗 [GitHub](https://github.com/parva3105)

---

