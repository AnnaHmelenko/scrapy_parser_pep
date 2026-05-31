from pathlib import Path

# Константа с именем бота
BOT_NAME = 'pep_parse'

# Константа с именем паука
SPIDER_NAME = 'pep'

# Используем константу с именем паука для формирования списка
SPIDER_MODULES = [f'{BOT_NAME}.spiders']

# Используем константу с именем бота (избавляемся от дублирования)
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