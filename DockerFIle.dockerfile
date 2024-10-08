# Use the official Python image
FROM python:3.10.14-slim-bullseye

# Set the working directory
WORKDIR /app

# Install dependencies directly
RUN apt-get update
RUN pip3 install --no-cache-dir quart discord.py

# Copy the application code
COPY . .


# Set an environment variable
ENV DISCORD_TOKEN="your_discord_token_here"
ENV DISCORD_CHANNEL_ID="your_channel_id_here"
ENV PYTHONUNBUFFERED=1

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python3", "#Hey Buddy.py"]
