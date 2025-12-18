FROM python:3.10-slim

WORKDIR /app

# Copy everything first
COPY . .

# Then install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
