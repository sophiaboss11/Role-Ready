# Role-Ready

Monorepo for Role-Ready application.

## Structure

- **frontend/**: Angular application
- **backend/**: FastAPI application

## Getting Started

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
ng serve
```