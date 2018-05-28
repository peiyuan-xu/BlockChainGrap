import re
import urllib.request

from bs4 import BeautifulSoup
from bs4.element import NavigableString

from com.db.api import TransactionDAO
from com.spider.base_spider import BaseSpider


class TransactionSpider(BaseSpider):
    def __init__(self, chain_day_url, base_url):
        super(TransactionSpider, self).__init__(chain_day_url, base_url)

    # now we should recorde every transaction
    def spider_transactions(self, url):
        # url = 'https://blockchain.info/block/00000000000000000010d0e4fb7732f2d1a30149fcfe3f0fb5d5216691d2296a'
        request = urllib.request.urlopen(url)
        content = request.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        # print(soup)
        # soup.find_all("div", class_="txdiv")[0].find_all('tr')[1].find_all('td')[0].contents
        all_transactions = soup.find_all("div", class_="txdiv")
        transaction_dao = TransactionDAO()

        for a_trans in all_transactions:
            source_addr = None
            source_addresses = a_trans.find_all('tr')[1].find_all('td')[0].contents
            for source_address in source_addresses:
                source_str = source_address.string
                if not source_str:
                    continue
                if self.new_generated_conin(source_str):
                    continue
                source_addr = source_str
                break

            destion_addr_and_btc_list = a_trans.find_all('tr')[1].find_all('td')[2].contents
            destion_str = None
            btc = 0.0

            for destion_pair in destion_addr_and_btc_list:
                if destion_pair.name == "br":
                    # a split for a destination
                    destion_str = None
                    btc = 0.0
                    continue
                if type(destion_pair) == NavigableString:
                    continue

                temp_str = destion_pair.string
                if not temp_str:
                    continue
                if self.unable_output_address(temp_str):
                    continue

                if not re.match(r'(.*?) BTC', temp_str):
                    destion_str = temp_str
                else:
                    btc = float(re.match(r'(.*?) BTC', temp_str).group(1).replace(',', ''))
                    if destion_str and btc > 0:
                        transaction_dao.create_transaction(source_addr, destion_str, btc)

    def spider_all_transactions(self):
        self.spider_blocks_in_a_day()
        print("===共有 " + str(len(self.transactions_url)) + " 页交易信息")
        count = 1
        for tran_url in self.transactions_url[0:50]:
            print("==Collect Transactions 第 " + str(count) + " / " + str(len(self.transactions_url)) + " 页")
            count += 1
            self.spider_transactions(tran_url)

#spider_trans = TransactionSpider()
#url = 'https://blockchain.info/block/00000000000000000010d0e4fb7732f2d1a30149fcfe3f0fb5d5216691d2296a'
#spider_trans.spider_transactions(url)