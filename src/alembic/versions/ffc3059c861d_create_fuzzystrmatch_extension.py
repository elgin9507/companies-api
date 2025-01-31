"""Create fuzzystrmatch extension

Revision ID: ffc3059c861d
Revises: 028fca7d474e
Create Date: 2024-05-08 17:01:49.924298

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "ffc3059c861d"
down_revision = "028fca7d474e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE EXTENSION IF NOT EXISTS fuzzystrmatch")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP EXTENSION IF EXISTS fuzzystrmatch")
    # ### end Alembic commands ###
