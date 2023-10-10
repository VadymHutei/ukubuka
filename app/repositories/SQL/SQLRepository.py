from repositories.IRepository import IRepository


class SQLRepository(IRepository):

    def create_where_conditions(self, conditions: list[str]) -> str:
        if not conditions:
            return ''

        return 'WHERE ' + ' AND '.join(conditions)