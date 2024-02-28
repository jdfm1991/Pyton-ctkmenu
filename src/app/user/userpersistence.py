from db.connectionDB import ConnectionDB
from db.tablemodelDB import AuthUser
from sqlalchemy.orm import Session

class AuthUserRp(ConnectionDB):
    
    #metodo para verificar en base de datos de el usuario ya existe antes de registrar uno nuevo    
    def getUserByName(self, user_name:str):
        user : AuthUser = None
        with Session(self.engine) as session:
            user = session.query(AuthUser).filter_by(userBD = user_name).first()
        return user
    
    #metodo para de consultar todos los datos registrado en la base de datos       
    def queryUser(self):
        user : AuthUser = None
        with Session(self.engine) as session:
            user = session.query(AuthUser).all()
        return user
    
    #metodo para buscar en base de datos los datos de un usuario registrado    
    def searchByName(self, user_s:str):
        user : AuthUser = None
        with Session(self.engine) as session:
            user = session.query(AuthUser).filter(AuthUser.userBD.like(f"%{user_s}%")).all()
            #user = print(f"{user_s}")
        return user
    
    #metodo para de registrar un nuevo usuario
    def insertUser(self, user:AuthUser):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
    
    #metodo para de eliminar un usuario registrado en la base de datos 
    def deleteUser(self, id:int):
        user : AuthUser = None
        with Session(self.engine) as session:
            session.query(AuthUser).filter_by(id = id).delete()
            session.commit()
            
    #metodo para de actualizar un usuario registrado en la base de datos         
    def uptadeUser(self, id:int, user:str, passw:str):
        user1 : AuthUser = None
        with Session(self.engine) as session:
            data = session.query(AuthUser).filter_by(id = id).first()
            data.userBD = user
            data.passw = passw
            session.add(data)
            session.commit()           
                