'''
    Program: SqlAlchemy test class
    Author: Jhonasttan Regalado
    Copyright: 2018 
'''

from sqlalchemy import create_engine
engine = create_engine("sqlite:///some.db")


result = engine.execute("select emp_id, emp_name from "
                        "employee where emp_id =:emp_id",
                        emp_id=3)
                        
                        