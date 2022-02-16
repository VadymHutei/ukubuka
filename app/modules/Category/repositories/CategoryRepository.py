from flask import request

from modules.Base.repositories.MySQLRepository import MySQLRepository


class CategoryRepository(MySQLRepository):

    def getCategories(self):
        currentLanguage = request.ctx['language'].code

        query = '''
            SELECT
                category.id,
                category.alias,
                category.parent_id,
                category.created_datetime,
                category.changed_datetime,
                category.is_active,
                category_text.name
            FROM
                category
            LEFT JOIN category_text
                ON category_text.category_id = category.id
                AND category_text.language = %s
        '''

        return self.fetchAll(query, (currentLanguage,))