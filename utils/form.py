from db import create_db, Form,Page,FormSubmission
from sqlalchemy.orm import Session
from sqlalchemy import select

class FormRepo:
    def __init__(self,session:Session):
        self.session = session

    def create_form(self,name,description):
        new_form = Form(name=name,description=description)
        self.session.add(new_form)
        # self.session.commit()
        # self.session.refresh(new_form)
        self.session.flush()
        return new_form.id

    def read_form(self,id):
        form = self.session.get(Form,id)
        return form

    def update_form():
        pass

    def delete_form():
        pass