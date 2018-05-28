from com.db.basedao import BaseDAO
from com.db import models
from com.db import common


class UserDAO(BaseDAO):
    def get_user_by_id(self, id):
        return self.get_resource(models.User, id)

    def create_user(self):
        code = common.generate_uuid()
        user_dict = {'code': code}
        return self.create_resource(models.User, user_dict)


class AddressDAO(BaseDAO):
    def get_address_by_address(self, address):
        filter = {'address': address}
        return self.get_resource_by_attr(models.Address, filter)

    def create_address(self, user_id, address):
        result = self.get_address_by_address(address)
        if not result:
            address_dict = {'user_id': user_id, 'address': address}
            return self.create_resource(models.Address, address_dict)
        return result


class TransactionDAO(BaseDAO):
    def create_transaction(self, source, destination, value):
        transaction_dict = {'source': source, 'destination': destination, 'value': value}
        return self.create_resource(models.Transaction, transaction_dict)

    def paginate_list(self, page_num):
        return self.paginate_list_resource(page_num)