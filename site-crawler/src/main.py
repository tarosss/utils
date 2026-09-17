from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(
        viewport={
            "width": 1440,
            "height": 900,
        }
    )

    page.goto("https://nhentai.net/g/435258/", wait_until="domcontentloaded", timeout=60000)

    page.screenshot(
        path="/app/screenshots/example.png",
        full_page=True,
    )

    browser.close()