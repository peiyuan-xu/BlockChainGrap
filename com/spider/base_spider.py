import urllib.request
from bs4 import BeautifulSoup


class BaseSpider:

    def __init__(self, chain_day_url, base_url):
        self.chain_day_url = chain_day_url
        self.base_url = base_url
        self.transactions_url = []

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

    def new_generated_conin(self, source_address):
        match_str = "No Inputs (Newly Generated Coins)"
        if match_str == source_address:
            return True
        return False

    def unable_output_address(self, dest_address):
        match_str = "Unable to decode output address"
        if match_str == dest_address:
            return True
        return False