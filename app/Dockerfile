FROM python:3.7
COPY . /app
RUN pip3 install -r /app/requirements.txt
RUN pip3 freeze
CMD python app/app.py
