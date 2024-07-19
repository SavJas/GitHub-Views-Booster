import json
import time
import random
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def load_proxies():
    with open('proxies.txt') as proxy_file:
        return [line.strip() for line in proxy_file]

def set_proxy(options, proxy):
    options.add_argument(f'--proxy-server={proxy}')

def view_page(target_url, use_proxies, proxies):
    # Setup Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3')

    if use_proxies and proxies:
        proxy = random.choice(proxies)
        set_proxy(options, proxy)

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    high_rate_duration = 22
    slow_rate_duration = 3
    high_rate_delay = 0.01
    slow_rate_delay = 2.5

    try:
        while True:
            # High rate phase
            cycle_start_time = time.time()
            while time.time() - cycle_start_time < high_rate_duration:
                driver.get(target_url)
                print("Visited", target_url)
                driver.refresh()
                time.sleep(high_rate_delay)

            # Slow rate phase
            cycle_start_time = time.time()
            while time.time() - cycle_start_time < slow_rate_duration:
                driver.get(target_url)
                print("Visited", target_url)
                driver.refresh()
                time.sleep(slow_rate_delay)

    except Exception as e:
        print(f"Exception occurred - {e}")
    finally:
        driver.quit()

def main():
    config = load_config()
    target_url = config["target_url"]
    use_proxies = config["use_proxies"].lower() == 'y'
    
    proxies = load_proxies() if use_proxies else []
    
    num_threads = 12
    
    threads = []
    
    for _ in range(num_threads):
        thread = threading.Thread(target=view_page, args=(target_url, use_proxies, proxies))
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping all threads.")

if __name__ == "__main__":
    main()
