# HowManyIPs

## Overview
HowManyIPs is a simple, yet powerful tool designed to calculate the total number of hosts in IP ranges specified in CIDR notation. It allows users to input either a single CIDR address or a file containing multiple CIDR entries.

## Features
- **Single CIDR Processing**: Input a single IP range in CIDR notation to get the total number of hosts.
- **Bulk CIDR Processing**: Input a file containing multiple CIDR notations for bulk processing.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup
1. Clone the repository:
```normal
git clone https://github.com/smhuda/howmanyips.git
```
2. Navigate to the cloned directory:
```normal
cd howmanyips
```
3. Install the required packages:
```normal
pip install -r requirements.txt
```

## Usage

### Single CIDR Notation
To process a single CIDR notation, use the following command:

```normal
python checkmyips.py <192.168.1.0/24>
```

### File Containing Multiple CIDR Notations
To process a file containing multiple CIDR notations, use the following command:

```normal
python checkmyips.py <ip-cidr-range.txt>
```

## Contributing
Contributions, issues, and feature requests are welcome! 

If you liked this or it helped you in anyway

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/smhuda)
