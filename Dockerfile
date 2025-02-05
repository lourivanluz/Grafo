FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY . .

RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
