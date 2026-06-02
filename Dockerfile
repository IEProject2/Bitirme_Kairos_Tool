FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy package files
COPY pyproject.toml setup.cfg MANIFEST.in README.md ./
COPY factory_sim ./factory_sim
COPY examples ./examples

# Install the package
RUN pip install --no-cache-dir -e .

# Create a non-root user
RUN useradd -m -u 1000 simuser && chown -R simuser:simuser /app
USER simuser

# Expose port for potential web UI
EXPOSE 8080

# Default command
CMD ["python", "-c", "from factory_sim import SimulationEngine; print('Factory Sim Framework ready')"]
