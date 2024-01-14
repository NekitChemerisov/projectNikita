from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import SQLAlchemyError

Base = declarative_base()
class Person(Base):
    __tablename__ = 'person'
    id = Column('id', Integer, primary_key= True)
    name = Column('name', String(50))
    lastname = Column('lastname', String(50))
    course = Column('course', String)

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()

person1 = Person(name = "Иван", lastname = 'Иванов', course = 'Python для новичком')

session.add(person1)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(f"{person.name} {person.lastname}, курс: {person.course}")


'''try:
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO person (name, lastname) VALUES (?, ?)', ('Иван', 'Иванов'))
    cursor.execute('UPDATE person SET lastname = ? WHERE name = ?', ('Сидоров', 'Иван'))

    connection.commit()

except Exception as e:
    connection.rollback()
    print(f"Произошла ошибка: {e}")

finally:
    connection.close()'''