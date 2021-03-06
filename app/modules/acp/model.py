import config
from db import DB



#     ##     ## ######## ##    ## ##     ##  ######
#     ###   ### ##       ###   ## ##     ## ##    ##
#     #### #### ##       ####  ## ##     ## ##
#     ## ### ## ######   ## ## ## ##     ##  ######
#     ##     ## ##       ##  #### ##     ##       ##
#     ##     ## ##       ##   ### ##     ## ##    ##
#     ##     ## ######## ##    ##  #######   ######



def getMenuItem(item_id):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `id`,
            `parent`,
            `link`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('menus'))
    cursor.execute(query, (item_id,))
    item_data = cursor.fetchone()
    if not item_data:
        connection.close()
        return {}
    query = """
        SELECT
            `language`,
            `name`
        FROM `{table}`
        WHERE `item_id` = %s
    """.format(table=db.table('menus_text'))
    cursor.execute(query, (item_id,))
    connection.close()
    item_text_data = cursor.fetchall()
    item_data['name'] = {}
    for row in item_text_data:
        if 'language' not in row: continue
        if row['name'] is None: continue
        if row['language'] not in config.LANGUAGES: continue
        if row['language'] not in item_data['name']: item_data['name'][row['language']] = row['name']
    return item_data

def getMenus(language, order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'parent', 'link', 'order', 'added', 'is_active', 'name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            m.`id` `id`,
            m.`parent` `parent`,
            m.`link` `link`,
            m.`order` `order`,
            m.`added` `added`,
            m.`is_active` `is_active`,
            mt.`name` `name`
        FROM `{table}` m
        LEFT JOIN `{table_t}` mt
            ON m.`id` = mt.`item_id`
        AND `language` = '{language}'
        {order}
    """.format(
        table=db.table('menus'),
        table_t=db.table('menus_text'),
        language=language,
        order=order_row
    )
    cursor.execute(query)
    connection.close()
    menu_items = cursor.fetchall()
    return menu_items if menu_items else []

def getMenusTree(language, order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'parent', 'link', 'order', 'added', 'is_active', 'name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            m.`id` `id`,
            m.`parent` `parent`,
            m.`link` `link`,
            m.`order` `order`,
            m.`added` `added`,
            m.`is_active` `is_active`,
            mt.`name` `name`
        FROM `{table}` m
        LEFT JOIN `{table_t}` mt
            ON m.`id` = mt.`item_id`
        AND `language` = '{language}'
        {order}
    """.format(
        table=db.table('menus'),
        table_t=db.table('menus_text'),
        language=language,
        order=order_row
    )
    cursor.execute(query)
    connection.close()
    menu_items = cursor.fetchall()
    if not menu_items: return []
    result = []
    for item in menu_items:
        if item['parent'] is None:
            menu = item.copy()
            menu['items'] = []
            result.append(menu)
    def setItems(result):
        for menu in result:
            for item in menu_items:
                if item['parent'] == menu['id']:
                    item_copy = item.copy()
                    item_copy['items'] = []
                    menu['items'].append(item_copy)
            if menu['items']:
                setItems(menu['items'])
    setItems(result)
    return result

def getMenuItemNames(language):
    db = DB()
    query = """
        SELECT
            m.`id`,
            t.`name`
        FROM `{table}` m
        RIGHT JOIN `{table_text}` t
            ON m.`id` = t.`item_id`
        WHERE t.`language` = %s
    """.format(
        table=db.table('menus'),
        table_text=db.table('menus_text')
    )
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, (language))
    connection.close()
    menus_names_data = cursor.fetchall()
    return {row['id']: row['name'] for row in menus_names_data} if menus_names_data else {}

