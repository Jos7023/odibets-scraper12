from playwright.sync_api import sync_playwright
from retry_utils import retry_with_alert
from supabase_client import upload_results_data, upload_standings_data
from config import MATCH_URL

@retry_with_alert
def scrape_results_and_standings():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(MATCH_URL, timeout=60000)
        page.wait_for_selector('li:has-text("Results")')
        page.click('li:has-text("Results")')
        page.wait_for_selector('div.result-item')

        results = []
        for r in page.query_selector_all('div.result-item'):
            results.append({
                'date': r.query_selector('div.date').inner_text().strip(),
                'teams': r.query_selector('div.teams').inner_text().strip(),
                'score': r.query_selector('div.score').inner_text().strip()
            })
        upload_results_data(results)

        page.goto(MATCH_URL, timeout=60000)
        page.click('li:has-text("Standings")')
        page.wait_for_selector('table.standings')

        standings = []
        for row in page.query_selector_all('table.standings tr')[1:]:
            cols = row.query_selector_all('td')
            standings.append({
                'position': cols[0].inner_text().strip(),
                'team': cols[1].inner_text().strip(),
                'played': cols[2].inner_text().strip(),
                'points': cols[3].inner_text().strip()
            })
        upload_standings_data(standings)
        browser.close()