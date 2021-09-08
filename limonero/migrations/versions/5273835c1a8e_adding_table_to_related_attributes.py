"""adding table to related attributes

Revision ID: 5273835c1a8e
Revises: bdc227c85127
Create Date: 2017-07-05 15:38:55.267018

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5273835c1a8e'
down_revision = 'bdc227c85127'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attribute_privacy_group',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column(u'attribute_privacy',
                  sa.Column('attribute_privacy_group_id', sa.Integer(),
                            nullable=True))
    op.create_foreign_key('attribute_privacy_fk_privacy_group',
                          'attribute_privacy', 'attribute_privacy_group',
                          ['attribute_privacy_group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('attribute_privacy_fk_privacy_group',
                       'attribute_privacy', type_='foreignkey')
    op.drop_column(u'attribute_privacy', 'attribute_privacy_group_id')
    op.drop_table('attribute_privacy_group')
    # ### end Alembic commands ###
