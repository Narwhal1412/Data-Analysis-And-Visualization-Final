# Image used for Woodpecker CI, that also contain all necessary requirements for the project
FROM python:3.12-slim

# Copy the pre-compiled uv binary from Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Run the uv to install dependencies directly onto the system environtment
RUN uv pip install --system --no-cache -r requirements.txt
