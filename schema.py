from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional, List, Dict,Union
from enum import Enum
import random
import string

# Enum to represent different field variants


class FieldVariant(str, Enum):
    checkbox = "Checkbox"
    combobox = "Combobox"
    date_picker = "Date Picker"
    file_input = "File Input"
    datetime_picker = "Datetime Picker"
    multi_select = "Multi Select"
    phone = "Phone"
    select = "Select"
    slider = "Slider"
    textarea = "Textarea"
    tags_input = "Tags Input"


# Pydantic model for the Field
class Field(BaseModel):
    checked: bool
    description: str
    disabled: bool
    label: str
    name: str
    placeholder: str
    required: bool
    rowIndex: int
    value: Optional[str] = None
    variant: FieldVariant
    options: Optional[List[str]] = None  # Corrected the type for options

    class Config:
        from_attributes = True

# Pydantic model for Page

class Page(BaseModel):
    title: Optional[str]
    fields: List[Field] | Dict[str,Field] # List of Field instances

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True  # This allows arbitrary types like Enum

class Pages(BaseModel):  # Changed to inherit from BaseModel
    pages: List[Page]

    class Config:
        from_attributes = True

class PagesDBModel(BaseModel):
    pages:Dict[str,Field]

    class Config:
        from_attributes = True

# Pydantic model for Form
class Form(BaseModel):  # Changed to inherit from BaseModel
    name: str
    description: Optional[str] = None  # Corrected the Optional type here
    close_date: Optional[datetime] = None  # Corrected the Optional type here
    pages: List[Page]

    class Config:
        from_attributes = True


class Submission(BaseModel):
    formId: Union[int,str]
    data: Dict[str, str]


def transform_to_kv(data):
    fields = {}
    for field in data:
        random_suffix = "".join(random.choices(string.ascii_letters, k=10))
        random_name = f"{field.get('name')}_{random_suffix}"
        fields[random_name] = field
    return fields
