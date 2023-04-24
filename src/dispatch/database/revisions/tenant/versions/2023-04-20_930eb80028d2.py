"""Adds a thread_ts column for a signal message in a case so it can be updated by conversation plugin

Revision ID: 930eb80028d2
Revises: 56eb1c0a3a92
Create Date: 2023-04-20 16:55:33.901449

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "930eb80028d2"
down_revision = "56eb1c0a3a92"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("case", sa.Column("signal_thread_ts", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("case", "signal_thread_ts")
    # ### end Alembic commands ###