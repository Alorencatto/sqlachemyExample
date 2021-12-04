from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,registry,relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.ext.automap import automap_base

SQLALCHEMY_DATABASE_URL = "sqlite:///sqlite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Original
Base = declarative_base()

# Base = automap_base()


# Base.prepare(engine, reflect=True)

# User = Base.classes.users



# Usado para criar as tabelas com base nas classes
# def create_tables():
#     Base.metadata.create_all(bind=engine)
#
#
# create_tables()

if __name__ == '__main__':
    #Criando as tabelas
    # models.Base.metadata.create_all(bind=engine)
    print(Base)
    print("Ola")
