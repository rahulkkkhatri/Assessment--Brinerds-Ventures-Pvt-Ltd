
FROM python:latest

LABEL Maintainer="docker0rahul"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY processdata.py ./
# Now the structure looks like this '/usr/app/src/test.py'
RUN mkdir -p dataset/
COPY requirements.txt ./
RUN pip install -r requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3", "./processdata.py"]