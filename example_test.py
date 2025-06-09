from playwright.sync_api import sync_playwright, expect
import datetime

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Открываем страницу Wikipedia
    page.goto("https://www.wikipedia.org/")

    # Вводим запрос и нажимаем кнопку поиска
    page.fill('input[name="search"]', "Python")
    page.get_by_role("button", name="Search").click()

    # Проверяем заголовок
    expect(page).to_have_title("Python — Википедия")
    print("Успех: заголовок совпадает")

    # Скриншот
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    page.screenshot(path=f"screenshot_{timestamp}.png")