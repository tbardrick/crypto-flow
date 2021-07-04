# import our base image
FROM python:latest

# import our python code to launch from image root folder
COPY ["historic.py",  "current.py", "./"]

# command to launch when running the image
CMD ["python", "./historic.py"]

