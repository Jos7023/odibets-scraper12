from alert import send_error_email
import time

def retry_with_alert(func):
    def wrapper(*args, **kwargs):
        for attempt in range(4):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[Retry] {func.__name__} failed (attempt {attempt+1})")
                time.sleep(5)
        send_error_email(
            f"SCRAPER ERROR: {func.__name__}",
            f"Failed after 4 retries.\nFunction: {func.__name__}"
        )
    return wrapper