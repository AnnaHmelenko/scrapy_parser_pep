from pathlib import Path

BOT_NAME = 'pep_parse'

DOMAIN = 'peps.python.org'

SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
