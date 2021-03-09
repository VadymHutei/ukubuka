import pymysql.cursors

from ukubuka.AbstractRepository import AbstractRepository


class ShopRepository(AbstractRepository):
    
    def getCatalogByAlias(self, alias):
        query = f'''
            SELECT
                *
            FROM
                catalog
            WHERE
                alias = '{alias}'
        '''

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     database='ukubuka',
                                     cursorclass=pymysql.cursors.DictCursor)

        return query