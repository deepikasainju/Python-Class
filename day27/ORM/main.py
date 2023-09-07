# ORM object relation mapping
from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base=declarative_base()

# here class student is the table modeling
class Student(Base):
    __tablename__="StudentI"
    # table create hunxa
    id=Column('id', Integer, primary_key=True)
    # primary_key=True garda indexing hunxa id ko
    name=Column("name", String)
    age=Column('age', Integer)
    gender=Column('gender', CHAR)

    def __init__(self, id, name, age, gender):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):
        return self.name
    
engine=create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()
print("Connection Established!!")

if __name__=="__main__":
    s1=Student(1, "ram", 30, "M")
    s2=Student(2, "shyam", 20, "M")
    s3=Student(3, "ham", 40, "M")
    session.add(s1)
    session.add(s2) # table ma data add gareko
    session.add(s3)
    session.commit()

