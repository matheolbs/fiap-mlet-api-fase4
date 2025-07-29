FROM tensorflow/tensorflow:2.15.0

WORKDIR /src

COPY . .


RUN pip install --no-cache-dir --ignore-installed -r requirements.txt

COPY . .

CMD ["python", "run.py"]