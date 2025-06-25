import subprocess
import sys

def run_spider():
    # Запускаємо scrapy crawl quotes і зберігаємо результати в json-файли
    subprocess.run([sys.executable, "-m", "scrapy", "crawl", "quotes", "-o", "quotes.json"])
    subprocess.run([sys.executable, "-m", "scrapy", "crawl", "authors", "-o", "authors.json"])

if __name__ == "__main__":
    run_spider()
