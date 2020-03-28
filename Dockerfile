FROM python
WORKDIR /src
COPY *.py ./
ENTRYPOINT ["python", "main.py"]
