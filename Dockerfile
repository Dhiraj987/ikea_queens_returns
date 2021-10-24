FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /app .
COPY .env .
CMD [smtpd_tls_auth_only = yes]

ENTRYPOINT ["python", "app.py"]
