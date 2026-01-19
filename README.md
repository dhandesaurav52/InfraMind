# InfraMind GPU Agent

InfraMind GPU Agent is a Linux-first infrastructure observability tool designed to monitor system and NVIDIA GPU health.

## Why InfraMind?
GPUs are expensive, scarce, and often underutilized. Traditional monitoring tools focus on CPU and memory while ignoring GPUs.

InfraMind brings visibility to GPU infrastructure.

## Features
- Linux system health monitoring
- NVIDIA GPU detection
- GPU utilization, memory, and temperature metrics
- Docker-ready deployment

## Supported Platforms
- Ubuntu 20.04+
- Linux with NVIDIA GPUs
- macOS (development only)

## Run Locally
```bash
python3 agent/gpu_collector.py

