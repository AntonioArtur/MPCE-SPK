"""mpce

Revision ID: 2a5d4a1d87fb
Revises: 6f7a506d4afb
Create Date: 2021-06-21 11:45:37.579605

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column, text
import json

 
# revision identifiers, used by Alembic.
revision = '2a5d4a1d87fb'
down_revision = '6f7a506d4afb'
branch_labels = None
depends_on = None

def _insert_operation_category():
    operation_category_table = table('operation_category',
                                     column("id", Integer),
                                     column('type', String),
                                     column("order", Integer),
                                     column("default_order", Integer)
                                     )
    columns = ['id', 'type', 'order', 'default_order']
    all_categories = [
        (9501, 'group', 0, 0),
    ]
    rows = [dict(list(zip(columns, cat))) for cat in all_categories]

    op.bulk_insert(operation_category_table, rows)

def _insert_operation_category_translation():
    tb = table(
        'operation_category_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (9501, 'en', 'Speech Analytics'),
        (9501, 'pt', 'Análise de Voz'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation():
    tb = table('operation',
               column("id", Integer),
               column("slug", String),
               column('enabled', Integer),
               column('type', String),
               column('icon', String),
               )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    data = [
        (9500, 'read-embedded-folder', 1, 'TRANSFORMATION', 'fa-filter'),
        (9501, 'read-audio-folder', 1, 'TRANSFORMATION', 'fa-filter'),
        (9502, 'extract-audio-features', 1, 'TRANSFORMATION', 'fa-filter'),
        (9503, 'search-database', 1, 'TRANSFORMATION', 'fa-filter'),
        (9504, 'process', 1, 'TRANSFORMATION', 'fa-filter'),
        (9505, 'denoise', 1, 'TRANSFORMATION', 'fa-filter'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (9500, 4),
        (9501, 4), 
        (9502, 4),
        (9503, 4),
        (9504, 4),
        (9505, 4),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (9500, 9501),
        (9501, 9501),
        (9502, 9501),
        (9503, 9501),
        (9504, 9501),
        (9505, 9501),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (9500, 'en', 'Read Embedded Folder',
         'List all embeddings inside the folder.'),
        (9500, 'pt', 'Ler Pasta de Embeddings',
         'Lista todas os embeddings contidas na pasta.'),
        (9501, 'en', 'Read Audio Folder',
         'List all audios inside the folder.'),
        (9501, 'pt', 'Ler Pasta de Áudio',
         'Lista todas os áudios contidas na pasta.'),
        (9502, 'en', 'Extract speaker features',
         'Extract audio features.'),
        (9502, 'pt', 'Extrair características do interlocutor',
         'Extrair características dos interlocutores.'),
        (9503, 'en', 'Search in database',
         'Search for speaker in database.'),
        (9503, 'pt', 'Procurar no banco de dados',
         'Procurar interlocutor no banco de dados.'),
        (9504, 'en', 'Preprocess',
         'Preprocessment of audio.'),
        (9504, 'pt', 'Pré-Processar',
         'Pŕe-processamento do áudio.'),
        (9505, 'en', 'Denoise',
         'Denoises the audio.'),
        (9505, 'pt', 'Remover Ruído',
         'Remove ruído do áudio.')
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)    

def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (9500, 1, 1, 'execution'), 
        (9501, 1, 1, 'execution'), #Form's ID = Operation ID
        (9502, 1, 1, 'execution'), #Form's ID = Operation ID
        (9503, 1, 1, 'execution'), #Form's ID = Operation ID
        (9504, 1, 1, 'execution'), #Form's ID = Operation ID
        (9505, 1, 1, 'execution'), #Form's ID = Operation ID
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(operation_form_table, rows)

def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (9500, 'en', 'Execution'), #Form ID
        (9500, 'pt', 'Execução'), #Form ID
        (9501, 'en', 'Execution'), #Form ID
        (9501, 'pt', 'Execução'), #Form ID
        (9502, 'en', 'Execution'), #Form ID
        (9502, 'pt', 'Execução'), #Form ID
        (9503, 'en', 'Execution'), #Form ID
        (9503, 'pt', 'Execução'), #Form ID
        (9504, 'en', 'Execution'), #Form ID
        (9504, 'pt', 'Execução'), #Form ID
        (9505, 'en', 'Execution'), #Form ID
        (9505, 'pt', 'Execução'), #Form ID
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (9500, 41),   # Appearance
        (9500, 9501), #Own Execution Form
        (9500, 110), #Results
        (9501, 41),   # Appearance
        (9501, 9501), #Own Execution Form
        (9501, 110), #Results
        (9502, 41),   # Appearance
        (9502, 9502), #Own Execution Form
        (9502, 110), #Results
        (9503, 41),   # Appearance
        (9503, 9503), #Own Execution Form
        (9503, 110), #Results
        (9504, 41),   # Appearance
        (9504, 9504), #Own Execution Form
        (9504, 110), #Results
        (9505, 41),   # Appearance
        (9505, 9505), #Own Execution Form
        (9505, 110), #Results
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('order', Integer),
        column('multiplicity', String),
        column('operation_id', Integer),
        column('slug', String),)

    columns = ('id', 'type', 'tags', 'order', 'multiplicity', 'operation_id', 'slug')
    data = [
        (9501, 'OUTPUT', '', 1, 'ONE', 9500, 'output data'),
        (9502, 'OUTPUT', '', 1, 'ONE', 9501, 'output data'),
        (9503, 'INPUT', '', 1, 'ONE', 9502, 'input data'),
        (9504, 'OUTPUT', '', 1, 'ONE', 9502, 'output data'),
        (9505, 'INPUT', '', 1, 'ONE', 9503, 'query data'),
        (9506, 'INPUT', '', 2, 'ONE', 9503, 'database data'),
        (9507, 'OUTPUT', '', 1, 'ONE', 9503, 'output data'),
        (9508, 'INPUT', '', 1, 'ONE', 9504, 'input data'),
        (9509, 'OUTPUT', '', 1, 'ONE', 9504, 'output data'),
        (9510, 'INPUT', '', 1, 'ONE', 9505, 'input data'),
        (9511, 'OUTPUT', '', 1, 'ONE', 9505, 'output data'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (9501, "en", 'output data', 'Output data'),
        (9501, "pt", 'dados de saída', 'Dados de saída'),
        (9502, "en", 'output data', 'Output data'),
        (9502, "pt", 'dados de saída', 'Dados de saída'),
        (9503, "en", 'input data', 'Input data'),
        (9503, "pt", 'dados de entrada', 'Dados de entrada'),
        (9504, "en", 'output data', 'Output data'),
        (9504, "pt", 'dados de saída', 'Dados de saída'),
        (9505, "en", 'query data', 'Input data'),
        (9505, "pt", 'dados para procura', 'Dados de entrada'),
        (9506, "en", 'database', 'Input data'),
        (9506, "pt", 'banco de dados', 'Dados de entrada'),
        (9507, "en", 'output data', 'Output data'),
        (9507, "pt", 'dados de saída', 'Dados de saída'),
        (9508, "en", 'input data', 'Input data'),
        (9508, "pt", 'dados de entrada', 'Dados de entrada'),
        (9509, "en", 'output data', 'Output data'),
        (9509, "pt", 'dados de saída', 'Dados de saída'),
        (9510, "en", 'input data', 'Input data'),
        (9510, "pt", 'dados de entrada', 'Dados de entrada'),
        (9511, "en", 'output data', 'Output data'),
        (9511, "pt", 'dados de saída', 'Dados de saída'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (9501, 1),
        (9502, 1),
        (9503, 1),
        (9504, 1),
        (9505, 1),
        (9506, 1),
        (9507, 1),
        (9508, 1),
        (9509, 1),
        (9510, 1),
        (9511, 1),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_form_field():
    tb = table(
        'operation_form_field',
        column('id', Integer),
        column('name', String),
        column('type', String),
        column('required', Integer),
        column('order', Integer),
        column('default', Text),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer),
        column('enable_conditions', String),
    )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id',
               'enable_conditions')

    data = [
        #Flatten - data_format
        (9500, 'folder_name', 'TEXT', 1, 1, 'folder_name', 'text', None, None, 'EXECUTION', 9500, None),
        (9501, 'folder_name', 'TEXT', 1, 1, 'folder_name', 'text', None, None, 'EXECUTION', 9501, None),
        (9502, 'folder_name', 'TEXT', 1, 1, 'folder_name', 'text', None, None, 'EXECUTION', 9502, None),
        (9503, 'group', 'INTEGER', 1, 1, 0, 'checkbox', None, None, 'EXECUTION', 9503, None),
        (9504, 'resample', 'INTEGER', 1, 1, 1, 'checkbox', None, None, 'EXECUTION', 9504, None),
        (9505, 'mono', 'INTEGER', 1, 1, 1, 'checkbox', None, None, 'EXECUTION', 9504, None),
        (9506, 'convert', 'INTEGER', 1, 1, 1, 'checkbox', None, None, 'EXECUTION', 9504, None),
     ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        (9500, 'en', 'Folder Name', 'Folder Name.'),
        (9500, 'pt', 'Nome da Pasta', 'Nome da Pasta.'),
        (9501, 'en', 'Folder Name', 'Folder Name.'),
        (9501, 'pt', 'Nome da Pasta', 'Nome da Pasta.'),
        (9502, 'en', 'Folder Name', 'Folder Name.'),
        (9502, 'pt', 'Nome da Pasta', 'Nome da Pasta.'),
        (9503, 'en', 'Group search', 'Group search.'),
        (9503, 'pt', 'Pesquisar grupo', 'Pesquisar grupo.'),
        (9504, 'en', 'Resample', 'Change sample rate.'),
        (9504, 'pt', 'Resample', 'Mudar sample rate.'),
        (9505, 'en', 'Mono', 'Set the audio with one channel.'),
        (9505, 'pt', 'Mono', 'Converter áudio para mono.'),
        (9506, 'en', 'Convert', 'Convert audio to wav format.'),
        (9506, 'pt', 'Converter', 'Converter áudio para formato wav.'),
    ]

    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)

all_commands = [
    (_insert_operation_category,
     'DELETE FROM operation_category WHERE id IN (4003)'),
    (_insert_operation_category_translation,
     'DELETE FROM operation_category_translation WHERE id IN (4003)'),
    (_insert_operation, 'DELETE FROM operation WHERE id >= 9001'),
    (_insert_operation_platform,
     'DELETE FROM operation_platform WHERE operation_id >= 9001'),
    (_insert_operation_category_operation,
     'DELETE FROM operation_category_operation WHERE operation_id >= 9001'),
    (_insert_operation_form, 'DELETE FROM operation_form WHERE id >= 9001'),
    (_insert_operation_form_translation,
     'DELETE FROM operation_form_translation WHERE id >= 9001'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id >= 9001'),
    (_insert_operation_translation,
     'DELETE FROM operation_translation WHERE id >= 9001'),
    (_insert_operation_port, 'DELETE FROM operation_port WHERE id >= 9001'),
    (_insert_operation_port_translation,
     'DELETE FROM operation_port_translation WHERE id >= 9001'),
    (_insert_operation_port_interface_operation_port,
     'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id >= 9001'),
    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id >= 4373'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id >= 4373')
]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()