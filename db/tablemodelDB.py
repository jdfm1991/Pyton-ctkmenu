from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AuthUser(Base):
    __tablename__ = "auth_user"
    id    = Column(Integer, primary_key=True, autoincrement=True)
    userBD  = Column(String(30))
    passw = Column(String(150))
    
    def __repr__(self):
        return f"User(id={self.id}, userBD={self.userBD}, passw={self.passw})"
    

    