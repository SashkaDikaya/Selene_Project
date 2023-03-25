from selene import browser
from selene import be, have

def test_open_browser():
    browser.open_url("https://mangalib.me/?section=home-updates")
    browser.element("#search-link").click()
    browser.element("//input").set_value("Алхимик").press_enter()
    browser.all("manga-list-item__name").element_by(have.text("Стальной алхимик")).click()
