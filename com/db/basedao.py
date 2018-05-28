"""
Basic class for operating DB
"""
from sqlalchemy.inspection import inspect

from com.db import common
from com.common import exceptions


class BaseDAO:

    def create_resource(self, model, res_dict):

        res_object = model.from_dict(res_dict)
        session = common.get_session()
        session.add(res_object)
        session.commit()
        # retrieve auto-generated fields
        session.refresh(res_object)
        return res_object.to_dict()

    def _get_resource(self, model, pk_value):
        session = common.get_session()
        res_obj = session.query(model).get(pk_value)
        if not res_obj:
            raise exceptions.ResourceNotFound(model, pk_value)
        return res_obj

    def delete_resource(self, model, pk_value):
        res_obj = self._get_resource(model, pk_value)
        session = common.get_session()
        session.delete(res_obj)
        session.commit()

    def update_resource(self, model, pk_value, update_dict):
        res_obj = self._get_resource(model, pk_value)
        session = common.get_session()
        for key in update_dict:
            if key not in model.attributes:
                continue

            skip = False
            for pkey in inspect(model).primary_key:
                if pkey.name == key:
                    skip = True
                    break

            if skip:
                continue

            setattr(res_obj, key, update_dict[key])
        session.commit()
        return res_obj.to_dict()

    def get_resource(self, model, pk_value):
        return self._get_resource(model, pk_value).to_dict()

    def get_resource_by_attr(self, model, filter_dict):
        session = common.get_session()
        resource = session.query(model).filter_by(**filter_dict).first()
        session.commit()
        return resource

    def list_resources_by_attr(self, model, filter_dict):
        session = common.get_session()
        resources = session.query(model).filter_by(**filter_dict).all()
        session.commit()
        return resources

    def paginate_list_resource(self, model, page_num):
        page_size = 100
        session = common.get_session()
        return session.query(model).filter_by().limit(page_size).offset((page_num) * page_size)