def addMenuItem(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        INSERT INTO `{table}` (`parent`, `link`, `order`, `added`, `is_active`)
        VALUES (%s, %s, %s, %s, %s)
    """.format(table=db.table('menus'))
    cursor.execute(query, (data['parent'], data['link'], data['order'], data['added'], data['is_active']))
    item_id = cursor.lastrowid
    for language in config.LANGUAGES:
        prop_name = 'name_' + language
        if prop_name in data:
            query = """
                INSERT INTO `{table}` (`item_id`, `language`, `name`)
                VALUES (%s, %s, %s)
            """.format(table=db.table('menus_text'))
            cursor.execute(query, (item_id, language, data[prop_name]))
    connection.commit()
    connection.close()

def editMenuItem(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        UPDATE `{table}`
        SET
            `parent` = %s,
            `link` = %s,
            `order` = %s,
            `is_active` = %s
        WHERE `id` = %s
    """.format(table=db.table('menus'))
    cursor.execute(query, (data['parent'], data['link'], data['order'], data['is_active'], data['id']))
    for language in config.LANGUAGES:
        prop_name = 'name_' + language
        if prop_name in data:
            query = """
                INSERT INTO `{table}` (`item_id`, `language`, `name`)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY
                UPDATE `name` = %s
            """.format(table=db.table('menus_text'))
            cursor.execute(query, (data['id'], language, data[prop_name], data[prop_name]))
    connection.commit()
    connection.close()

def deleteMenuItem(item_id):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        DELETE FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('menus'))
    cursor.execute(query, (item_id,))
    connection.commit()
    connection.close()



#      ######  ##     ## ########  ########  ######## ##    ##  ######  #### ########  ######
#     ##    ## ##     ## ##     ## ##     ## ##       ###   ## ##    ##  ##  ##       ##    ##
#     ##       ##     ## ##     ## ##     ## ##       ####  ## ##        ##  ##       ##
#     ##       ##     ## ########  ########  ######   ## ## ## ##        ##  ######    ######
#     ##       ##     ## ##   ##   ##   ##   ##       ##  #### ##        ##  ##             ##
#     ##    ## ##     ## ##    ##  ##    ##  ##       ##   ### ##    ##  ##  ##       ##    ##
#      ######   #######  ##     ## ##     ## ######## ##    ##  ######  #### ########  ######



def getCurrency(code):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `code`,
            `name`,
            `symbol`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `code` = %s
    """.format(table=db.table('currencies'))
    cursor.execute(query, (code,))
    connection.close()
    currency = cursor.fetchone()
    if not currency: return {}
    return currency

def getCurrencies(order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('code', 'name', 'symbol', 'order', 'added', 'is_active'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            `code`,
            `name`,
            `symbol`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        {order}
    """.format(
        table=db.table('currencies'),
        order=order_row
    )
    cursor.execute(query)
    connection.close()
    currencies = cursor.fetchall()
    if not currencies: return []
    return currencies

