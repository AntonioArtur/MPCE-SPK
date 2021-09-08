"""new features in workflow

Revision ID: 500f09c2325d
Revises: 03420d9b3079
Create Date: 2017-12-12 15:00:44.309169

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import LONGTEXT

# revision identifiers, used by Alembic.
revision = '500f09c2325d'
down_revision = '03420d9b3079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workflow_history',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('version', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('user_login', sa.String(length=50),
                              nullable=False),
                    sa.Column('user_name', sa.String(length=200),
                              nullable=False),
                    sa.Column('date', sa.DateTime(), nullable=False),
                    sa.Column('content', LONGTEXT, nullable=False),
                    sa.Column('workflow_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('workflow_permission',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('permission',
                              sa.Enum('READ', 'EXECUTE', 'WRITE',
                                      name='PermissionTypeEnumType'),
                              nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('user_login', sa.String(length=50),
                              nullable=False),
                    sa.Column('user_name', sa.String(length=200),
                              nullable=False),
                    sa.Column('workflow_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['workflow_id'], ['workflow.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column('workflow',
                  sa.Column('is_public', sa.Boolean(), nullable=False))
    op.add_column('workflow',
                  sa.Column('is_template', sa.Boolean(), nullable=False))
    op.add_column('workflow',
                  sa.Column('template_code', LONGTEXT, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workflow', 'template_code')
    op.drop_column('workflow', 'is_template')
    op.drop_column('workflow', 'is_public')
    op.drop_table('workflow_permission')
    op.drop_table('workflow_history')
    # ### end Alembic commands ###
