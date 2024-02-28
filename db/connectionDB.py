import sqlalchemy as db

class ConnectionDB():
    def __init__(self):
        self.engine = db.create_engine("mysql+pymysql://sa:GconfiSql.2022..@localhost/catalogo", echo=True, future=True)
        super().__init__()
        