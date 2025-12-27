FROM python:3.13
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY src ./src
EXPOSE 8080

RUN useradd app
USER app

CMD ["fastapi", "run", "main.py"]
