from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('https://health-management-app.onrender.com/')
        time.sleep(20)
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()