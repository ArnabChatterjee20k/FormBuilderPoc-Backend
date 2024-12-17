from schema import Pages, Field, Form, Page, transform_to_kv,Submission,PagesDBModel
from pydantic import ValidationError
from utils.pages import PagesRepo
from utils.form import FormRepo
from utils.submission import SubmissionRepo
from db import Session
from db import create_db


page1 = {"title": "page1", "fields": [{
    "checked": True,
    "description": "You can manage your mobile notifications in the mobile settings page.",
    "disabled": False,
    "label": "Use different settings for my mobile devices",
    "name": "name_5251793821",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Checkbox"
},
    {
    "checked": True,
    "description": "This is the language that will be used in the dashboard.",
    "disabled": False,
    "label": "Language",
    "name": "name_5956971624",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Combobox"
},
    {
    "checked": True,
    "description": "Your date of birth is used to calculate your age.",
    "disabled": False,
    "label": "Date of birth",
    "name": "name_0423339215",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Date Picker"
},
    {
    "checked": True,
    "description": "Select a file to upload.",
    "disabled": False,
    "label": "Select File",
    "name": "name_2385205346",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "File Input"
},
    {
    "checked": True,
    "description": "Add the date of submission with detailly.",
    "disabled": False,
    "label": "Submission Date",
    "name": "name_9565160153",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Datetime Picker"
},
    {
    "checked": True,
    "description": "Select multiple options.",
    "disabled": False,
    "label": "Select your framework",
    "name": "name_1039175267",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Multi Select"
},
    {
    "checked": True,
    "description": "Enter your phone number.",
    "disabled": False,
    "label": "Phone number",
    "name": "name_6718092261",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Phone"
},
    {
    "checked": True,
    "description": "You can manage email addresses in your email settings.",
    "disabled": False,
    "label": "Email",
    "name": "name_7950230592",
    "placeholder": "Select a verified email to display",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Select"
},
    {
    "checked": True,
    "description": "Adjust the price by sliding.",
    "disabled": False,
    "label": "Set Price Range",
    "name": "name_9395282442",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Slider"
},
    {
    "checked": True,
    "description": "You can @mention other users and organizations.",
    "disabled": False,
    "label": "Bio",
    "name": "name_3228155921",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Textarea"
},
    {
    "checked": True,
    "description": "Add tags.",
    "disabled": False,
    "label": "Enter your tech stack.",
    "name": "name_4441468805",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Tags Input"
}
]
}

page2 = {"title": "page2", "fields": [{
    "checked": True,
    "description": "You can manage your mobile notifications in the mobile settings page.",
    "disabled": False,
    "label": "Use different settings for my mobile devices",
    "name": "name_5251793821",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Checkbox"
},
    {
    "checked": True,
    "description": "This is the language that will be used in the dashboard.",
    "disabled": False,
    "label": "Language",
    "name": "name_5956971624",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Combobox"
},
    {
    "checked": True,
    "description": "Your date of birth is used to calculate your age.",
    "disabled": False,
    "label": "Date of birth",
    "name": "name_0423339215",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Date Picker"
},
    {
    "checked": True,
    "description": "Select a file to upload.",
    "disabled": False,
    "label": "Select File",
    "name": "name_2385205346",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "File Input"
},
    {
    "checked": True,
    "description": "Add the date of submission with detailly.",
    "disabled": False,
    "label": "Submission Date",
    "name": "name_9565160153",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Datetime Picker"
},
    {
    "checked": True,
    "description": "Select multiple options.",
    "disabled": False,
    "label": "Select your framework",
    "name": "name_1039175267",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "options": ["sdlfjds", "lsdjfl"],
    "variant": "Multi Select"
},
    {
    "checked": True,
    "description": "Enter your phone number.",
    "disabled": False,
    "label": "Phone number",
    "name": "name_6718092261",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Phone"
},
    {
    "checked": True,
    "description": "You can manage email addresses in your email settings.",
    "disabled": False,
    "label": "Email",
    "name": "name_7950230592",
    "placeholder": "Select a verified email to display",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Select"
},
    {
    "checked": True,
    "description": "Adjust the price by sliding.",
    "disabled": False,
    "label": "Set Price Range",
    "name": "name_9395282442",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Slider"
},
    {
    "checked": True,
    "description": "You can @mention other users and organizations.",
    "disabled": False,
    "label": "Bio",
    "name": "name_3228155921",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Textarea"
},
    {
    "checked": True,
    "description": "Add tags.",
    "disabled": False,
    "label": "Enter your tech stack.",
    "name": "name_4441468805",
    "placeholder": "Placeholder",
    "required": True,
    "rowIndex": 0,
    "type": "",
    "value": "",
    "variant": "Tags Input"
}
]
}

