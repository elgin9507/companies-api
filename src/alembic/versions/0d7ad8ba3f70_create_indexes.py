"""Create indexes

Revision ID: 0d7ad8ba3f70
Revises: ffc3059c861d
Create Date: 2024-05-08 17:19:27.972610

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0d7ad8ba3f70"
down_revision = "ffc3059c861d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_companies_country"), "companies", ["country"], unique=False
    )
    op.create_index(op.f("ix_companies_name"), "companies", ["name"], unique=False)
    op.create_index(
        "ix_companies_name_country", "companies", ["name", "country"], unique=False
    )
    op.create_index(
        "ix_companies_name_website", "companies", ["name", "website"], unique=False
    )
    op.create_index(
        "ix_companies_name_website_country",
        "companies",
        ["name", "website", "country"],
        unique=False,
    )
    op.create_index(
        op.f("ix_companies_website"), "companies", ["website"], unique=False
    )
    op.create_index(
        "ix_companies_website_country",
        "companies",
        ["website", "country"],
        unique=False,
    )
    op.create_index(
        op.f("ix_contacts_job_function"), "contacts", ["job_function"], unique=False
    )
    op.create_index(
        op.f("ix_contacts_job_level"), "contacts", ["job_level"], unique=False
    )
    op.create_index(
        "ix_contacts_job_level_job_function",
        "contacts",
        ["job_level", "job_function"],
        unique=False,
    )
    op.create_index(
        op.f("ix_contacts_job_title"), "contacts", ["job_title"], unique=False
    )
    op.create_index(
        "ix_contacts_job_title_job_function",
        "contacts",
        ["job_title", "job_function"],
        unique=False,
    )
    op.create_index(
        "ix_contacts_job_title_job_level",
        "contacts",
        ["job_title", "job_level"],
        unique=False,
    )
    op.create_index(
        "ix_contacts_job_title_job_level_job_function",
        "contacts",
        ["job_title", "job_level", "job_function"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_contacts_job_title_job_level_job_function", table_name="contacts")
    op.drop_index("ix_contacts_job_title_job_level", table_name="contacts")
    op.drop_index("ix_contacts_job_title_job_function", table_name="contacts")
    op.drop_index(op.f("ix_contacts_job_title"), table_name="contacts")
    op.drop_index("ix_contacts_job_level_job_function", table_name="contacts")
    op.drop_index(op.f("ix_contacts_job_level"), table_name="contacts")
    op.drop_index(op.f("ix_contacts_job_function"), table_name="contacts")
    op.drop_index("ix_companies_website_country", table_name="companies")
    op.drop_index(op.f("ix_companies_website"), table_name="companies")
    op.drop_index("ix_companies_name_website_country", table_name="companies")
    op.drop_index("ix_companies_name_website", table_name="companies")
    op.drop_index("ix_companies_name_country", table_name="companies")
    op.drop_index(op.f("ix_companies_name"), table_name="companies")
    op.drop_index(op.f("ix_companies_country"), table_name="companies")
    # ### end Alembic commands ###
