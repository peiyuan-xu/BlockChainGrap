from com.db import common
from com.db.models import ModelBase
from com.spider.user_spider import UserSpider


def init_db():
    ModelBase.metadata.create_all(common.get_engine())


def drop_db():
    ModelBase.metadata.drop_all(common.get_engine())


chain_day_url = [
            'https://blockchain.info/blocks/1527226494065']
base_url = 'https://blockchain.info/block/'


def cluster_user():
    spider_user = UserSpider(chain_day_url, base_url)
    spider_user.spider_user_cluster()

drop_db()
init_db()

cluster_user()
