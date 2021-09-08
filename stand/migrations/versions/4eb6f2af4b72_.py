"""empty message

Revision ID: 4eb6f2af4b72
Revises: 881eb6755083
Create Date: 2017-10-31 13:47:46.604186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eb6f2af4b72'
down_revision = '881eb6755083'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cluster_configuration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], ['cluster.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cluster_configuration')
    ### end Alembic commands ###