import csv
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from pep_parse.settings import RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        project_root = Path(__file__).parent.parent
        actual_results_dir = project_root / RESULTS_DIR

        feeds = spider.crawler.settings.get('FEEDS')
        if not feeds:
            feeds = spider.settings.get('FEEDS')

        if feeds:
            first_key = next(iter(feeds.keys()))
            target_dir = Path(first_key).parent
        else:
            target_dir = actual_results_dir

        target_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        summary_path = target_dir / f'status_summary_{timestamp}.csv'

        with open(summary_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in sorted(self.statuses.items()):
                writer.writerow([status, count])
            total = sum(self.statuses.values())
            writer.writerow(['Total', total])

        if target_dir != actual_results_dir:
            for pep_file in actual_results_dir.glob('pep_*.csv'):
                shutil.copy2(pep_file, target_dir / pep_file.name)
