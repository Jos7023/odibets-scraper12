from playwright.sync_api import sync_playwright
from retry_utils import retry_with_alert
from supabase_client import upload_match_data
from config import MATCH_URL

@retry_with_alert
def scrape_matches():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(MATCH_URL, timeout=60000)
        page.wait_for_selector('div.match')

        matches = []
        for match in page.query_selector_all('div.match'):
            try:
                timestamp = match.query_selector('div.ss').inner_text().strip()
                home = match.query_selector('div.t-l').inner_text().strip()
                away = match.query_selector('div.t-r').inner_text().strip()
                match_data = {
                    'timestamp': timestamp,
                    'home_team': home,
                    'away_team': away,
                    'markets': []
                }
                for btn in match.query_selector_all('button:not(.o)'):
                    market = btn.inner_text().strip()
                    btn.click()
                    page.wait_for_selector('div.odds')
                    odds = []
                    for o in match.query_selector_all('div.odds button'):
                        label = o.query_selector('small.o-1').inner_text().strip()
                        val = o.query_selector('span.o-2').inner_text().strip()
                        odds.append({"label": label, "value": float(val)})
                    match_data['markets'].append({"market_name": market, "odds": odds})
                matches.append(match_data)
            except Exception as e:
                continue
        upload_match_data(matches)
        browser.close()