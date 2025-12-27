FROM python:3.13
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY static ./static
COPY templates ./templates
COPY config ./config
EXPOSE 8080

CMD ["fastapi", "run", "src/main.py"]
