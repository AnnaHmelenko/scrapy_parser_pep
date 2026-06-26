import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        summary_path = results_dir / f'status_summary_{timestamp}.csv'

        with open(summary_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in sorted(self.statuses.items()):
                writer.writerow([status, count])
            total = sum(self.statuses.values())
            writer.writerow(['Total', total])
