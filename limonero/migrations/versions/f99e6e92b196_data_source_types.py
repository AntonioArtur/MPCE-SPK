"""Data source types

Revision ID: f99e6e92b196
Revises: 422f46c29791
Create Date: 2019-11-11 09:09:53.296011

"""
from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = 'f99e6e92b196'
down_revision = '422f46c29791'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('attribute_privacy_ibfk_1', 'attribute_privacy',
                       type_='foreignkey')
    op.create_foreign_key(None, 'attribute_privacy', 'attribute',
                          ['attribute_id'], ['id'], ondelete='CASCADE')
    op.get_bind().execute(text("""
        ALTER TABLE data_source
        CHANGE COLUMN `format` `format` ENUM(
            'CSV', 'CUSTOM', 'GEO_JSON', 'HAR_IMAGE_FOLDER', 'HDF5',
            'DATA_FOLDER', 'IMAGE_FOLDER', 'JDBC', 'JSON', 'NETCDF4', 'NPY',
            'PARQUET', 'PICKLE', 'SAV', 'SHAPEFILE', 'TAR_IMAGE_FOLDER', 'TEXT',
            'VIDEO_FOLDER', 'UNKNOWN', 'VALLUM', 'XML_FILE')
            CHARACTER SET 'utf8' NOT NULL ;"""))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'attribute_privacy', type_='foreignkey')
    op.create_foreign_key('attribute_privacy_ibfk_1', 'attribute_privacy',
                          'attribute', ['attribute_id'], ['id'])
    op.get_bind().execute(text("""
        ALTER TABLE data_source
        CHANGE COLUMN `format` `format` ENUM(
            'CSV', 'CUSTOM', 'GEO_JSON', 'HAR_IMAGE_FOLDER', 'HDF5',
            'DATA_FOLDER', 'IMAGE_FOLDER', 'JDBC', 'JSON', 'NETCDF4',
            'PARQUET', 'PICKLE', 'SHAPEFILE', 'TAR_IMAGE_FOLDER', 'TEXT',
            'VIDEO_FOLDER', 'UNKNOWN', 'VALLUM', 'XML_FILE')
            CHARACTER SET 'utf8' NOT NULL ;"""))
    # ### end Alembic commands ###
