FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY /powered/*.py ./powered/
COPY /leditbe/*.py ./leditbe/

COPY *.py .

CMD python main.py


