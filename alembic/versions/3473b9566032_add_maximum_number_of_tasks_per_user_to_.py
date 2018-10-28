"""Add maximum number of tasks per user to project

Revision ID: 3473b9566032
Revises: 20eddf9fcc78
Create Date: 2018-10-28 13:39:28.542709

"""

# revision identifiers, used by Alembic.
revision = '3473b9566032'
down_revision = '20eddf9fcc78'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('project', sa.Column('n_allowed_tasks', sa.Integer, default=0))
    query = 'UPDATE "project" SET n_allowed_tasks=0;'
    op.execute(query)


def downgrade():
    op.drop_column('project', 'n_allowed_tasks')
