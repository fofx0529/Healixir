# <img src="https://raw.githubusercontent.com/mato1321/Healixir/main/drug-frontend/public/favicon.ico" alt="Healixir Logo" width="35" height="35" /> Healixir - ���z���d�O���~���˨t��(�Ī����R)

<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=2E7D32&center=true&vCenter=true&width=600&lines=���z���d�O���~����;�ƾڤ��R���x;�z���M�ݰ��d�U��" alt="Typing SVG" />
  
  <br/>
  
  [![Version](https://img.shields.io/badge/����-1.0.0-blue.svg)](https://github.com/mato1321/healixir)
  [![Node.js](https://img.shields.io/badge/Node.js-?14.0.0-339933.svg?logo=node.js)](https://nodejs.org/)
  [![Python](https://img.shields.io/badge/Python-?3.8-3776AB.svg?logo=python)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-?0.68.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
  [![React](https://img.shields.io/badge/React-18.3.1-61DAFB.svg?logo=react)](https://reactjs.org/)
  
</div>

---

## ? ����

<img align="right" src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pill.png" width="150" alt="Pill">

**Healixir** �O�@�M��X���d�ƾڤ��R���x�P�U�~�P�����d�O���~���˨t�ΡC�z�L���R�z�ӤH�����d���p�B�ͬ��ߺD�P�ӤH�ݨD�A���z���Ѷq���Ȼs�ƪ��O���~��ĳ�C

### ? �A�αڸs

<table>
  <tr>
    <td align="center">?<br/><b>�W�j�K�̤O</b></td>
    <td align="center">?<br/><b>�ﵽ�O�лP�M�`</b></td>
    <td align="center">?<br/><b>�ﵽ��`�ίv</b></td>
    <td align="center">?<br/><b>���ɹB�ʪ�{</b></td>
  </tr>
</table>

---

## ? �D�n�\��

<details open>
<summary><b>? �֤ߥ\��@��</b></summary>

| �\�� | ���� |
|------|------|
| ? **���d�ƾں޲z** | ����O���ðl�ܱz�����d�ƾ� |
| ? **�W�a�t��k����** | ���W�a���t��k�ӭӤH�ƫO���~���� |
| ? **�ӤH�ƫ�ĳ** | �ھڱz�����p���ѱM�~���d��ĳ |
| ? **��ı�Ƥ��R** | ���[���Ϫ�i�ܰ��d�Ͷ� |
| ? **���p�O�@** | �ĥΥ[�K�޳N�O�@�ƾ� |

</details>

---

## ?? �޳N�[�c

<div align="center">
  
```mermaid
graph TD
    A[React �e������] --> B[FastAPI ��ݪA��]
    B --> C[���˺t��k����]
    B --> D[PostgreSQL �ƾڮw]
    B --> E[Redis �w�s�h]
    
    C --> F[�Ī��t���k]
    C --> G[���d���p���R]
    C --> H[�ӤH�Ʊ����޿�]
    
    D --> I[�Τ᰷�d���]
    D --> J[�Ī���Ʈw]
    D --> K[���˾��v�O��]
    
    subgraph "���˨t�ή֤�"
        F
        G  
        H
    end
    
    subgraph "�ƾڦs�x�h"
        I
        J
        K
    end
```

</div>

### ?? �޳N��

**�e�ݧ޳N�G**
- React 18.3.1 + TypeScript
- Vite �c�ؤu��
- Tailwind CSS + shadcn/ui
- Zustand ���A�޲z
- React Query �ƾں޲z

**��ݧ޳N�G**
- FastAPI (Python)
- PostgreSQL �ƾڮw
- Redis �w�s
- JWT ��������

---

## ? �ֳt�}�l

### ? �t�λݨD

- **Node.js** ? 14.0.0
- **Python** ? 3.8
- **npm** ? 6.0.0 �� **yarn** ? 1.22.0
- **Git** �̷s����

### ? �w�˨B�J

<details>
<summary><b>? Step 1: Clone �M��</b></summary>

```bash
# �ƻs�M�ר쥻�a
git clone https://github.com/mato1321/healixir.git

# �i�J�M�ץؿ�
cd healixir
```

</details>

<details>
<summary><b>? Step 2: �e�ݳ]�w</b></summary>

```bash
# �i�J�e�ݥؿ�
cd frontend

# �w�˨̿�M��
npm install
# �Ψϥ� yarn
yarn install

# �ƻs�����ܼ��ɮ�
cp .env.example .env

# �Ұʶ}�o���A��
npm run dev
# �Ψϥ� yarn
yarn dev
```

> ? �e�ݪA�ȹw�]�B��� `http://localhost:5173` (Vite �q�{�ݤf)

</details>

<details>
<summary><b>?? Step 3: ��ݳ]�w</b></summary>

#### ? Python FastAPI ���

```bash
# �i�J��ݥؿ�
cd ../backend

# �إߵ�������
python -m venv venv

# �Ұʵ�������
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# �w�˨̿�M��
pip install -r requirements.txt

# �ƻs�����ܼ��ɮ�
cp .env.example .env

# ����ƾڮw�E�� (�p�G������)
# python -m alembic upgrade head

# �ҰʪA�Ⱦ�
uvicorn app.main:app --reload --port 8000
```

> ? ��ݪA�ȹw�]�B��� `http://localhost:8000`

**�ֳt�Ұʫ��O�]����ϥΡ^�G**
```bash
# �Ұʵ�������
venv\Scripts\activate

# �Ұʫ�ݪA��
uvicorn app.main:app --reload --port 8000
```

</details>

---

## ? �ϥΫ��n

### ? �ֳt�W��

<table>
  <tr>
    <td><b>1?? �ҰʪA��</b></td>
    <td>�T�O�e�ݩM��ݪA�ȳ��w���\�Ұ�</td>
  </tr>
  <tr>
    <td><b>2?? �y�X����</b></td>
    <td>�}���s�����e�� <code>http://localhost:5173</code></td>
  </tr>
  <tr>
    <td><b>3?? ���U�n�J</b></td>
    <td>�إ߷s�b���ΨϥάJ���b���n�J</td>
  </tr>
  <tr>
    <td><b>4?? ��g�ݨ�</b></td>
    <td>�����ӤH���d�ƾڰݨ��լd</td>
  </tr>
  <tr>
    <td><b>5?? ��o����</b></td>
    <td>�d�� AI ���˪��O���~�P���R���i</td>
  </tr>
</table>

### ? �`�ζ}�o���O

**�e�ݶ}�o�G**
```bash
cd frontend
npm run dev          # �Ұʶ}�o�A�Ⱦ�
npm run build        # �c�إͲ�����
npm run lint         # �N�X�ˬd
npm run preview      # �w���Ͳ�����
```

**��ݶ}�o�G**
```bash
cd backend
venv\Scripts\activate                    # �Ұʵ������� (Windows)
source venv/bin/activate                 # �Ұʵ������� (macOS/Linux)
uvicorn app.main:app --reload --port 8000  # �Ұʶ}�o�A�Ⱦ�
```

---

## ? ���ҳ]�w

### ? �����ܼưt�m

�Цb `.env` �ɮפ��[�J�H�U�]�w�G

**�e�� (.env)�G**
```env
# API ��¦ URL
VITE_API_BASE_URL=http://localhost:8000

# ���ε{����T
VITE_APP_NAME=�Ī����˨t��
VITE_APP_VERSION=1.0.0

# �}�o�Ҧ��]�w
VITE_DEV_MODE=true
```

**��� (.env)�G**
```env
# === �A�Ⱦ��]�w ===
NODE_ENV=development
PORT=8000

# === �ƾڮw�]�w ===
DATABASE_URL=postgresql://user:password@localhost:5432/healixir
REDIS_URL=redis://localhost:6379

# === �w���]�w ===
JWT_SECRET=your-super-secret-jwt-key
ENCRYPTION_KEY=your-encryption-key

# === AI API �]�w ===
AI_API_KEY=your-ai-api-key
AI_API_URL=https://api.example.com/v1
AI_MODEL=gpt-4

# === �ĤT��A�� ===
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
```

---

## ? �M�׵��c

```
Healixir/
�u�w�w ? drug-frontend/
�x   �u�w�w ? node_modules/
�x   �u�w�w ? public/
�x   �u�w�w ? src/
�x   �x   �u�w�w ? assets/
�x   �x   �u�w�w ? components/
�x   �x   �u�w�w ? hooks/
�x   �x   �u�w�w ? lib/
�x   �x   �u�w�w ? pages/
�x   �x   �u�w�w ? services/
�x   �x   �u�w�w ? stores/
�x   �x   �u�w�w ? styles/
�x   �x   �u�w�w ? types/
�x   �x   �u�w�w ? utils/
�x   �x   �u�w�w ? App.css
�x   �x   �u�w�w ? App.tsx
�x   �x   �u�w�w ? index.css
�x   �x   �u�w�w ? main.tsx
�x   �x   �|�w�w ? vite-env.d.ts
�x   �u�w�w ? .env
�x   �u�w�w ? .gitignore
�x   �u�w�w ? eslint.config.js
�x   �u�w�w ? index.html
�x   �u�w�w ? package.json
�x   �u�w�w ? package-lock.json
�x   �u�w�w ? postcss.config.js
�x   �u�w�w ? README.md
�x   �u�w�w ? tailwind.config.ts
�x   �u�w�w ? tsconfig.app.json
�x   �u�w�w ? tsconfig.json
�x   �u�w�w ? tsconfig.node.json
�x   �|�w�w ? vite.config.ts
�u�w�w ?? drug-backend/
�x   �u�w�w ? alembic/
�x   �u�w�w ? app/
�x   �u�w�w ? scripts/
�x   �u�w�w ? venv/
�x   �u�w�w ? .env
�x   �u�w�w ? .env.example
�x   �u�w�w ? .gitignore
�x   �u�w�w ? docker-compose.yml
�x   �u�w�w ? Dockerfile
�x   �u�w�w ? README.md
�x   �u�w�w ? requirements.txt
�x   �u�w�w ? requirements-dev.txt
�x   �|�w�w ? test.db
�u�w�w ? docker-compose.yml
�|�w�w ? README.md
```

---

## ? �^�m���n

�ڭ��w��U�اΦ����^�m�I�L�׬O�s�\��B���~�״_�٬O����i�C

<details>
<summary><b>? �p��^�m</b></summary>

1. **Fork** �M�ר�z�� GitHub
2. **Clone** �쥻�a�G`git clone https://github.com/your-username/Healixir.git`
3. **�إ�**�\�����G`git checkout -b feature/your-feature`
4. **����**�ܧ�G`git commit -m 'Add: �s�\��y�z'`
5. **���e**�G`git push origin feature/your-feature`
6. **�}��** Pull Request

</details>

---

## ? �p����T

<div align="center">

| �p���覡 | ��T |
|---------|------|
| ? Email | charleskao811@gmail.com |

</div>

---

## ? �P��

<div align="center">
  
  �S�O�P�©Ҧ��� **Healixir** ���X�^�m���}�o�̩M�ϥΪ̡I
  
  
  ---
  
  <b>Made with ?? by Healixir Team</b>
  
  <br/>
  
  �p�G�o�ӱM�׹�z�����U�A�е��ڭ̤@�� ?�I
  
</div>
