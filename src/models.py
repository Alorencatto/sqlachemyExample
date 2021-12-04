from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship,registry

# from fastapiDdatabase.src.database import Base
from src.database import Base


# mapper_registry = registry()

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    __table_args__ = {'extend_existing': True}


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# #TODO Problema é aqui, não está funcionando
# # @mapper_registry.as_declarative_base()
# # @mapper_registry.mapped
class Token(Base):
    __tablename__ = "tokens"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)

#Não implementado ainda
class Teste(Base):
    __tablename__ = "teste"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)



# if __name__ == '__main__':
#     print("Ola")
