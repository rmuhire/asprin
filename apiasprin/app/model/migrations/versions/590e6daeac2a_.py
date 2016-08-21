"""empty message

Revision ID: 590e6daeac2a
Revises: 2b239789c407
Create Date: 2016-08-18 15:16:03.984139

"""

# revision identifiers, used by Alembic.
revision = '590e6daeac2a'
down_revision = '2b239789c407'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    ### end Alembic commands ###
