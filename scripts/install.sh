#!/bin/bash

set -e

INSTALL_DIR="/opt/inframind"

echo "Installing InfraMind GPU Agent..."

sudo mkdir -p $INSTALL_DIR
sudo cp -r agent $INSTALL_DIR/

echo "InfraMind installed at $INSTALL_DIR"
echo "Run with: python3 $INSTALL_DIR/agent/gpu_collector.py"

