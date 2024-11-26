from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db

app = FastAPI(
    title="Company Contacts API",
    description="Read-only API to search companies and contacts",
    version="0.1.0",
)


@app.get(
    "/companies/",
    response_model=list[schemas.CompanyResponse],
    responses={404: {"model": schemas.HTTP404Response}},
    tags=["company"],
)
def companies_list(
    query: schemas.CompanySearchQuery = Depends(), db: Session = Depends(get_db)
):
    """
    List companies based on search criteria.
    """

    companies = db.query(models.Company)

    if query.name:
        companies = companies.filter(
            func.levenshtein(models.Company.name, query.name) <= 3
        )
    if query.website:
        companies = companies.filter(models.Company.website == query.website)
    if query.country:
        companies = companies.filter(models.Company.country == query.country)

    companies = companies.offset(query.offset).limit(query.limit).all()

    if not companies:
        raise HTTPException(
            status_code=404, detail="No companies found with the given criteria"
        )

    return companies


@app.get(
    "/companies/{company_id}/",
    response_model=schemas.CompanyResponse,
    responses={404: {"model": schemas.HTTP404Response}},
    tags=["company"],
)
def company_detail(company_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a company by ID.
    """

    company = db.query(models.Company).get(company_id)

    if company is None:
        raise HTTPException(
            status_code=404, detail="Company not found with the given ID"
        )

    return company


@app.get(
    "/contacts/",
    response_model=list[schemas.ContactResponse],
    responses={404: {"model": schemas.HTTP404Response}},
    tags=["contact"],
)
def contacts_list(
    query: schemas.ContactSearchQuery = Depends(), db: Session = Depends(get_db)
):
    """
    List contacts based on search criteria.
    """

    contacts = db.query(models.Contact)

    if query.job_title:
        contacts = contacts.filter(models.Contact.job_title == query.job_title)
    if query.job_level:
        contacts = contacts.filter(models.Contact.job_level == query.job_level)
    if query.job_function:
        contacts = contacts.filter(models.Contact.job_function == query.job_function)

    contacts = contacts.offset(query.offset).limit(query.limit).all()

    if not contacts:
        raise HTTPException(
            status_code=404, detail="No contacts found with the given criteria"
        )

    return contacts


@app.get(
    "/contacts/{contact_id}/",
    response_model=schemas.ContactResponse,
    responses={404: {"model": schemas.HTTP404Response}},
    tags=["contact"],
)
def contact_detail(contact_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a contact by ID.
    """

    contact = db.query(models.Contact).get(contact_id).join(models.Contact.company)

    if contact is None:
        raise HTTPException(
            status_code=404, detail="Contact not found with the given ID"
        )

    return contact
