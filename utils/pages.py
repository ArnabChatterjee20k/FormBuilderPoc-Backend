from db import create_db, Form,Page,FormSubmission
from sqlalchemy.orm import Session
from sqlalchemy import select
from schema import Page as PageSchema
class PagesRepo:
    def __init__(self,session:Session):
        self.session = session

    def create_pages(self,pages:list[PageSchema],form_id:str):
        pages = list(map(lambda page: {**dict(page), "form_id": form_id, "page_order":1}, pages))
        self.session.bulk_insert_mappings(Page,pages)
        self.session.commit()

    def get_pages(self,form_id):
        query = select(Page).where(Page.form_id == form_id)
        result = self.session.execute(query).all()
        return [PageSchema.model_validate(page) for page in result]

    def update_form():
        pass

    def delete_form():
        pass