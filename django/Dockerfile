# Use an official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (create it with pip freeze if needed)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . ./app

# Expose port 8000 for Django
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
