from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column('id', Integer, primary_key= True)
    name = Column('name', String(50))
    lastname = Column('lastname', String(50))
    course = Column('course', String)

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()

person1 = Person(name = "Иван", lastname = 'Иванов', course = 'Python для новичком')

session.add(person1)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(f"{person.name} {person.lastname}, курс: {person.course}")