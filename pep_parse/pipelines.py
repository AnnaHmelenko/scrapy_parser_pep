import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)
        self.items = []

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        self.items.append(item)
        return item

    def close_spider(self, spider):
        feeds = spider.settings.get('FEEDS', {})

        if feeds:
            first_feed_path = next(iter(feeds.keys()))
            if isinstance(first_feed_path, str):
                feed_path = Path(first_feed_path)
            else:
                feed_path = first_feed_path
            results_dir = feed_path.parent
        else:
            results_dir = Path('results')

        results_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        summary_filename = results_dir / f'status_summary_{timestamp}.csv'
        with open(summary_filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])

            total = 0
            for status, count in sorted(self.statuses.items()):
                writer.writerow([status, count])
                total += count

            writer.writerow(['Total', total])

        pep_files = list(results_dir.glob('pep_*.csv'))
        if not pep_files:
            pep_filename = results_dir / f'pep_{timestamp}.csv'
            with open(pep_filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['number', 'name', 'status'])
                for item in self.items:
                    writer.writerow(
                        [item['number'], item['name'], item['status']])
