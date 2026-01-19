# InfraMind GPU Agent – Architecture

## Overview
InfraMind is a lightweight Linux agent designed to provide visibility into GPU and system health.

## Execution Flow
1. Agent starts on Linux
2. Detects GPU availability
3. Collects system metrics
4. Collects GPU metrics (if available)
5. Outputs structured JSON

## Modes
- GPU_REAL: NVIDIA GPU detected
- NO_GPU: Linux without GPU
- UNSUPPORTED: Non-Linux OS

## Deployment
- Docker container
- Bare-metal Linux
- Kubernetes DaemonSet (future)

## Future Enhancements
- Prometheus metrics
- GPU anomaly detection
- Central controller

