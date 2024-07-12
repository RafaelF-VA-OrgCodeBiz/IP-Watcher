# IP-Watcher
IP Change Notifier with DynDNS updater and Telegram Integration

Description:
This project provides a robust solution for monitoring IP address changes and sending notifications via Telegram. It seamlessly integrates with DynDNS to automatically update DNS records when IP changes occur. Configuration is managed through a config.ini file, allowing customization of settings such as Telegram bot tokens and chat IDs. Implemented in Python, the project utilizes libraries like requests for network requests and configparser for configuration management.

Key Features:

Monitors IP address changes.
Updates DynDNS entries upon IP changes.
Sends real-time notifications via Telegram.
Technologies Used:

Python
requests library
configparser library
asyncio (for asynchronous message handling)
Applications:
This tool is ideal for users needing to maintain accessibility to devices with dynamically changing IP addresses via DynDNS. With Telegram integration, users receive immediate alerts about IP changes, facilitating effective device management and monitoring.
