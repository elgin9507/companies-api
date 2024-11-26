FROM python:3.11.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DIRPATH=/var/company

WORKDIR $DIRPATH

COPY requirements.txt $DIRPATH

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . $DIRPATH

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
