from pytest_playwright.pytest_playwright import browser
from playwright.sync_api import Page


def test_playwrightbasics(playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()
    page.goto("https://playwright.com/")

# chromium headless mode 1 single context
def test_playwrightshortcut(page:Page):
    page.goto("https://www.netflix.com/browse/genre/63676?bc=34399")