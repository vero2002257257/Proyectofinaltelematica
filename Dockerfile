FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install dash
RUN pip3 install pandas
COPY app.py /
EXPOSE 80
