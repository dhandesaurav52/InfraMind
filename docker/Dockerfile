FROM ubuntu:22.04

LABEL name="InfraMind GPU Agent"
LABEL version="0.1.0"
LABEL description="Linux GPU infrastructure observability agent"

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    procps \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/inframind

COPY agent/ agent/

CMD ["python3", "agent/gpu_collector.py"]

