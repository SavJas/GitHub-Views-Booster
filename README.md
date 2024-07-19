# GitHub-Views-Booster

This script uses Selenium with multiple threads to visit and refresh a target URL at a high rate for 20 seconds, then slows down for 3 seconds to avoid rate limiting, cycling indefinitely. This approach helps increase the view count on a GitHub profile or repository while mitigating the risk of getting blocked due to excessive traffic.
![image](https://github.com/user-attachments/assets/2f66fb7e-b484-4d14-9469-108d3b3c932a)

## Features

- **High and Low Rate Cycles**: Visits the target URL at a high rate for 20 seconds, followed by a slower rate for 3 seconds.
- **Multi-threaded**: Utilizes multiple threads to maximize the number of visits.
- **Proxy Support**: Optional use of proxies to distribute traffic and reduce the likelihood of being blocked.
- **Configurable**: Easily configurable via `config.json` and `proxies.txt` files.

## Requirements

- Python 3.x
- Selenium
- Webdriver Manager
- Google Chrome Browser

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/github-views-booster.git
cd github-views-booster

2. Install the required Python packages:
pip install `-r requirements.txt`

3. Configure config.json:
{
  "target_url": "https://github.com/yourusername",
  "use_proxies": "n"
}

4. (Optional) Add proxies to proxies.txt:
http://proxy1:port
http://proxy2:port

## Usage
Run the script:
```python main.py```

## Estimated Views

I tested it, per minute you get 300 views, that means 300 * 60 = 18.000 or 18k Views per hour.

## Important Notice

Use a VPN while running this script to avoid IP-based rate limiting by GitHub.

## Disclaimer

This script is for educational purposes only. Use it responsibly and do not violate GitHub's terms of service.
