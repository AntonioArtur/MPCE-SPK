# -*- coding: utf-8 -*-

"""Update GBT classifier (scikit_learn).

Revision ID: 77cb7c3ffbee
Revises: 40705a398028
Create Date: 2019-12-03 08:07:42.860346

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
revision = '77cb7c3ffbee'
down_revision = '40705a398028'
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
        (4023, 41),  #appearance
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
        (4240, 'subsample', 'DECIMAL', 0, 7, 1.0, 'decimal', None,  None, 'EXECUTION', 4003, None),
        (4241, 'criterion', 'TEXT', 0, 8, 'friedman_mse', 'dropdown', None,
         json.dumps([
             {'key': 'friedman_mse', 'value': 'friedman_mse'},
             {'key': 'mse', 'value': 'mse'},
             {'key': 'mae', 'value': 'mae'},
         ]),
         'EXECUTION', 4003, None),
        (4242, 'min_weight_fraction_leaf', 'DECIMAL', 0, 9, 0, 'decimal', None,  None, 'EXECUTION', 4003, None),
        (4243, 'max_depth', 'INTEGER', 0, 10, 3, 'integer', None,  None, 'EXECUTION', 4003, None),
        (4244, 'min_impurity_decrease', 'DECIMAL', 0, 11, 0, 'decimal', None,  None, 'EXECUTION', 4003, None),
        (4245, 'init', 'TEXT', 0, 12, None, 'text', None,  None, 'EXECUTION', 4003, None),
        (4246, 'max_features', 'TEXT', 0, 13, None, 'dropdown', None,
         json.dumps([
             {'key': 'auto', 'value': 'auto'},
             {'key': 'sqrt', 'value': 'sqrt'},
             {'key': 'log2', 'value': 'log2'},
         ]),
         'EXECUTION', 4003, None),
        (4247, 'verbose', 'INTEGER', 0, 14, 0, 'integer', None,  None, 'EXECUTION', 4003, None),
        (4248, 'max_leaf_nodes', 'INTEGER', 0, 15, None, 'integer', None,  None, 'EXECUTION', 4003, None),
        (4249, 'warm_start', 'INTEGER', 0, 16, 0, 'integer', None,  None, 'EXECUTION', 4003, None),
        (4250, 'presort', 'TEXT', 0, 17, None, 'auto', None,  None, 'EXECUTION', 4003, None),
        (4251, 'validation_fraction', 'DECIMAL', 0, 18, 0.1, 'decimal', None,  None, 'EXECUTION', 4003, None),
        (4252, 'n_iter_no_change', 'INTEGER', 0, 19, None, 'integer', None,  None, 'EXECUTION', 4003, None),
        (4253, 'tol', 'DECIMAL', 0, 20, 1e-4, 'decimal', None,  None, 'EXECUTION', 4003, None),
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
        (4240, 'en', 'Subsample', 'The fraction of samples to be used for fitting the individual base learners.'),
        (4240, 'pt', 'Subamostra', 'A fra????o de amostras a serem usadas para ajustar os aprendizes da base'
                                   ' individual.'),

        (4241, 'en', 'Criterion', 'The function to measure the quality of a split.'),
        (4241, 'pt', 'Crit??rio', 'A fun????o para medir a qualidade de uma divis??o.'),

        (4242, 'en', 'Minimum weighted fraction leaf', 'The minimum weighted fraction of the sum total of weights (of '
                                                       'all the input samples) required to be at a leaf node.'),
        (4242, 'pt', 'Folha de fra????o ponderada m??nima', 'A fra????o ponderada m??nima da soma total de pesos (de todas as'
                                                         ' amostras de entrada) necess??ria para estar em um n?? folha.'),

        (4243, 'en', 'Maximum depth', 'Maximum depth of the individual regression estimators.The maximum depth limits'
                                      ' the number of nodes in the tree.'),
        (4243, 'pt', 'Profundidade m??xima', 'Profundidade m??xima dos estimadores de regress??o individuais. A'
                                            ' profundidade m??xima limita o n??mero de n??s na ??rvore.'),

        (4244, 'en', 'Minimum impurity decrease', 'A node will be split if this split induces a decrease of the'
                                                  ' impurity greater than or equal to this value.'),
        (4244, 'pt', 'Diminui????o m??nima da impureza', 'Um n?? ser?? dividido se essa divis??o induzir uma diminui????o da'
                                                      ' impureza maior ou igual a esse valor.'),

        (4245, 'en', 'Init', 'An estimator object that is used to compute the initial predictions. If ???zero???, the'
                             ' initial raw predictions are set to zero. By default, a DummyEstimator predicting the'
                             ' classes priors is used.'),
        (4245, 'pt', 'Previs??es iniciais', 'Um objeto estimador usado para calcular as previs??es iniciais. Se "zero",'
                                           ' as previs??es brutas iniciais s??o definidas como zero. Por padr??o, um'
                                           ' DummyEstimator que prev?? as classes anteriores ?? usado.'),

        (4246, 'en', 'Maximum features', 'The number of features to consider when looking for the best split.'),
        (4246, 'pt', 'Recursos m??ximos', 'O n??mero de recursos a serem considerados ao procurar a melhor divis??o.'),

        (4247, 'en', 'Verbose', 'Enable verbose output. If 1 then it prints progress and performance once in a while'
                                ' (the more trees the lower the frequency). If greater than 1 then it prints progress'
                                ' and performance for every tree.'),
        (4247, 'pt', 'Sa??da detalhada', 'Ativar sa??da detalhada. Se 1, ele imprime progresso e desempenho de vez em'
                                        ' quando (quanto mais ??rvores, menor a frequ??ncia). Se maior que 1, imprime o'
                                        ' progresso e o desempenho de todas as ??rvores.'),

        (4248, 'en', 'Maximum leaf nodes', 'Grow trees with max_leaf_nodes in best-first fashion.'),
        (4248, 'pt', 'N??mero m??ximo de n??s foliares', 'Cultive ??rvores com max_leaf_nodes da melhor maneira poss??vel.'),

        (4249, 'en', 'Warm start', 'When set to True, reuse the solution of the previous call to fit and add more'
                                   ' estimators to the ensemble, otherwise, just erase the previous solution.'),
        (4249, 'pt', 'Come??o pr??-definido', 'Quando definido como True, reutilize a solu????o da chamada anterior do fit'
                                            ' e adicione mais estimadores ao conjunto, caso contr??rio, apenas apague a'
                                            ' solu????o anterior.'),

        (4250, 'en', 'Presort', 'Whether to presort the data to speed up the finding of best splits in fitting.'),
        (4250, 'pt', 'Pr??-classifica????o', 'Se os dados devem ser pr??-classificados para acelerar a localiza????o das'
                                          ' melhores divis??es no ajuste.'),

        (4251, 'en', 'Validation fraction', 'The proportion of training data to set aside as validation set for early'
                                            ' stopping.'),
        (4251, 'pt', 'Fra????o de valida????o', 'A propor????o de dados de treinamento a serem retirados como valida????o'
                                            ' definida para parada antecipada.'),

        (4252, 'en', 'Number of iterations with no change', 'Used to decide if early stopping will be used to'
                                                            ' terminate training when validation score is not'
                                                            ' improving.'),
        (4252, 'pt', 'N??mero de itera????es sem altera????o', 'Usado para decidir se a parada precoce ser?? usada para'
                                                          ' encerrar o treinamento quando a pontua????o da valida????o n??o'
                                                          ' estiver melhorando.'),

        (4253, 'en', 'Tolerance', 'Tolerance for the early stopping.'),
        (4253, 'pt', 'Toler??ncia', 'Toler??ncia ?? parada antecipada.'),
    ]
    rows = [dict(list(zip(columns, row))) for row in data]
    op.bulk_insert(tb, rows)


all_commands = [
    ("""UPDATE operation_form_field SET `type` = 'DECIMAL' WHERE id = 4012""",
     """UPDATE operation_form_field SET `type` = 'FLOAT' WHERE id = 4012"""),

    ("""UPDATE operation_form_field SET `default` = 'prediction' WHERE id = 4107""",
     """UPDATE operation_form_field SET `default` = '' WHERE id = 4107"""),

    (_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id BETWEEN 4240 AND 4253'),
    (_insert_operation_form_field_translation,
     'DELETE FROM operation_form_field_translation WHERE id BETWEEN 4240 AND 4253'),
    (_insert_operation_operation_form,
     'DELETE FROM operation_operation_form WHERE operation_id = 4023 AND operation_form_id = 41'),
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