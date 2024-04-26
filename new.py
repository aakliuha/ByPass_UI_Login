from playwright.sync_api import sync_playwright



def create_browser_context():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    browser_context = browser.new_context()
    return browser_context

def log_in_rest():
    browser_context = create_browser_context()
    browser_context.add_cookies([{"name": "PHPSESSID", "value": "5katpf671bt07e0897v8jnncjlcs0ndn", "domain": ".makeup.com.ua", "path": "/", "expire": "2025-04-25T20:11:44.831Z"}])
    page = browser_context.new_page()
    page.goto("https://makeup.com.ua/ua/user/#history-order")
    page.pause()




log_in_rest()




