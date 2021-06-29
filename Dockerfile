# import our base image
FROM python:latest

# import our python code to launch from image root folder
COPY ["main.py",  "database.py", "infura.py", "./"]

# comman to launch when running the image
CMD ["python", "./main.py"]

