FROM python:3.13

WORKDIR '/app'

COPY requirements.txt .

RUN python -m venv .venv

RUN source .venv/bin/activate

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
