# Use the official Python runtime image
FROM python:3.13  
 
RUN mkdir /app
 
WORKDIR /app
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
RUN pip install --upgrade pip 
 
#
COPY requirements.txt  /app/
 
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
COPY . /app/
 
EXPOSE 8000
 
CMD ["python", "jobboard/manage.py", "runserver", "0.0.0.0:8000"]