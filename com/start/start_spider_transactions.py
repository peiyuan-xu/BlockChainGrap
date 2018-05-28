from com.spider.transaction_spider import TransactionSpider


chain_day_url = [
            'https://blockchain.info/blocks/1527226494065']
base_url = 'https://blockchain.info/block/'


def collect_transactions():
    transaction_spider = TransactionSpider(chain_day_url, base_url)
    transaction_spider.spider_all_transactions()


collect_transactions()