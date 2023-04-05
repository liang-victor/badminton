FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the Pipenv files to the container
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pip install pipenv 
RUN pipenv install --system

# Copy the Django project to the container
COPY . .

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]