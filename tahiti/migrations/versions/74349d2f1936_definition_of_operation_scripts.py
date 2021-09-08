"""Definition of operation scripts

Revision ID: 74349d2f1936
Revises: 5f6fc133361a
Create Date: 2017-06-01 16:03:16.940815

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '74349d2f1936'
down_revision = '5f6fc133361a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation_script',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('JS_CLIENT', 'PY_SERVER', name='ScriptTypeEnumType'), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('operation_ui_code')
    # ### end Alembic commands ###

    insert_data()

def insert_data():
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation_ui_code',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('type', mysql.ENUM('ATTRIBUTE_LIST'), nullable=False),
    sa.Column('value', mysql.TEXT(), nullable=False),
    sa.Column('operation_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.id'], name='operation_ui_code_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('operation_script')
    # ### end Alembic commands ###