# if create_db():
#     pass
# else:
#     raise Exception("Not working")


def create_form_and_save_page():
    pages = {"pages": [page1, page2]}
    with Session() as session:
        try:
            form = FormRepo(session)
            page = PagesRepo(session)
            f_id = form.create_form("arnab", "data")
            pages = Pages(**pages).model_dump(mode="python")
            for page_info in pages["pages"]:
                page_info["fields"] = transform_to_kv(page_info.get("fields"))
            page.create_pages(pages["pages"], f_id)
            session.commit()
        except ValidationError as e:
            print(e.json())
            for err in e.errors():
                print(
                    f"Field: {err['loc']}, Error: {err['msg']}, Type: {err['type']}")


def read_form():
    with Session() as session:
        f_id = 1
        form = FormRepo(session)
        form_instance = form.read_form(f_id)
        validated_data = Form.model_validate(form_instance).model_dump()
        print(validated_data)


def validate_submission():
    submission = Submission(
        formId=16,
        data={
        # Page 1
        "name_0423339215_nkcZFVNGmn": "01/01/1990",  # Date of birth
        "name_1039175267_yCZJBbnJsB": "React, Angular",  # Select your framework
        "name_2385205346_IiRksSEEDe": "file1.pdf",  # Select File
        "name_3228155921_DUcGKSBNhU": "I am a software developer passionate about coding and technology.",  # Bio
        "name_4441468805_MRbpemAynB": "JavaScript, Python, React",  # Enter your tech stack
        "name_5251793821_GMaPqIWGxr": "true",  # Use different settings for my mobile devices
        "name_5956971624_XTdKiIWMzI": "English",  # Language
        "name_6718092261_tcNJPYHwpo": "+1234567890",  # Phone number
        "name_7950230592_rQAHZUXDde": "email@example.com",  # Email
        "name_9395282442_iewlsOHGGo": "1000-5000",  # Set Price Range
        "name_9565160153_htCApDhgbc": "12/12/2024",  # Submission Date
        
        # Page 2
        "name_0423339215_rIJnfDdMSS": "01/01/1990",  # Date of birth
        "name_1039175267_GZExFyeWTz": "React, Angular",  # Select your framework (with options)
        "name_2385205346_tPonTWjHTc": "file2.pdf",  # Select File
        "name_3228155921_vCgAHtkycq": "I love working on open-source projects.",  # Bio
        "name_4441468805_WnnLfUTMXO": "Node.js, Express, MongoDB",  # Enter your tech stack
        "name_5251793821_WsfRUJGQoA": "false",  # Use different settings for my mobile devices
        "name_5956971624_KclssBzXov": "Spanish",  # Language
        "name_6718092261_WvLvvhDeAf": "+9876543210",  # Phone number
        "name_7950230592_bbwpNRUoKk": "anotheremail@example.com",  # Email
        "name_9395282442_paPJwwzpmc": "2000-8000",  # Set Price Range
        "name_9565160153_cZtAErGrJT": "15/12/2024",  # Submission Date
    }
    ).model_dump()

    with Session() as session:
        f_id = 16
        form = FormRepo(session)
        pages = Form.model_validate(form.read_form(f_id)).model_dump().get("pages")
        fields = {}
        for cur_page in pages:
            fields = {**fields,**cur_page.get("fields")}
        for i in submission["data"]:
            if i not in fields:
                print("Data validated")
                return
        # query the server for the structure of the pages and fields
        # first validate the structure and type of the submission
        # the structure and type should be validated for each fields
        # use a strategy pattern to build a list of validators
        # and call them accordinly
        # then validate the value of the submission if regex present
        repo = SubmissionRepo(session)
        # have user id here
        repo.submit(submission=submission,form_id=f_id)
        session.commit()
validate_submission()
# create_form_and_save_page()