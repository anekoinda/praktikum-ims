import pymysql

def connect_db(db_config):
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['pass'],
        db=db_config['db_name']
    )
