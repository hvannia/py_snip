# Use the official image as a parent image.
FROM python:3

# Env var 
ENV foo=bar


#The <dest> is an absolute path, or a path relative to WORKDIR, into which the source will be copied inside the destination container.
# Copy the file from your host to your current location.
# COPY [--chown=<user>:<group>] <src>... <dest>
RUN echo 'Copying app files'
COPY ./ /falcon_app

# Set the working directory.
WORKDIR /falcon_app

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8000

RUN echo 'Installing dependencies'
# Run the command inside your image filesystem. shellform
RUN pip install falcon 
RUN pip install gunicorn 
RUN pip install ipython

# Run the specified command within the container.
# RUN ["executable", "param1", "param2"]  add -t 30
# Specify a server socket to bind.
CMD [ "gunicorn", "--bind","0.0.0.0:8000", "app.quote:app" ]


