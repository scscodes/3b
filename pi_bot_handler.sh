#!/bin/bash

# Path to your .env file
ENV_FILE=".env"

# Run the cloudflared command in the background and discard logs after processing
CLOUDFLARED_LOG="/tmp/cloudflared.log"
cloudflared tunnel --url http://localhost:5000 > "$CLOUDFLARED_LOG" 2>&1 &
CLOUDFLARED_PID=$!

# Wait for the URL to appear in the log file
WEBHOOK_URL=""
while [ -z "$WEBHOOK_URL" ]; do
    WEBHOOK_URL=$(grep -oP 'https://[a-zA-Z0-9.-]+\.trycloudflare\.com' "$CLOUDFLARED_LOG")
    sleep 1

done

# Check if a URL was successfully extracted
if [ -n "$WEBHOOK_URL" ]; then
    echo "Extracted URL: $WEBHOOK_URL"

    # Update the .env file with the new WEBHOOK_URL value
    if grep -q '^WEBHOOK_URL=' "$ENV_FILE"; then
        # If WEBHOOK_URL exists, replace it
        sed -i "s|^WEBHOOK_URL=.*|WEBHOOK_URL=$WEBHOOK_URL|" "$ENV_FILE"
    else
        # If WEBHOOK_URL does not exist, append it
        echo "WEBHOOK_URL=$WEBHOOK_URL" >> "$ENV_FILE"
    fi

    echo ".env file updated with WEBHOOK_URL=$WEBHOOK_URL"

    # Run Python applications
    echo "Starting Python applications..."
    python set_webhook.py
    sleep 1
    python app.py > /dev/null 2>&1 &
else
    echo "Error: Could not extract a URL from the cloudflared output."
    exit 1
fi

# Limit the size of the log file to prevent it from becoming too large
truncate -s 0 "$CLOUDFLARED_LOG"
