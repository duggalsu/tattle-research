"""
Set constants
"""
import os

# Output data directory
DIR_UP_PATH = ".."

# File names
SCRAPE_TIME_FILENAME = "scrape_time.json"
CRAWLED_URLS_BEGIN_FILENAME = "crawled_urls_"
DOWNLOADED_ARTICLES_BEGIN_FILENAME = "downloaded_articles_"

CRAWLED_URLS_FILE_EXTENSION = ".pkl"
DOWNLOADED_ARTICLES_FILE_EXTENSION = ".pkl"

# other dir
TEMP_PIPELINE_OUTPUT = "temp_pipeline_output"
LOGS_DIR = "logs"

# data dir
DATA_DIR = "data"
DATA_RAW_DIR = "raw"

# paths
SCRAPE_TIME_FILEPATH = os.path.join(DIR_UP_PATH, SCRAPE_TIME_FILENAME)
TEMP_PIPELINE_FILEPATH = os.path.join(DIR_UP_PATH, TEMP_PIPELINE_OUTPUT)
DATA_RAW_FILEPATH = os.path.join(DIR_UP_PATH, DATA_DIR, DATA_RAW_DIR)

# log tags
LOG_TAG_CRAWLER = "CRAWLER"
LOG_TAG_ARTICLE_DOWNLOADER = "ARTICLE_DOWNLOADER"
LOG_TAG_ARTICLE_PARSER = "ARTICLE_PARSER"
LOG_TAG_EMBEDDED_MEDIA_DOWNLOADER = "EMBEDDED_MEDIA_DOWNLOADER"
LOG_TAG_DATA_FORMATTER = "DATA_FORMATTER"
LOG_TAG_DATA_UPOADER = "DATA_UPLOADER"

# scraping mode for saving data
MODE_LOCAL = "local"
MODE_REMOTE = "remote"
MODE_INVALID = "mode_invalid"

# log file name
LOG_FILE = "scraper.log"

# MongoDB
SCRAPING_DB_DEV = "factcheck_sites_dev"
SCRAPING_DB_COLL_STORIES = "stories"

# times to retry downloading article
RETRY_COUNT = 3

# sites config
SITES = {
    "altnews.in": {
        "url": "https://www.altnews.in",
        "langs": ["english"],
        "domain": "altnews.in",
        "getLinks": "get_historical_links_altnews",
        "getPost": "get_post_altnews",
    },
    "altnews.in/hindi": {
        "url": "https://www.altnews.in/hindi",
        "langs": ["hindi"],
        "domain": "altnews.in/hindi",
        "getLinks": "get_historical_links_altnews",
        "getPost": "get_post_altnews",
    },
    "boomlive.in": {
        "url": "https://www.boomlive.in/fake-news",
        "langs": ["english"],
        "domain": "boomlive.in",
        "body_div": 'div[@class="story"]',
        "img_link": "src",
    },
    "hindi.boomlive.in": {
        "url": "https://hindi.boomlive.in/fake-news",
        "langs": ["hindi"],
        "domain": "hindi.boomlive.in",
        "body_div": 'div[@class="story"]',
        "img_link": "src",
    },
    "bangla.boomlive.in": {
        "url": "https://bangla.boomlive.in/fake-news",
        "langs": ["bengali"],
        "domain": "bangla.boomlive.in",
        "body_div": 'div[@class="story"]',
        "img_link": "src",
    },
    "factly.in": {
        "url": "https://factly.in/category/fake-news",
        "langs": ["english", "telugu"],
        "domain": "factly.in",
        "body_div": "div[@itemprop='articleBody']",
    },
    "indiatoday.in": {
        "url": "https://www.indiatoday.in/fact-check",
        "langs": ["english"],
        "domain": "indiatoday.in",
        "header_div": "div[contains(@class,'node-story')]",
        "body_div": "div[contains(@itemprop,'articleBody')]",
    },
    "vishvasnews.com/hindi": {
        "url": "https://www.vishvasnews.com",
        "langs": ["hindi"],
        "domain": "vishvasnews.com/hindi",
        "body_div": "div[@class='lhs-area']",
    },
    "vishvasnews.com/english": {
        "url": "https://www.vishvasnews.com/english",
        "langs": ["english"],
        "domain": "vishvasnews.com/english",
        "body_div": "div[@class='lhs-area']",
    },
    "vishvasnews.com/punjabi": {
        "url": "https://www.vishvasnews.com/punjabi",
        "langs": ["punjabi"],
        "domain": "vishvasnews.com/punjabi",
        "body_div": "div[@class='lhs-area']",
    },
    "vishvasnews.com/assamese": {
        "url": "https://www.vishvasnews.com/assamese",
        "langs": ["assamese"],
        "domain": "vishvasnews.com/assamese",
        "body_div": "div[@class='lhs-area']",
    },
    "thequint.com": {
        "url": "https://www.thequint.com/news/webqoof",
        "langs": ["english"],
        "domain": "thequint.com",
        "getLinks": "get_historical_links_quint",
        "getPost": "get_post_quint",
    },
}
