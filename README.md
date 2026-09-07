# Custom Python Network Scanner

## 📌 Project Overview
A custom, lightweight network reconnaissance tool developed in Python. This script automates the discovery of open TCP ports on a target IP address, enabling cybersecurity professionals to perform initial vulnerability assessments efficiently.

## 🛠️ Features & Functionality
* **Multi-Port Scanning:** Scans a predefined list of high-value ports (e.g., 21, 22, 80, 443, 8080).
* **Timeout Optimization:** Utilizes connection timeout bounds to speed up scan sequences.
* **Error Handling:** Employs socket status codes (`connect_ex`) to determine port status silently without crashing.

## 🚀 How It Works
The script utilizes Python's native `socket` library to attempt a TCP three-way handshake with specified ports on the target host. If the connection returns a status of `0`, the port is flagged as **OPEN**.