def addCurrency(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        INSERT INTO `{table}` (`code`, `name`, `symbol`, `order`, `added`, `is_active`)
        VALUES (%s, %s, %s, %s, %s, %s)
    """.format(table=db.table('currencies'))
    cursor.execute(query, (data['code'], data['name'], data['symbol'], data['order'], data['added'], data['is_active']))
    connection.commit()
    connection.close()

def editCurrency(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        UPDATE `{table}`
        SET
            `code` = %s,
            `name` = %s,
            `symbol` = %s,
            `order` = %s,
            `is_active` = %s
        WHERE `code` = %s
    """.format(table=db.table('currencies'))
    cursor.execute(query, (data['new_code'], data['name'], data['symbol'], data['order'], data['is_active'], data['code']))
    connection.commit()
    connection.close()

def deleteCurrency(code):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        DELETE FROM `{table}`
        WHERE `code` = %s
    """.format(table=db.table('currencies'))
    cursor.execute(query, (code,))
    connection.commit()
    connection.close()



#     ##          ###    ##    ##  ######   ##     ##    ###     ######   ########  ######
#     ##         ## ##   ###   ## ##    ##  ##     ##   ## ##   ##    ##  ##       ##    ##
#     ##        ##   ##  ####  ## ##        ##     ##  ##   ##  ##        ##       ##
#     ##       ##     ## ## ## ## ##   #### ##     ## ##     ## ##   #### ######    ######
#     ##       ######### ##  #### ##    ##  ##     ## ######### ##    ##  ##             ##
#     ##       ##     ## ##   ### ##    ##  ##     ## ##     ## ##    ##  ##       ##    ##
#     ######## ##     ## ##    ##  ######    #######  ##     ##  ######   ########  ######



def getLanguage(code):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `code`,
            `name`,
            `is_default`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `code` = %s
    """.format(table=db.table('languages'))
    cursor.execute(query, (code,))
    connection.close()
    language = cursor.fetchone()
    if not language: return {}
    return language

def getLanguages(order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('code', 'name', 'is_default', 'order', 'added', 'is_active'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            `code`,
            `name`,
            `is_default`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        {order}
    """.format(
        table=db.table('languages'),
        order=order_row
    )
    cursor.execute(query)
    connection.close()
    languages = cursor.fetchall()
    if not languages: return []
    return languages

def addLanguage(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        INSERT INTO `{table}` (`code`, `name`, `is_default`, `order`, `added`, `is_active`)
        VALUES (%s, %s, %s, %s, %s, %s)
    """.format(table=db.table('languages'))
    cursor.execute(query, (data['code'], data['name'], data['is_default'], data['order'], data['added'], data['is_active']))
    connection.commit()
    connection.close()

def editLanguage(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        UPDATE `{table}`
        SET
            `code` = %s,
            `name` = %s,
            `is_default` = %s,
            `order` = %s,
            `is_active` = %s
        WHERE `code` = %s
    """.format(table=db.table('languages'))
    cursor.execute(query, (data['new_code'], data['name'], data['is_default'], data['order'], data['is_active'], data['code']))
    connection.commit()
    connection.close()

def deleteLanguage(code):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        DELETE FROM `{table}`
        WHERE `code` = %s
    """.format(table=db.table('languages'))
    cursor.execute(query, (code,))
    connection.commit()
    connection.close()



#      ######     ###    ######## ########  ######    #######  ########  #### ########  ######
#     ##    ##   ## ##      ##    ##       ##    ##  ##     ## ##     ##  ##  ##       ##    ##
#     ##        ##   ##     ##    ##       ##        ##     ## ##     ##  ##  ##       ##
#     ##       ##     ##    ##    ######   ##   #### ##     ## ########   ##  ######    ######
#     ##       #########    ##    ##       ##    ##  ##     ## ##   ##    ##  ##             ##
#     ##    ## ##     ##    ##    ##       ##    ##  ##     ## ##    ##   ##  ##       ##    ##
#      ######  ##     ##    ##    ########  ######    #######  ##     ## #### ########  ######



def getCategory(category_id):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `id`,
            `parent`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('categories'))
    cursor.execute(query, (category_id))
    category_data = cursor.fetchone()
    if not category_data:
        connection.close()
        return {}
    query = """
        SELECT
            `language`,
            `name`
        FROM `{table}`
        WHERE `category_id` = %s
    """.format(table=db.table('categories_text'))
    cursor.execute(query, (category_id))
    connection.close()
    category_text_data = cursor.fetchall()
    for row in category_text_data:
        for prop in row:
            if prop == 'language': continue
            if prop not in category_data: category_data[prop] = {}
            category_data[prop][row['language']] = row[prop]
    return category_data

def getCategories(language, order_by=None, order_type=None):
    result = {}
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'parent', 'order', 'added', 'is_active', 'name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            c.`id`,
            c.`parent`,
            c.`order`,
            c.`added`,
            c.`is_active`,
            t.`name`
        FROM `{table}` c
        LEFT JOIN `{table_text}` t
            ON c.`id` = t.`category_id`
        WHERE t.`language` = %s
        {order}
    """.format(
        table=db.table('categories'),
        table_text=db.table('categories_text'),
        order=order_row
    )
    cursor.execute(query, (language))
    connection.close()
    categories = cursor.fetchall()
    if not categories: return []
    return categories

def getCategoriesSubcategories(language, parent, order_by=None, order_type=None):
    result = {}
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'parent', 'order', 'added', 'is_active', 'name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            c.`id`,
            c.`parent`,
            c.`order`,
            c.`added`,
            c.`is_active`,
            t.`name`
        FROM `{table}` c
        LEFT JOIN `{table_text}` t
            ON c.`id` = t.`category_id`
        WHERE t.`language` = %s
        {order}
    """.format(
        table=db.table('categories'),
        table_text=db.table('categories_text'),
        order=order_row
    )
    cursor.execute(query, (language))
    connection.close()
    categories_data = cursor.fetchall()
    if not categories_data: return []
    category_ids = [row['id'] for row in categories_data]
    if parent not in category_ids: return []
    subcategories = []
    subcategory_ids = [parent]
    while True:
        done_flag = True
        for row in categories_data:
            if row['id'] not in subcategory_ids and row['parent'] in subcategory_ids:
                subcategories.append(row)
                subcategory_ids.append(row['id'])
                done_flag = False
        if done_flag:
            break
    return subcategories

def getCategoryNames(language):
    db = DB()
    query = """
        SELECT
            c.`id`,
            t.`name`
        FROM `{table}` c
        RIGHT JOIN `{table_text}` t
            ON c.`id` = t.`category_id`
        WHERE t.`language` = %s
    """.format(
        table=db.table('categories'),
        table_text=db.table('categories_text')
    )
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, (language))
    connection.close()
    category_names_data = cursor.fetchall()
    return {row['id']: row['name'] for row in category_names_data} if category_names_data else {}

def addCategory(data):
    db = DB()
    query = """
        INSERT INTO `{table}` (`parent`, `order`, `added`, `is_active`)
        VALUES (%s, %s, %s, %s)
    """.format(table=db.table('categories'))
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, (data['parent'], data['order'], data['added'], data['is_active']))
    category_id = cursor.lastrowid
    for language in config.LANGUAGES:
        prop = 'name_' + language
        if prop in data:
            query = """
                INSERT INTO `{table}` (`category_id`, `language`, `name`)
                VALUES (%s, %s, %s)
            """.format(table=db.table('categories_text'))
            cursor.execute(query, (category_id, language, data[prop]))
    connection.commit()
    connection.close()

def editCategory(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        UPDATE `{table}`
        SET
            `parent` = %s,
            `order` = %s,
            `is_active` = %s
        WHERE `id` = %s
    """.format(table=db.table('categories'))
    cursor.execute(query, (data['parent'], data['order'], data['is_active'], data['id']))
    for language in config.LANGUAGES:
        prop = 'name_' + language
        if prop in data:
            query = """
                INSERT INTO `{table}` (`category_id`, `language`, `name`)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY
                UPDATE `name` = %s
            """.format(table=db.table('categories_text'))
            cursor.execute(query, (data['id'], language, data[prop], data[prop]))
    connection.commit()
    connection.close()

def deleteCategory(category_id):
    db = DB()
    query = """
        DELETE FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('categories'))
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, [category_id])
    connection.commit()
    connection.close()



