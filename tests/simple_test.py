from selene import browser
from selene import be, have

def test_open_browser():
    browser.open_url("https://mangalib.me")
    browser.element("#search-link").click()
    browser.element("//input").set_value("Алхимик").press_enter()
    browser.elements(".manga-list-item__name").find_by(have.text("Стальной алхимик")).click()

