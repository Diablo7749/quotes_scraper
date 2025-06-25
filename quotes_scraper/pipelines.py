# Поки можна лишити пустим або видалити, якщо не використовуєш
class QuotesScraperPipeline:
    def process_item(self, item, spider):
        return item
