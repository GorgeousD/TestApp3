import pytest
from playwright.sync_api import sync_playwright, expect
import datetime

# Фикстура для инициализации Playwright
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Для отладки headless=False
        page = browser.new_page()
        yield page
        browser.close()

# Параметризация: список запросов и ожидаемых заголовков
@pytest.mark.parametrize("search_query, expected_title", [
    ("Python", "Python — Википедия"),
    ("JavaScript", "JavaScript — Википедия"),
    ("QA", "QA — Википедия"),
])
def test_wikipedia_search(page, search_query, expected_title):
    # Открываем Wikipedia
    page.goto("https://www.wikipedia.org/")

    #Вводим запрос и нажимаем кнопку поиска
    page.fill('input[name="search"]', search_query)
    page.get_by_role("button", name="Search").click()

    # Проверяем заголовок статьи
    expect(page.locator('h1#firstHeading')).to_be_visible()
    expect(page).to_have_title(expected_title)

    # Делаем скриншот
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    page.screenshot(path=f"screenshots/screenshot_{search_query}_{timestamp}.png")