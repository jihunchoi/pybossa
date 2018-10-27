"""Add user and accessible project relationship

Revision ID: 20eddf9fcc78
Revises: 4da122b13d81
Create Date: 2018-10-27 16:37:07.929843

"""

# revision identifiers, used by Alembic.
revision = '20eddf9fcc78'
down_revision = '4da122b13d81'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user_accessible_project_association',
        sa.Column('user_id', sa.Integer,
                  sa.ForeignKey('user.id', ondelete='CASCADE')),
        sa.Column('project_id', sa.Integer,
                  sa.ForeignKey('project.id', ondelete='CASCADE'))
    )


def downgrade():
    op.drop_table('user_accessible_project_association')