#     ########  ########   #######  ########  ##     ##  ######  ########  ######
#     ##     ## ##     ## ##     ## ##     ## ##     ## ##    ##    ##    ##    ##
#     ##     ## ##     ## ##     ## ##     ## ##     ## ##          ##    ##
#     ########  ########  ##     ## ##     ## ##     ## ##          ##     ######
#     ##        ##   ##   ##     ## ##     ## ##     ## ##          ##          ##
#     ##        ##    ##  ##     ## ##     ## ##     ## ##    ##    ##    ##    ##
#     ##        ##     ##  #######  ########   #######   ######     ##     ######



def getProduct(product_id):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `id`,
            `category_id`,
            `model`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('products'))
    cursor.execute(query, (product_id))
    product_data = cursor.fetchone()
    if not product_data:
        connection.close()
        return {}
    query = """
        SELECT
            `language`,
            `name`,
            `description`
        FROM `{table}`
        WHERE `product_id` = %s
    """.format(table=db.table('products_text'))
    cursor.execute(query, (product_id))
    product_text_data = cursor.fetchall()
    for row in product_text_data:
        for prop in row:
            if prop == 'language': continue
            if prop not in product_data: product_data[prop] = {}
            product_data[prop][row['language']] = row[prop]
    query = """
        SELECT
            `currency`,
            `price`
        FROM `{table}`
        WHERE `product_id` = %s
    """.format(table=db.table('products_prices'))
    cursor.execute(query, (product_id))
    connection.close()
    product_price_data = cursor.fetchall()
    product_data['price'] = {}
    for row in product_price_data:
        product_data['price'][row['currency']] = row['price']
    return product_data

