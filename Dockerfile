FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend

WORKDIR /app/backend

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]