import schedule
import time
from match_scraper import scrape_matches
from result_scraper import scrape_results_and_standings

schedule.every(1).hours.do(scrape_matches)
schedule.every(2).minutes.do(scrape_results_and_standings)

print("[Scheduler] Running...")
while True:
    schedule.run_pending()
    time.sleep(1)