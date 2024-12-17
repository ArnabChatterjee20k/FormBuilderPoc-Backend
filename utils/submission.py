from db import FormSubmission
from sqlalchemy.orm import Session
from sqlalchemy import select
from schema import Submission
class SubmissionRepo:
    def __init__(self,session:Session):
        self.session = session

    def submit(self,submission,form_id,user_id):
        data = FormSubmission(form_id=form_id,submission_data=submission)
        return data.id

    def get_pages(self,form_id):
        """For data visualisation"""
        pass

    def update_form():
        pass

    def delete_form():
        pass