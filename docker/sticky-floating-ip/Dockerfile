FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
ADD src/ /app
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD [ "python", "/app/sticky-floating-ip.py" ]
