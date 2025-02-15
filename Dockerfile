# Use an official Python runtime
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 9000
EXPOSE 9000

# Run the app
CMD ["python", "app.py"]
