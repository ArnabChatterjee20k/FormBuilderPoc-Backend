from schema import Pages, Field, Form, Page
from pydantic import ValidationError
from utils.pages import PagesRepo
from utils.form import FormRepo
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
    "options":["sdlfjds","lsdjfl"],
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

pages = {"pages":[page1,page2]}

if create_db():
    pass
else:
    raise Exception("Not working")

with Session() as session:
    try:
        form = FormRepo(session)
        page = PagesRepo(session)
        f_id = form.create_form("arnab","data")
        pages = Pages(**pages).model_dump(mode="python")
        page.create_pages(pages["pages"],f_id)
        session.commit()
    except ValidationError as e:
        print(e.json())
        for err in e.errors():
            print(f"Field: {err['loc']}, Error: {err['msg']}, Type: {err['type']}")
