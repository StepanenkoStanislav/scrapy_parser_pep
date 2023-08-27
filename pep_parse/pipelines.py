from datetime import datetime as dt
import csv

from pep_parse.settings import DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.statuses = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        filename = f'status_summary_{dt.now().strftime(DATETIME_FORMAT)}.csv'
        with open(BASE_DIR / 'results' / filename,
                  'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Статус', 'Количество'])
            csv_writer.writerows(self.statuses.items())
            csv_writer.writerow(['Total', sum(self.statuses.values())])
