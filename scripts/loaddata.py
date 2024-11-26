#!/usr/bin/env python3

import sys

sys.path = ["", ".."] + sys.path[1:]

import json
from src.models import Company, Contact
from src.database import SessionLocal

session = SessionLocal()

# Load data from JSON files
with open("data/companies.json", "r") as f:
    companies_data = json.load(f)

with open("data/contacts.json", "r") as f:
    contacts_data = json.load(f)

# Batch insert data into Company table
company_mappings = [
    {
        "id": company_data["id"],
        "name": company_data["name"],
        "website": company_data["website"],
        "country": company_data["country"],
    }
    for company_data in companies_data
]
session.bulk_insert_mappings(Company, company_mappings)

# Batch insert data into Contact table
contact_mappings = [
    {
        "id": contact_data["id"],
        "company_id": contact_data["company_id"],
        "name": contact_data["name"],
        "job_title": contact_data["job_title"],
        "job_level": contact_data["job_level"],
        "job_function": contact_data["job_function"],
    }
    for contact_data in contacts_data
]
session.bulk_insert_mappings(Contact, contact_mappings)

# Commit the changes
session.commit()
session.close()
