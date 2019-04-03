FROM reg.qiniu.com/library/python:latest
RUN pip3 install Flask
RUN pip install Flask
WORKDIR /app
COPY ./hello.py /app/
ENTRYPOINT ["python", "/app/hello.py"]
