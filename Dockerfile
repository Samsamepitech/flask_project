FROM python:3.10


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --use-pep517 --user


WORKDIR app

COPY . .

EXPOSE 5000



#HEALTHCHECK --interval=10s --timeout=3s  CMD curl -f http://localhost || exit 1

CMD ["python3","-m","flask","run", "--host=0.0.0.0" ]






