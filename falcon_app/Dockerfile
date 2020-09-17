# Use the official image as a parent image.
FROM python:3

# Copy the file from your host to your current location.
ADD ./ /app

# Set the working directory.
WORKDIR /app


# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8000

# Run the command inside your image filesystem.
RUN pip install falcon 
RUN pip install gunicorn 
RUN pip install ipython


# Run the specified command within the container.
CMD [ "gunicorn", "quote:app" ]

# Copy the rest of your app's source code from your host to your image filesystem.
# COPY . .


