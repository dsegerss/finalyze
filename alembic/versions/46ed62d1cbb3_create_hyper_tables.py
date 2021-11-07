"""create hyper-tables

Revision ID: 46ed62d1cbb3
Revises: 5c37d0058858
Create Date: 2021-11-07 22:17:12.824433

"""
from alembic import op
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

# revision identifiers, used by Alembic.
revision = "46ed62d1cbb3"
down_revision = "5c37d0058858"
branch_labels = None
depends_on = "5c37d0058858"


def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    session.execute("create extension if not exists timescaledb;")
    session.execute("select create_hypertable('priceminute', 'time');")
    session.execute("select create_hypertable('priceday', 'time');")


def downgrade():
    pass