def getProducts(language, order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'category_id', 'model', 'added', 'is_active', 'name', 'description', 'category_name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            p.`id`,
            p.`category_id`,
            p.`model`,
            p.`added`,
            p.`is_active`,
            pt.`name`,
            pt.`description`,
            ct.`name` category_name
        FROM `{table}` p
        LEFT JOIN `{table_t}` pt
            ON p.`id` = pt.`product_id`
        LEFT JOIN `{table_c}` c
            ON p.`category_id` = c.`id`
        LEFT JOIN `{table_ct}` ct
            ON c.`id` = ct.`category_id`
        WHERE pt.`language` = %s
        AND ct.`language` = %s
        {order}
    """.format(
        table=db.table('products'),
        table_t=db.table('products_text'),
        table_c=db.table('categories'),
        table_ct=db.table('categories_text'),
        order=order_row
    )
    cursor.execute(query, (language, language))
    connection.close()
    products_data = cursor.fetchall()
    return products_data if products_data else []

def getCategoryProducts(language, category_id, order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'category_id', 'model', 'added', 'is_active', 'name', 'description', 'category_name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            p.`id`,
            p.`category_id`,
            p.`model`,
            p.`added`,
            p.`is_active`,
            pt.`name`,
            pt.`description`,
            ct.`name` category_name
        FROM `{table}` p
        LEFT JOIN `{table_t}` pt
            ON p.`id` = pt.`product_id`
        LEFT JOIN `{table_c}` c
            ON p.`category_id` = c.`id`
        LEFT JOIN `{table_ct}` ct
            ON c.`id` = ct.`category_id`
        WHERE p.`category_id` = %s
        AND pt.`language` = %s
        AND ct.`language` = %s
        {order}
    """.format(
        table=db.table('products'),
        table_t=db.table('products_text'),
        table_c=db.table('categories'),
        table_ct=db.table('categories_text'),
        order=order_row
    )
    cursor.execute(query, (category_id, language, language))
    connection.close()
    products_data = cursor.fetchall()
    return products_data if products_data else []

def addProduct(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        INSERT INTO `{table}` (`category_id`, `model`, `added`, `is_active`)
        VALUES (%s, %s, %s, %s)
    """.format(table=db.table('products'))
    cursor.execute(query, (data['category_id'], data['model'], data['added'], data['is_active']))
    product_id = cursor.lastrowid
    for language in config.LANGUAGES:
        prop_name = 'name_' + language
        prop_description = 'description_' + language
        if prop_name in data and prop_description in data:
            query = """
                INSERT INTO `{table}` (`product_id`, `language`, `name`, `description`)
                VALUES (%s, %s, %s, %s)
            """.format(table=db.table('products_text'))
            cursor.execute(query, (product_id, language, data[prop_name], data[prop_description]))
    for currency in config.CURRENCIES:
        prop_price = 'price_' + currency
        if prop_price in data:
            query = """
                INSERT INTO `{table}` (`product_id`, `currency`, `price`)
                VALUES (%s, %s, %s)
            """.format(table=db.table('products_prices'))
            cursor.execute(query, (product_id, currency, data[prop_price]))
    connection.commit()
    connection.close()



#      ######  ##     ##    ###    ########     ###     ######  ######## ######## ########  ####  ######  ######## ####  ######   ######
#     ##    ## ##     ##   ## ##   ##     ##   ## ##   ##    ##    ##    ##       ##     ##  ##  ##    ##    ##     ##  ##    ## ##    ##
#     ##       ##     ##  ##   ##  ##     ##  ##   ##  ##          ##    ##       ##     ##  ##  ##          ##     ##  ##       ##
#     ##       ######### ##     ## ########  ##     ## ##          ##    ######   ########   ##   ######     ##     ##  ##        ######
#     ##       ##     ## ######### ##   ##   ######### ##          ##    ##       ##   ##    ##        ##    ##     ##  ##             ##
#     ##    ## ##     ## ##     ## ##    ##  ##     ## ##    ##    ##    ##       ##    ##   ##  ##    ##    ##     ##  ##    ## ##    ##
#      ######  ##     ## ##     ## ##     ## ##     ##  ######     ##    ######## ##     ## ####  ######     ##    ####  ######   ######



def getCharacteristic(characteristic_id):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `id`,
            `order`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('characteristics'))
    cursor.execute(query, (characteristic_id))
    characteristic_data = cursor.fetchone()
    if not characteristic_data:
        connection.close()
        return {}
    query = """
        SELECT
            `language`,
            `name`
        FROM `{table}`
        WHERE `characteristic_id` = %s
    """.format(table=db.table('characteristics_text'))
    cursor.execute(query, (characteristic_id))
    connection.close()
    characteristic_text_data = cursor.fetchall()
    for row in characteristic_text_data:
        for prop in row:
            if prop == 'language': continue
            if prop not in characteristic_data: characteristic_data[prop] = {}
            characteristic_data[prop][row['language']] = row[prop]
    return characteristic_data

def getCharacteristics(language, order_by=None, order_type=None):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    order_row = ''
    if order_by and order_by in ('id', 'order', 'added', 'is_active', 'name'):
        order_row = 'ORDER BY `{column}`'.format(column=order_by)
        if order_type and order_type in ('asc', 'desc'): order_row += ' ' + order_type.upper()
    query = """
        SELECT
            c.`id`,
            c.`order`,
            c.`added`,
            c.`is_active`,
            ct.`name`
        FROM `{table}` c
        LEFT JOIN `{table_t}` ct
            ON c.`id` = ct.`characteristic_id`
        WHERE ct.`language` = %s
        {order}
    """.format(
        table=db.table('characteristics'),
        table_t=db.table('characteristics_text'),
        order=order_row
    )
    cursor.execute(query, (language))
    connection.close()
    characteristics = cursor.fetchall()
    if not characteristics: return []
    return characteristics

def addCharacteristic(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        INSERT INTO `{table}` (`order`, `added`, `is_active`)
        VALUES (%s, %s, %s)
    """.format(table=db.table('characteristics'))
    cursor.execute(query, (data['order'], data['added'], data['is_active']))
    characteristic_id = cursor.lastrowid
    for language in config.LANGUAGES:
        prop_name = 'name_' + language
        if prop_name in data:
            query = """
                INSERT INTO `{table}` (`characteristic_id`, `language`, `name`)
                VALUES (%s, %s, %s)
            """.format(table=db.table('characteristics_text'))
            cursor.execute(query, (characteristic_id, language, data[prop_name]))
    connection.commit()
    connection.close()

def editCharacteristic(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        UPDATE `{table}`
        SET
            `order` = %s,
            `is_active` = %s
        WHERE `id` = %s
    """.format(table=db.table('characteristics'))
    cursor.execute(query, (data['order'], data['is_active'], data['id']))
    for language in config.LANGUAGES:
        prop_name = 'name_' + language
        if prop_name in data:
            query = """
                INSERT INTO `{table}` (`characteristic_id`, `language`, `name`)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY
                UPDATE `name` = %s
            """.format(table=db.table('characteristics_text'))
            cursor.execute(query, (data['id'], language, data[prop_name], data[prop_name]))
    connection.commit()
    connection.close()

def deleteCharacteristic(characteristic_id):
    db = DB()
    query = """
        DELETE FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('characteristics'))
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, (characteristic_id,))
    connection.commit()
    connection.close()



#     ##     ##  ######  ######## ########   ######
#     ##     ## ##    ## ##       ##     ## ##    ##
#     ##     ## ##       ##       ##     ## ##
#     ##     ##  ######  ######   ########   ######
#     ##     ##       ## ##       ##   ##         ##
#     ##     ## ##    ## ##       ##    ##  ##    ##
#      #######   ######  ######## ##     ##  ######



def getUsers():
    db = DB()
    query = """
        SELECT
            `id`,
            `group_id`,
            `first_name`,
            `last_name`,
            `patronymic`,
            `added`,
            `is_active`
        FROM `{table}`
    """.format(table=db.table('users'))
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    users_data = cursor.fetchall()
    if not users_data:
        connection.close()
        return []
    user_ids = []
    users = {}
    for row in users_data:
        user_ids.append(row['id'])
        users[row['id']] = {
            'id': row['id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'patronymic': row['patronymic'],
            'group_id': row['group_id'],
            'group': config.USERS_GROUPS.get(row['group_id'], ''),
            'emails': [],
            'phone_numbers': [],
            'added': row['added'].strftime('%d-%m-%Y %H:%M:%S'),
            'is_active': row['is_active'] == 'Y'
        }
    query = """
        SELECT
            `user_id`,
            `email`
        FROM `{table}`
        WHERE `user_id` IN %s
    """.format(table=db.table('users_emails'))
    cursor.execute(query, [user_ids])
    user_emails_data = cursor.fetchall()
    query = """
        SELECT
            `user_id`,
            `phone_number`
        FROM `{table}`
        WHERE `user_id` IN %s
    """.format(table=db.table('users_phone_numbers'))
    cursor.execute(query, [user_ids])
    user_phone_numbers_data = cursor.fetchall()
    connection.close()
    for row in user_emails_data:
        if row['user_id'] in users:
            users[row['user_id']]['emails'].append(row['email'])
    for row in user_phone_numbers_data:
        if row['user_id'] in users:
            users[row['user_id']]['phone_numbers'].append(row['phone_number'])
    return users

def getUser(user_id):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    query = """
        SELECT
            `id`,
            `group_id`,
            `first_name`,
            `last_name`,
            `patronymic`,
            `added`,
            `is_active`
        FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('users'))
    cursor.execute(query, (user_id,))
    user_data = cursor.fetchone()
    if not user_data:
        connection.close()
        return False
    query = """
        SELECT `phone_number`
        FROM `{table}`
        WHERE `user_id` = %s
    """.format(table=db.table('users_phone_numbers'))
    cursor.execute(query, (user_id,))
    user_phone_numbers_data = cursor.fetchall()
    query = """
        SELECT `email`
        FROM `{table}`
        WHERE `user_id` = %s
    """.format(table=db.table('users_emails'))
    cursor.execute(query, (user_id,))
    user_emails_data = cursor.fetchall()
    connection.close()
    user = {}
    for prop in user_data:
        user[prop] = user_data[prop] if user_data[prop] is not None else ''
    if user_phone_numbers_data:
        user['phone_numbers'] = []
        for row in user_phone_numbers_data:
            user['phone_numbers'].append(row['phone_number'])
    if user_emails_data:
        user['emails'] = []
        for row in user_emails_data:
            user['emails'].append(row['email'])
    return user

def addUser(data):
    db = DB()
    users_fields = ('group_id', 'added', 'is_active', 'first_name', 'patronymic', 'last_name')
    fields = []
    values = []
    for field in users_fields:
        if field in data:
            values.append(data[field])
            fields.append('`' + field + '`')
    query = """
        INSERT INTO `{table}` ({fields})
        VALUES %s
    """.format(
        table=db.table('users'),
        fields=', '.join(fields)
    )
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, (values,))
    user_id = cursor.lastrowid
    if 'email' in data:
        query = """
            INSERT INTO `{table}` (`user_id`, `email`)
            VALUES (%s, %s)
        """.format(table=db.table('users_emails'))
        cursor.execute(query, [user_id, data['email']])
    if 'phone_number' in data:
        query = """
            INSERT INTO `{table}` (`user_id`, `phone_number`)
            VALUES (%s, %s)
        """.format(table=db.table('users_phone_numbers'))
        cursor.execute(query, [user_id, data['phone_number']])
    if 'salt' in data and 'password_hash' in data:
        query = """
            INSERT INTO `{table}` (`user_id`, `salt`, `password_hash`)
            VALUES (%s, %s, %s)
        """.format(table=db.table('users_passwords'))
        cursor.execute(query, [user_id, data['salt'], data['password_hash']])
    connection.commit()
    connection.close()

def editUser(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    if 'group_id' in data or 'is_active' in data:
        columns = []
        values = []
        if 'group_id' in data:
            columns.append('group_id')
            values.append(data['group_id'])
        if 'is_active' in data:
            columns.append('is_active')
            values.append(data['is_active'])
        values.append(data['user_id'])
        query = """
            UPDATE `{table}`
            SET {values}
            WHERE `id` = %s
        """.format(
            table=db.table('users'),
            values=', '.join('`{column}` = %s'.format(column=column) for column in columns)
        )
        cursor.execute(query, values)
        connection.commit()
    query = """
        DELETE FROM `{table}`
        WHERE `user_id` = %s
    """.format(table=db.table('users_data'))
    cursor.execute(query, [data['user_id']])
    values = []
    for prop in data:
        if prop in user_properties:
            values.append([data['user_id'], prop, data[prop]])
        if prop in user_multiproperties:
            for value in data[prop]:
                values.append([data['user_id'], user_multiproperties[prop], value])
    if values:
        query = """
            INSERT INTO `{table}` (`user_id`, `property`, `value`)
            VALUES (%s, %s, %s)
        """.format(table=db.table('users_data'))
        cursor.executemany(query, values)
        connection.commit()
    connection.close()

def deleteUser(user_id):
    db = DB()
    query = """
        DELETE FROM `{table}`
        WHERE `id` = %s
    """.format(table=db.table('users'))
    connection = db.getConnection()
    cursor = connection.cursor()
    cursor.execute(query, [user_id])
    connection.commit()
    connection.close()

def addUserPhoneNumber(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    values = [
        data['user_id'],
        'phone_number',
        data['phone_number']
    ]
    query = """
        INSERT INTO `{table}` (`user_id`, `property`, `value`)
        VALUES (%s, %s, %s)
    """.format(table=db.table('users_data'))
    cursor.execute(query, values)
    connection.commit()
    connection.close()

def addUserEmail(data):
    db = DB()
    connection = db.getConnection()
    cursor = connection.cursor()
    values = [
        data['user_id'],
        'email',
        data['email']
    ]
    query = """
        INSERT INTO `{table}` (`user_id`, `property`, `value`)
        VALUES (%s, %s, %s)
    """.format(table=db.table('users_data'))
    cursor.execute(query, values)
    connection.commit()
    connection.close()