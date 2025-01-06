#!/usr/bin/env bash

LOGFILE="/var/log/setup-network-manager.log"

log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') | $*" | tee -a "$LOGFILE"
}

run_or_fail() {
  log "Running: $*"
  if ! "$@"; then
    log "ERROR: '$*' failed."
    exit 1
  fi
}

run_or_warn() {
  log "Running: $*"
  if ! "$@"; then
    log "WARNING: '$*' failed, continuing."
  fi
}

# Capture all output in LOGFILE
exec > >(tee -a "$LOGFILE") 2>&1

if [[ $EUID -ne 0 ]]; then
  log "Please run as root (sudo)."
  exit 1
fi

# log "Updating packages..."
# run_or_fail apt-get update

log "Installing NetworkManager..."
run_or_fail apt-get install -y network-manager

# Stop/disable dhcpcd, but don't fail if it can't be stopped or disabled
log "Disabling dhcpcd..."
run_or_warn systemctl disable dhcpcd
log "Stopping dhcpcd..."
run_or_warn systemctl stop dhcpcd

log "Enabling NetworkManager..."
run_or_fail systemctl enable NetworkManager
log "Starting NetworkManager..."
run_or_fail systemctl start NetworkManager

log "NetworkManager is installed and running. Launching mtui..."
nmtui
