# The image you are going to inherit your Dockerfile from
FROM python:3.9
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
# Copies from your local machine's current directory to the django_recipe_api folder 
# in the Docker image
COPY . .

# Install the requirements.txt file in Docker image

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver"]