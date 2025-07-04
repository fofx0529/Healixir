<div align="center">

# <img src="https://raw.githubusercontent.com/mato1321/Healixir/main/frontend/public/favicon.ico" alt="Healixir Logo" width="35" height="35" /> Healixir - Smart Health Recommendation System

</div>

<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=2E7D32&center=true&vCenter=true&width=600&lines=Your+Personal+Health+Advisor;Smart+Supplement+Recommendations" alt="Typing SVG" />
  
  <br/>
  
  [![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/mato1321/Healixir)
  [![Node.js](https://img.shields.io/badge/Node.js-≥14.0.0-339933.svg?logo=node.js)](https://nodejs.org/)
  [![Python](https://img.shields.io/badge/Python-≥3.8-3776AB.svg?logo=python)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-≥0.104.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
  [![React](https://img.shields.io/badge/React-18.3.1-61DAFB.svg?logo=react)](https://reactjs.org/)
  
  <br/>
  
  [中文檔案](README_CN.md)
  
</div>

---

## 📖 Introduction

<img align="right" src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pill.png" width="150" alt="Pill">

**Healixir** is an intelligent health supplement recommendation system that combines health data analytics with personalized recommendation algorithms. By analyzing your personal health status, lifestyle habits, and individual needs, our system provides customized supplement suggestions tailored specifically for you.

### 🎯 Target Audience

<table>
  <tr>
    <td align="center">💪<br/><b>Boost Immunity</b></td>
    <td align="center">🧠<br/><b>Improve Memory & Focus</b></td>
    <td align="center">😴<br/><b>Better Sleep Quality</b></td>
    <td align="center">🏃<br/><b>Enhance Athletic Performance</b></td>
  </tr>
</table>

---

## 🚀 Key Features

<details open>
<summary><b>📋 Core Features Overview</b></summary>

| Feature | Description | Status |
|---------|-------------|--------|
| 👤 **User Management** | Complete user registration, login, and profile management | ✅ Complete |
| 📝 **Profile Editing** | Edit personal information and health data | ✅ Complete |
| 🔐 **Secure Authentication** | JWT-based authentication with encrypted passwords | ✅ Complete |
| 📊 **Health Data Storage** | PostgreSQL database with complete user health records | ✅ Complete |
| 🔒 **Privacy Protection** | Encrypted technology to protect your data | ✅ Complete |
| 🧮 **Recommendation Algorithm** | Personalized supplement recommendations | 🚧 In Development |
| 📈 **Visual Analytics** | Intuitive charts displaying health trends | 🚧 In Development |

</details>

---

## 🏗️ System Architecture

<div align="center">
  
```mermaid
graph TD
    A[React Frontend Application] --> B[FastAPI Backend Service]
    B --> C[JWT Authentication]
    B --> D[PostgreSQL Database]
    
    C --> E[User Registration/Login]
    C --> F[Profile Management]
    
    D --> G[User Health Data]
    D --> H[Authentication Records]
    
    subgraph "Frontend Components"
        A --> A1[Registration Page]
        A --> A2[Login Page]
        A --> A3[Profile Edit Page]
        A --> A4[Dashboard]
    end
    
    subgraph "Backend API Endpoints"
        B --> B1[/auth/register]
        B --> B2[/auth/login]
        B --> B3[/api/user/me]
        B --> B4[/api/user/update]
    end
    
    subgraph "Database Schema"
        G --> G1[Users Table]
        G1 --> G2[id, email, hashed_password]
        G1 --> G3[name, gender, birth_date, phone]
        G1 --> G4[is_active, created_at, updated_at]
    end
```

</div>

### 🛠️ Technology Stack

**Frontend Technologies:**
- React 18.3.1 + TypeScript
- Vite Build Tool
- Tailwind CSS + shadcn/ui Components
- React Router for Navigation
- Axios HTTP Client
- Lucide React Icons

**Backend Technologies:**
- FastAPI (Python) - High-performance API framework
- PostgreSQL - Primary database with complete ACID compliance
- SQLAlchemy - ORM for database operations
- Alembic - Database migration management
- JWT (JSON Web Tokens) - Secure authentication
- bcrypt - Password hashing
- Pydantic - Data validation and serialization

**Security Features:**
- Password encryption using bcrypt
- JWT token-based authentication
- CORS middleware for secure cross-origin requests
- SQL injection protection via SQLAlchemy ORM
- Input validation with Pydantic schemas

---

## 🚀 Quick Start

### 📋 System Requirements

- **Node.js** ≥ 14.0.0
- **Python** ≥ 3.8
- **PostgreSQL** ≥ 12.0
- **npm** ≥ 6.0.0 or **yarn** ≥ 1.22.0
- **Git** Latest version

### 📦 Installation Steps

<details>
<summary><b>📥 Step 1: Clone the Project</b></summary>

```bash
# Clone the project locally
git clone https://github.com/mato1321/Healixir.git

# Enter the project directory
cd Healixir
```

</details>

<details>
<summary><b>🗄️ Step 2: Database Setup</b></summary>

```bash
# Install and start PostgreSQL
# Create database
createdb drug_recommend_db

# Create user (optional)
psql -c "CREATE USER drug_user WITH PASSWORD 'drug123456';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE drug_recommend_db TO drug_user;"
```

</details>

<details>
<summary><b>⚙️ Step 3: Backend Setup</b></summary>

```bash
# Enter the backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-jose passlib bcrypt python-multipart pydantic pydantic-settings

# Set up environment variables
# Create .env file with database configuration
echo "DATABASE_URL=postgresql://drug_user:drug123456@localhost:5432/drug_recommend_db" > .env
echo "SECRET_KEY=your-super-secret-key-change-this-in-production" >> .env
echo "ACCESS_TOKEN_EXPIRE_MINUTES=30" >> .env
echo "ALGORITHM=HS256" >> .env
echo "DEBUG=True" >> .env

# Initialize database (if using Alembic)
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# Start the server
python -m app.main
```

> 🔧 Backend service runs on `http://localhost:8000` by default

</details>

<details>
<summary><b>🎨 Step 4: Frontend Setup</b></summary>

```bash
# Enter the frontend directory
cd ../frontend

# Install dependencies
npm install
# or use yarn
yarn install

# Start the development server
npm run dev
# or use yarn
yarn dev
```

> 🌐 Frontend service runs on `http://localhost:5173` by default (Vite default port)

</details>

---

## 📖 User Guide

### 🎯 Getting Started

<table>
  <tr>
    <td><b>1️⃣ Start Services</b></td>
    <td>Ensure both frontend and backend services are successfully running</td>
  </tr>
  <tr>
    <td><b>2️⃣ Visit Application</b></td>
    <td>Open your browser and go to <code>http://localhost:5173</code></td>
  </tr>
  <tr>
    <td><b>3️⃣ Register Account</b></td>
    <td>Create a new account with your email, password, and personal information</td>
  </tr>
  <tr>
    <td><b>4️⃣ Login</b></td>
    <td>Login with your credentials to access the dashboard</td>
  </tr>
  <tr>
    <td><b>5️⃣ Edit Profile</b></td>
    <td>Update your personal information including name, phone, and birth date</td>
  </tr>
</table>

### 🔄 API Endpoints

**Authentication:**
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user info

**User Management:**
- `GET /api/user/me` - Get user profile
- `PUT /api/user/me` - Update user profile (RESTful)
- `PUT /api/user/update` - Update user profile (frontend compatible)

### 🗄️ Database Schema

```sql
-- Users table structure
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    hashed_password VARCHAR NOT NULL,
    name VARCHAR,
    gender genderenum,  -- ENUM: 'MALE', 'FEMALE', 'OTHER'
    birth_date DATE,
    phone VARCHAR,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔧 Environment Configuration

### 📝 Environment Variables Configuration

**Backend (.env):**
```env
# Database Configuration
DATABASE_URL=postgresql://drug_user:drug123456@localhost:5432/drug_recommend_db

# Security Settings
SECRET_KEY=your-super-secret-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256

# Application Settings
DEBUG=True
PROJECT_NAME=Drug Recommendation API
VERSION=1.0.0

# CORS Settings
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]
```

---

## 📁 Project Structure

```
Healixir/
├── 🎨 frontend/
│   ├── 📁 src/
│   │   ├── 📁 components/        # Reusable UI components
│   │   ├── 📁 pages/            # Application pages
│   │   │   ├── 📄 Register.tsx   # User registration
│   │   │   └── 📁 member/
│   │   │       └── 📄 editProfile.tsx  # Profile editing
│   │   ├── 📁 lib/              # Utility libraries
│   │   └── 📄 App.tsx           # Main application component
│   ├── 📄 package.json
│   └── 📄 vite.config.ts
├── ⚙️ backend/
│   ├── 📁 app/
│   │   ├── 📁 api/              # API route handlers
│   │   │   ├── 📄 auth.py       # Authentication routes
│   │   │   ├── 📄 deps.py       # Dependency injection
│   │   │   └── 📁 v1/
│   │   │       └── 📄 users.py  # User management routes
│   │   ├── 📁 core/             # Core application logic
│   │   │   ├── 📄 config.py     # Configuration settings
│   │   │   ├── 📄 database.py   # Database connection
│   │   │   └── 📄 security.py   # Security utilities
│   │   ├── 📁 crud/             # Database operations
│   │   │   └── 📄 user.py       # User CRUD operations
│   │   ├── 📁 models/           # Database models
│   │   │   └── 📄 user.py       # User model definition
│   │   ├── 📁 schemas/          # Pydantic schemas
│   │   │   └── 📄 user.py       # User data validation
│   │   └── 📄 main.py           # FastAPI application
│   ├── 📁 alembic/              # Database migrations
│   ├── 📄 .env                  # Environment variables
│   └── 📄 requirements.txt      # Python dependencies
└── 📄 README.md
```

---

## 🤝 Contributing Guidelines

We welcome suggestions and feedback!

### 📝 How to Contribute

1. **Fork** the project to your GitHub
2. **Clone** locally: `git clone https://github.com/your-username/Healixir.git`
3. **Create** a feature branch: `git checkout -b feature/your-feature`
4. **Commit** changes: `git commit -m 'Add: new feature description'`
5. **Push**: `git push origin feature/your-feature`
6. **Open** a Pull Request

### 📧 Or Contact Us Directly
For suggestions, please email: charleskao811@gmail.com

---

## 🚧 Development Roadmap

### ✅ Completed Features
- [x] User registration and authentication system
- [x] Secure password hashing with bcrypt
- [x] JWT token-based authentication
- [x] User profile management and editing
- [x] PostgreSQL database integration
- [x] RESTful API endpoints
- [x] Responsive frontend design

### 🚧 In Development
- [ ] Health questionnaire system
- [ ] Supplement recommendation algorithm
- [ ] Health data analytics dashboard
- [ ] Visual charts and reports
- [ ] Admin panel for supplement management

### 🎯 Future Plans
- [ ] Mobile application
- [ ] AI-powered health insights
- [ ] Integration with health devices
- [ ] Multi-language support
- [ ] Advanced reporting features

---

## 📞 Contact Information

<div align="center">

| Contact Method | Information |
|---------------|-------------|
| 📧 Email | charleskao811@gmail.com |
| 🐙 GitHub | [mato1321](https://github.com/mato1321) |

</div>

---

## 💝 Acknowledgments

<div align="center">
  
  Special thanks to all developers and users who have contributed to **Healixir**!
  
  
  ---
  
  <b>Made with ❤️ by Healixir Team</b>
  
  <br/>
  
  If this project helps you, please give us a ⭐!
  
</div>
