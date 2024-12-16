from datetime import datetime
from sqlalchemy import create_engine,text,Integer,String,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy.orm import mapped_column,Mapped,relationship

url = ""
engine = create_engine(url)
Session = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass

class Form(Base):
    __tablename__ = 'forms'
    
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    description = mapped_column(String(500), nullable=True)
    created_at = mapped_column(DateTime, default=datetime.utcnow)
    close_date = mapped_column(DateTime, nullable=True)

    pages = relationship('Page', back_populates='form', cascade="all, delete-orphan")

    submissions = relationship('FormSubmission', back_populates='form', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Form(id={self.id}, name={self.name})>"

# Page Table
class Page(Base):
    __tablename__ = 'form-pages'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    form_id = mapped_column(Integer, ForeignKey('forms.id'), nullable=False)
    title = mapped_column(String(100), nullable=True)
    page_order = mapped_column(Integer, nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)

    form = relationship('Form', back_populates='pages')
    fields = mapped_column(JSONB, nullable=False)

    def __repr__(self):
        return f"<Page(id={self.id}, form_id={self.form_id}, title={self.title})>"

# Form Submission Table
class FormSubmission(Base):
    __tablename__ = 'form-submission'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    form_id = mapped_column(Integer, ForeignKey('forms.id'), nullable=False)
    submitted_at = mapped_column(DateTime, default=datetime.now)
    submission_data = mapped_column(JSONB, nullable=False)  # JSONB for submitted form data

    form = relationship('Form', back_populates='submissions')

    def __repr__(self):
        return f"<FormSubmission(id={self.id}, form_id={self.form_id}, submitted_at={self.submitted_at})>"

def create_db():
    Base.metadata.create_all(bind=engine)
    with engine.connect() as connection:
        data = connection.execute(text("select 1;"))
        print("Database connected")
        return True
