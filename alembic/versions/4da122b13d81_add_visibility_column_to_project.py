"""Add visibility column to project

Revision ID: 4da122b13d81
Revises: 0fe9ec33fbbd
Create Date: 2018-08-22 15:30:36.341301

"""

# revision identifiers, used by Alembic.
revision = '4da122b13d81'
down_revision = '174eb928136a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('project', sa.Column('visible', sa.Boolean, default=True))
    query = 'UPDATE "project" SET visible=true;'
    op.execute(query)


def downgrade():
    op.drop_column('project', 'visible')
