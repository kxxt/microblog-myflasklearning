"""Post Upgrade

Revision ID: b489499a8f4a
Revises: 6b31ef18060c
Create Date: 2020-12-05 11:57:10.984370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b489499a8f4a'
down_revision = '6b31ef18060c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    # ### end Alembic commands ###
