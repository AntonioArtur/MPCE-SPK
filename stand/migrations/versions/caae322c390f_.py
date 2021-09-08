"""empty message

Revision ID: caae322c390f
Revises: 
Create Date: 2017-02-22 19:02:25.570381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caae322c390f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cluster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('enabled', sa.String(length=200), nullable=False),
    sa.Column('type', sa.Enum('MESOS', 'YARN', 'SPARK_LOCAL', name='ClusterTypeEnumType'), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('consumers', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cluster_access',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permission', sa.Enum('EXECUTE', name='ClusterPermissionEnumType'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], ['cluster.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('started', sa.DateTime(), nullable=True),
    sa.Column('finished', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('COMPLETED', 'RUNNING', 'INTERRUPTED', 'CANCELED', 'WAITING', 'ERROR', 'PENDING', name='StatusExecutionEnumType'), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=False),
    sa.Column('workflow_name', sa.String(length=200), nullable=False),
    sa.Column('workflow_definition', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], ['cluster.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_participant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sid', sa.String(length=200), nullable=False),
    sa.Column('join_date', sa.DateTime(), nullable=False),
    sa.Column('leave_date', sa.DateTime(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_step',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('COMPLETED', 'RUNNING', 'INTERRUPTED', 'CANCELED', 'WAITING', 'ERROR', 'PENDING', name='StatusExecutionEnumType'), nullable=False),
    sa.Column('task_id', sa.String(length=200), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.Column('operation_name', sa.String(length=200), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_step_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.String(length=200), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('step_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['step_id'], ['job_step.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_step_log')
    op.drop_table('job_step')
    op.drop_table('room_participant')
    op.drop_table('job')
    op.drop_table('cluster_access')
    op.drop_table('room')
    op.drop_table('cluster')
    ### end Alembic commands ###
