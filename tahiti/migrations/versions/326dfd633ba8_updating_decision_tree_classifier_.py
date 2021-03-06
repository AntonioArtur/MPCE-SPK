# -*- coding: utf-8 -*-

"""Updating Decision Tree Classifier (scikit_learn).

Revision ID: 326dfd633ba8
Revises: 529bd5bd009e
Create Date: 2019-11-28 17:27:00.525928

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
revision = '326dfd633ba8'
down_revision = '529bd5bd009e'
branch_labels = None
depends_on = None


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        #Flatten - data_format
        (4024, 41),  #appearance
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
        (4224, 'criterion', 'TEXT', 0, 6, 'gini', 'dropdown', None,
         json.dumps([
             {'key': 'gini', 'value': 'gini'},
             {'key': 'entropy', 'value': 'entropy'},
         ]),
         'EXECUTION', 4004, None),
        (4225, 'splitter', 'TEXT', 0, 7, 'best', 'dropdown', None,
         json.dumps([
             {'key': 'best', 'value': 'best'},
             {'key': 'random', 'value': 'random'},
         ]),
         'EXECUTION', 4004, None),
        (4226, 'max_features', 'TEXT', 0, 8, None, 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'sqrt', 'value': 'sqrt'},
             {'key': 'log2', 'value': 'log2'},
         ]),
         'EXECUTION', 4004, None),
        (4227, 'max_leaf_nodes', 'INTEGER', 0, 9, None, 'integer', None, None, 'EXECUTION', 4004, None),
        (4228, 'min_impurity_decrease', 'DECIMAL', 0, 10, 0, 'decimal', None, None, 'EXECUTION', 4004, None),
        (4229, 'class_weight', 'TEXT', 0, 11, None, 'text', None, None, 'EXECUTION', 4004, None),
        (4230, 'presort', 'INTEGER', 0, 12, 0, 'checkbox', None, None, 'EXECUTION', 4004, None),
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
        #Flatten - data_format
        (4224, 'en', 'Criterion', 'The function to measure the quality of a split.'),
        (4224, 'pt', 'Crit??rio', 'A fun????o para medir a qualidade de uma divis??o.'),

        (4225, 'en', 'Splitter', 'The strategy used to choose the split at each node.'),
        (4225, 'pt', 'Splitter', 'A estrat??gia usada para escolher a divis??o em cada n??.'),

        (4226, 'en', 'Maximum features', 'The number of features to consider when looking for the best split.'),
        (4226, 'pt', 'Recursos m??ximos', 'O n??mero de recursos a serem considerados ao procurar a melhor divis??o.'),

        (4227, 'en', 'Maximum leaf nodes', 'Grow a tree with max_leaf_nodes in best-first fashion. Best nodes are '
                                           'defined as relative reduction in impurity. If None then unlimited number of'
                                           ' leaf nodes.'),
        (4227, 'pt', 'N??mero m??ximo de n??s folha', 'Cres??a uma ??rvore com o n??mero m??ximo de n??s folha da melhor'
                                                   ' maneira poss??vel. Os melhores n??s s??o definidos como redu????o'
                                                   ' relativa na impureza. Se nenhum, n??mero ilimitado de n??s de'
                                                   ' folha.'),

        (4228, 'en', 'Minimum impurity decrease', 'A node will be split if this split induces a decrease of the'
                                                  ' impurity greater than or equal to this value.'),
        (4228, 'pt', 'Diminui????o m??nima da impureza', 'Um n?? ser?? dividido se essa divis??o induzir uma diminui????o da'
                                                      ' impureza maior ou igual a esse valor.'),

        (4229, 'en', 'Class weight', 'Weights associated with classes in the form {class_label: weight}.'),
        (4229, 'pt', 'Peso da classe', 'Pesos associados a classes no formato {class_label: weight}.'),

        (4230, 'en', 'Presort', 'Whether to presort the data to speed up the finding of best splits in fitting.'),
        (4230, 'pt', 'Pr??-classifica????o', 'Se os dados devem ser pr??-classificados para acelerar a localiza????o das'
                                          ' melhores divis??es no ajuste.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4019""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4019"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4224 AND 4230'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4224 AND 4230'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4024 AND operation_form_id = 41'),
]


def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in all_commands:
            if isinstance(cmd[0], str):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()


def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        connection.execute('SET FOREIGN_KEY_CHECKS=0;')
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], str):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
        connection.execute('SET FOREIGN_KEY_CHECKS=1;')
    except:
        session.rollback()
        raise
    session.commit()