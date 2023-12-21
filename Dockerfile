FROM python:3.9

WORKDIR /app

COPY ./* . 

COPY src ./src

RUN python3 -m pip install --upgrade pip 

RUN python3 -m pip install --no-cache-dir -r requirements.txt 

ENTRYPOINT ["python", "main.py"] 
