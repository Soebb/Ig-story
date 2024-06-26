FROM python:3.10-slim-bookworm
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
COPY . ./
RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install instagrapi Pillow
EXPOSE 5000
CMD ["python3", "main.py"]
