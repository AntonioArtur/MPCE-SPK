"""empty message

Revision ID: ed3b7980089f
Revises: a7d4e728b549
Create Date: 2017-08-18 11:39:07.745080

"""

from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column, text

# revision identifiers, used by Alembic.
revision = 'ed3b7980089f'
down_revision = 'a7d4e728b549'
branch_labels = None
depends_on = None


def insert_visualization_type():
    tb = table(
        'visualization_type',
        column('id', Integer),
        column('name', String),
        column('help', String),
        column('icon', String))

    all_ops = [
        (71, 'area-chart', 'Area Chart', 'fa-area-chart'),
        (87, 'plot-chart', 'Plot Chart', 'fa-lemon-o'),
        (88, 'map-chart', 'Map', 'fa-map-marker'),
        (89, 'donut-chart', 'Donut chart', 'fa-circle-o-notch'),
    ]
    rows = [dict(zip([c.name for c in tb.columns], operation)) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.execute(text('START TRANSACTION'))
        insert_visualization_type()
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise


# noinspection PyBroadException
def downgrade():
    try:
        op.execute(text('START TRANSACTION'))
        op.execute(text("DELETE FROM visualization_type WHERE id IN (71, 87, 88, 89)"))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
