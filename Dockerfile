FROM python:3.13
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY static ./static
COPY templates ./templates
EXPOSE 8080

RUN useradd app
USER app


CMD ["fastapi", "run", "src/main.py"]
