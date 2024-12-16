from pydantic import BaseModel,field_serializer,model_serializer
from datetime import datetime
from typing import Optional, List
from enum import Enum


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
        orm_mode = True

# Pydantic model for Page
class Page(BaseModel):
    title: Optional[str]
    fields: List[Field]  # List of Field instances

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True  # This allows arbitrary types like Enum

# Pydantic model for Pages
class Pages(BaseModel):  # Changed to inherit from BaseModel
    pages: List[Page]


# Pydantic model for Form
class Form(BaseModel):  # Changed to inherit from BaseModel
    name: str
    description: Optional[str] = None  # Corrected the Optional type here
    close_date: Optional[datetime] = None  # Corrected the Optional type here
