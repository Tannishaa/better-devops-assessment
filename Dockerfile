# --- Build Stage ---
# Use a full Python image to install dependencies
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Final Stage ---
# Use a smaller, more secure base image for the final container
FROM python:3.9-slim

WORKDIR /app
# Copy installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]