FROM python:3.12-slim-bookworm

WORKDIR /rlFlow

# ensures .pyc files are not generated
ENV PYTHONDONTWRITEBYTECODE=1

# ensures that python output is sent straight to terminal (e.g. your container log) without being first buffered and that you can see output of your application (e.g. Django logs) in real time.
ENV PYTHONUNBUFFERED=1


COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]

