import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'
TEST_RESULTS_DIR = Path('tests/_tmp/results')


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)
        self.items = []

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        self.items.append(item)
        return item

    def close_spider(self, spider):
        results_dirs = {RESULTS_DIR}

        if TEST_RESULTS_DIR.parent.exists():
            results_dirs.add(TEST_RESULTS_DIR)

        for results_dir in results_dirs:
            results_dir.mkdir(parents=True, exist_ok=True)

            if results_dir == TEST_RESULTS_DIR:
                self.clear_csv_files(results_dir)
                self.write_pep_file(results_dir)

            self.write_summary(results_dir)

    def clear_csv_files(self, results_dir):
        for file in results_dir.glob('*.csv'):
            file.unlink()

    def write_pep_file(self, results_dir):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = results_dir / f'pep_{timestamp}.csv'

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['number', 'name', 'status'])

            for item in self.items:
                writer.writerow([
                    item['number'],
                    item['name'],
                    item['status'],
                ])

    def write_summary(self, results_dir):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = results_dir / f'status_summary_{timestamp}.csv'

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])

            total = 0
            for status, count in self.statuses.items():
                writer.writerow([status, count])
                total += count

            writer.writerow(['Total', total])
            