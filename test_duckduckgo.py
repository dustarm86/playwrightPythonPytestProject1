import re
from playwright.sync_api import Page, expect


def test_visit_duckduckgo_and_search(page: Page) -> None:
    page.goto("https://www.duckduckgo.com")
    expect(page).to_have_title(re.compile("DuckDuckGo — Privacy, simplified."))
    page.fill('input[name="q"]', "computer science wikipedia")
    page.get_by_label("Search", exact=True).click()
    assert page.inner_text('a[href="https://en.wikipedia.org/wiki/Computer_science"]')
    page.get_by_role("link", name="Computer science - Wikipedia", exact=True).click()
