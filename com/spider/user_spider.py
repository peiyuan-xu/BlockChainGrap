import urllib.request
from bs4 import BeautifulSoup

from com.db.api import AddressDAO, UserDAO
from com.spider.base_spider import BaseSpider


class UserSpider(BaseSpider):
    def __init__(self, chain_day_url, base_url):
        super(UserSpider, self).__init__(chain_day_url,base_url)

    def spider_blocks_in_a_day(self):
        for blocks_url in self.chain_day_url:
            request = urllib.request.urlopen(blocks_url)
            content = request.read().decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            block_trs = soup.find('table').find_all('tr')

            for block_tr in block_trs[1:]:
                href = block_tr.find_all('td')[2].find('a')
                if not href:
                    continue

                self.transactions_url.append(self.base_url + href.string)

    def spider_user_in_transactions(self, url):
        request = urllib.request.urlopen(url)
        content = request.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        # print(soup)
        # soup.find_all("div", class_="txdiv")[0].find_all('tr')[1].find_all('td')[0].contents
        all_transactions = soup.find_all("div", class_="txdiv")
        address_dao = AddressDAO()
        user_dao = UserDAO()

        for a_trans in all_transactions:
            source_addresses = a_trans.find_all('tr')[1].find_all('td')[0].contents
            # get all source address for a transaction, check if anyone of it is recorded
            recorded_should = False
            user_id = None
            for source_address in source_addresses:
                source_str = source_address.string
                if not source_str:
                    continue
                if self.new_generated_conin(source_str):
                    continue
                # check if any address is recorded
                recorded_should = True
                address_in_db = address_dao.get_address_by_address(source_str)
                if address_in_db:
                    user_id = address_in_db['user_id']
                    break

            # if all addresses have no record in db, this a new user
            if recorded_should and (not user_id):
                new_user = user_dao.create_user()
                user_id = new_user['id']

            # now address has user_id, so record
            for source_address in source_addresses:
                source_str = source_address.string
                if not source_str:
                    continue
                if self.new_generated_conin(source_str):
                    continue
                address_dao.create_address(user_id, source_str)

    def spider_user_cluster(self):
        self.spider_blocks_in_a_day()
        print("===共有 " + str(len(self.transactions_url)) + " 页交易信息")
        count = 1
        for tran_url in self.transactions_url[0:50]:
            print("==Cluster Users 第 " + str(count) + " / " + str(len(self.transactions_url)) + " 页")
            count += 1
            self.spider_user_in_transactions(tran_url)



#spider_user = SpiderUser()
#url = 'https://blockchain.info/block/00000000000000000010d0e4fb7732f2d1a30149fcfe3f0fb5d5216691d2296a'
#spider_user.spider_user_in_transactions(url)
# spider_user.spider_blocks_in_a_day()