# tlsachecker

# DANE TLSA Record Checker

## Overview

The **DANE TLSA Record Checker** is a Python script designed to verify DANE TLSA records for specified web domains. This script ensures that the domain includes `http` or `https` and performs detailed checks for TLSA records, PKIX validation, and IP addresses.`.

## Features

- **Automatic Protocol Inclusion**: Automatically adds `https://` if the user does not specify `http` or `https`.
- **Detailed Output**: Provides comprehensive details about TLSA records, PKIX validation, and IP addresses.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/dane-tlsa-record-checker.git
    cd dane-tlsa-record-checker
    ```

2. **Run the Script**:
    ```bash
    python check_tlsa.py
    ```

3. **Follow the Prompts**:
    - Enter the domain name to check (e.g., `example.com`).
    - View the detailed output for TLSA records, PKIX validation, and IP addresses.
    - Choose whether to run another scan or exit the script.

## Example Output

```
Script created by Syafiee17x

Enter the domain name to check (e.g., example.com): example.com

========================================
Checking TLSA record for https://example.com
========================================
TLSA record:
No TLSA record found for _443._tcp.example.com.

IPv4 addresses:
93.184.216.34 PKIX-validated successfully

IPv6 addresses:
2606:2800:220:1:248:1893:25c8:1946 PKIX-validated successfully

========================================
Check complete for https://example.com
========================================

Do you want to run another scan? (yes/no):
```

## Requirements

- Python 3.x
- `dig` command-line tool

## License

This project is licensed under the MIT License. See the LICENSE file for details.
