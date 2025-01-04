# Reolink-Webhook-receiver

A simple Python server designed to handle webhook notifications from Reolink IP cameras.
This project is a basic Python server designed to receive and handle webhook notifications sent by Reolink IP cameras. Its simplicity makes it easy to understand and modify even with basic Python knowledge.

## What is a Webhook?

A webhook is a method by which an application (in this case, your Reolink camera) can automatically send real-time notifications to another application (your Python server) when a specific event occurs (e.g., motion detection). Instead of periodically "asking" if there are new events, the server "listens" for incoming notifications.

## Key Features

*   **Simplicity:** The code is intentionally kept simple to facilitate understanding and customization.
*   **Python:** Written in Python, a widely used programming language with a vast standard library.
*   **Customizable:** You can easily extend the functionalities to perform specific actions based on the received notifications.

## Requirements

*   Python (version 3.x recommended)
*   A Reolink IP camera configured to send webhooks (tested on RLC-820A, firmware version: v3.1.0.4054_2409131254, hardware version: IPC_56064M8MP)

## How it Works (Conceptually)

1.  The Reolink camera detects an event (e.g., motion).
2.  The camera sends an HTTP POST request to your Python server, containing the event data.
3.  Your Python server receives the request, analyzes its content, and can perform actions accordingly.

## How to run this server
Prerequisites:
*   Python 3.x installed.
*   Dependencies `http.server` and `json` present in the sysem (these are present by default in most cases).
*   The `server_webhook_reolink.py` file.

Run:
```bash
python server_webhook_reolink.py
```
