#!/bin/bash
echo "Starting process..."

sleep 60 &

PID=$!

echo "Process PID: $PID"

if ps -p "$PID" > /dev/null; then
    echo "Process is running."
else
    echo "Process is not running."
fi

kill -TERM "$PID"

sleep 1

if ps -p "$PID" > /dev/null; then
    echo "Process is still running."
else
    echo "Process has stopped successfully."
fi
