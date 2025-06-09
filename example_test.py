import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://wikipedia.org")
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("searchbox", name="Search Wikipedia").fill("Python")
    page.get_by_role("button", name="Search").click()
    page.screenshot(path="screenshot.png")
    expect(page).to_have_title(re.compile("Python"))
