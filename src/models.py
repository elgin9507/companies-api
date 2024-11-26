from sqlalchemy import Column, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False)
    website = Column(String, index=True)
    country = Column(String, index=True)
    contacts = relationship("Contact", back_populates="company")

    __table_args__ = (
        Index("ix_companies_name_website", "name", "website"),
        Index("ix_companies_name_country", "name", "country"),
        Index("ix_companies_website_country", "website", "country"),
        Index("ix_companies_name_website_country", "name", "website", "country"),
    )


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="contacts")
    name = Column(String, nullable=False)
    job_title = Column(String, index=True)
    job_level = Column(String, index=True)
    job_function = Column(String, index=True)

    __table_args__ = (
        Index("ix_contacts_job_title_job_level", "job_title", "job_level"),
        Index("ix_contacts_job_title_job_function", "job_title", "job_function"),
        Index("ix_contacts_job_level_job_function", "job_level", "job_function"),
        Index(
            "ix_contacts_job_title_job_level_job_function",
            "job_title",
            "job_level",
            "job_function",
        ),
    )
