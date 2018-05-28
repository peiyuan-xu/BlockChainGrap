from py2neo import Graph, Node, Relationship

from com.db.api import AddressDAO, UserDAO, TransactionDAO
from com.graph.user_graph import UserGraph


class UserGraphService(UserGraph):
    def __init__(self):
        self.graph = None
        self.label = "Account"
        self.user_dao = UserDAO()
        self.address_dao = AddressDAO()
        self.transaction_dao = TransactionDAO()

    def get_connect(self):
        self.graph = Graph("http://127.0.0.1:7474", username="neo4j", password="neo4j")

    def get_pay_chain_for_two_address(self, source_address, destination_address):
        # show graph in browser
        # MATCH (n:Account{name:'cdda6a23-3280-43fe-a159-07385c12b9ca'})-->(m:Account{name:'4f4cf283-db85-490f-9b95-ad87ac21e7c6'}) RETURN n, m;

        source_code = self.address_dao.get_address_by_address(source_address)['user']['code']
        dest_code = self.address_dao.get_address_by_address(destination_address)['user']['code']
        account_source_node = self.get_a_user_node_by_code(source_code)
        account_dest_node = self.get_a_user_node_by_code(dest_code)

        source_node_pay_destination_node = self.graph.match_one(start_node=account_source_node,
                                                                end_node=account_dest_node, bidirectional=False)
        print(source_node_pay_destination_node)


graph_service = UserGraphService()
graph_service.get_connect()
graph_service.get_pay_chain_for_two_address('1G6iPYeuG2kg7KVXDHaFt2ZWjp7uzND7yL', '19txGGGNyQBdR4T8WaACZHgJ8FpuqKT4Bu ')