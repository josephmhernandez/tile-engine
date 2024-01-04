FROM python:3.9

WORKDIR /app

COPY ./* . 

COPY src ./src

RUN python3 -m pip install --upgrade pip 

RUN python3 -m pip install --no-cache-dir -r requirements.txt 

# ENV REQUEST_ID='req_eb267789-a25d-47f7-bb7d-b326c96291ab'
# ENV ENV='dev'
ENTRYPOINT ["python", "main.py"] 
