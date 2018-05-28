from py2neo import Graph, Node, Relationship

from com.db import models
from com.db.api import AddressDAO, UserDAO, TransactionDAO


class UserGraph:

    def __init__(self):
        self.graph = None
        self.label = "Account"
        self.user_dao = UserDAO()
        self.address_dao = AddressDAO()
        self.transaction_dao = TransactionDAO()

    def init_connect(self):
        self.graph = Graph("http://127.0.0.1:7474", username="neo4j", password="neo4j")

    def clear_data(self):
        self.graph.delete_all()

    def create_a_user_node(self, name_code, btc):
        a_user = Node(self.label, name=name_code, btc=btc)
        return self.graph.create(a_user)

    def get_a_user_node_by_code(self, name_code):
        user_node = self.graph.find_one(
            self.label,
            property_key='name',
            property_value=name_code)
        return user_node

    def add_a_transaction(self, transaction_dict):
        if not transaction_dict['source']:
            # check the user node, if no create
            destination = transaction_dict['destination']
            temp_result = self.address_dao.get_address_by_address(destination)
            if not temp_result:
                # this destination address haven't recorded in address table
                new_user_for_dest = self.user_dao.create_user()
                temp_result = self.address_dao.create_address(new_user_for_dest['id'], destination)

            # add a new node
            account_dest = self.user_dao.get_user_by_id(temp_result['user_id'])
            account_node = self.get_a_user_node_by_code(account_dest['code'])
            if account_node:
                account_node['btc'] += transaction_dict['value']
                self.graph.push(account_node)
            else:
                self.create_a_user_node(account_dest['code'], transaction_dict['value'])
            return
        # if have source and destination address, not only need to check node but also add relation
        source = transaction_dict['source']
        destination = transaction_dict['destination']
        # source address must be exit, so skip to check
        temp_source_result = self.address_dao.get_address_by_address(source)
        temp_dest_result = self.address_dao.get_address_by_address(destination)
        if not temp_dest_result:
            new_user_for_dest = self.user_dao.create_user()
            temp_dest_result = self.address_dao.create_address(new_user_for_dest['id'], destination)

        # get source acount and check and update node
        account_source = self.user_dao.get_user_by_id(temp_source_result['user_id'])
        account_source_node = self.get_a_user_node_by_code(account_source['code'])
        if account_source_node:
            account_source_node['btc'] -= transaction_dict['value']
            self.graph.push(account_source_node)
        else:
            self.create_a_user_node(account_source['code'], -transaction_dict['value'])
            account_source_node = self.get_a_user_node_by_code(account_source['code'])

            # get destination acount and check and update node
        account_destination = self.user_dao.get_user_by_id(temp_dest_result['user_id'])
        account_destination_node = self.get_a_user_node_by_code(account_destination['code'])
        if account_destination_node:
            account_destination_node['btc'] += transaction_dict['value']
            self.graph.push(account_destination_node)
        else:
            self.create_a_user_node(account_destination['code'], transaction_dict['value'])
            account_destination_node = self.get_a_user_node_by_code(account_destination['code'])

        # add the relationship for two node
        source_node_pay_destination_node = self.graph.match_one(start_node=account_source_node, end_node=account_destination_node, bidirectional=False)
        if source_node_pay_destination_node:
            source_node_pay_destination_node['btc'] += transaction_dict['value']
            self.graph.push(source_node_pay_destination_node)
        else:
            source_node_pay_destination_node = Relationship(account_source_node, "Pay", account_destination_node)
            source_node_pay_destination_node['btc'] = transaction_dict['value']
            self.graph.create(source_node_pay_destination_node)

    def generate_user_graph(self):
        page_total = 100
        for page_num in range(page_total):
            print("====Generate User Graph 处理第 " + str(page_num) + " / " + str(page_total) + " 页交易（100/page）")
            transaction_list = self.transaction_dao.paginate_list_resource(models.Transaction, page_num)
            count = 1
            for item_transaction in transaction_list:
                # print("==处理本页第 " + str(count) + " / 100" + " 个交易")
                count += 1
                # print(item_transaction)
                # deal each transaction
                transaction_dict = {
                    'source': item_transaction['source'],
                    'destination': item_transaction['destination'],
                    'value': item_transaction['value']
                }
                self.add_a_transaction(transaction_dict)


#user_graph = UserGraph()
#user_graph.init_connect()
#user_graph.generate_user_graph()