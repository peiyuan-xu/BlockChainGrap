from com.graph.user_graph import UserGraph


def start_genarate_user_graph():
    user_graph = UserGraph()
    user_graph.init_connect()
    # user_graph.clear_data()
    user_graph.generate_user_graph()

start_genarate_user_graph()