"""empty message

Revision ID: 9c90052126ec
Revises: abedd6093698
Create Date: 2019-02-11 22:55:42.281482

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9c90052126ec'
down_revision = 'abedd6093698'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('deployment', 'description',
               existing_type=mysql.VARCHAR(length=400),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('deployment', 'description',
               existing_type=mysql.VARCHAR(length=400),
               nullable=False)
    # ### end Alembic commands ###
