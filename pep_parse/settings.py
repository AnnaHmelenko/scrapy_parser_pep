from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [SPIDER_MODULE]
NEWSPIDER_MODULE = SPIDER_MODULE

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
