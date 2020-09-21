# Falcon app with gunicorn

a. Confirm application is being served from development environment:
` gunicorn -b 0.0.0.0:5000 quote:app --reload

b. Confirm in browser:
 <http://localhost:5000/quote>

## Build docker image

<https://docs.docker.com/engine/reference/builder/>

In falcon_app folder:

 ` docker image build -t quote:latest .

## Run container

` docker run -p 8000:8000 de0f25a204c2