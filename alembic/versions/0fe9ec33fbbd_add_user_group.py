"""Add user group

Revision ID: 0fe9ec33fbbd
Revises: 174eb928136a
Create Date: 2018-08-22 15:20:33.319356

"""

# revision identifiers, used by Alembic.
revision = '0fe9ec33fbbd'
down_revision = '174eb928136a'

from alembic import op
import sqlalchemy as sa


def make_timestamp():
    now = datetime.datetime.now()
    return now.isoformat()


def upgrade():
    op.create_table(
        'user_group',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=254), nullable=False),
        sa.Column('created', sa.Text, default=make_timestamp)
    )
    op.create_table(
        'user_group_association',
        sa.Column('user_id', sa.Integer,
                  sa.ForeignKey('user.id', ondelete=None)),
        sa.Column('group_id', sa.Integer,
                  sa.ForeignKey('user_group.id', ondelete=None))
    )
    op.create_table(
        'project_group_association',
        sa.Column('project_id', sa.Integer,
                  sa.ForeignKey('project.id', ondelete=None)),
        sa.Column('group_id', sa.Integer,
                  sa.ForeignKey('user_group.id', ondelete=None))
    )


def downgrade():
    op.drop_table('project_group_association')
    op.drop_table('user_group_association')
    op.drop_table('user_group')
