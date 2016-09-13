"""empty message

Revision ID: 03798c930e68
Revises: None
Create Date: 2016-09-13 11:40:37.184407

"""

# revision identifiers, used by Alembic.
revision = '03798c930e68'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('lat', sa.String(length=100), nullable=True),
    sa.Column('lon', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('web', sa.String(length=80), nullable=True),
    sa.Column('logo', sa.String(length=80), nullable=True),
    sa.Column('regDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('business_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('paper_size',
    sa.Column('size_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('size', sa.String(length=30), nullable=True),
    sa.Column('size_type', sa.String(length=30), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('size_id')
    )
    op.create_table('paper_type',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('color', sa.String(length=40), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('characteristics', sa.Text(), nullable=True),
    sa.Column('uses', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('type_id')
    )
    op.create_table('printer',
    sa.Column('printer_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('uri', sa.String(length=220), nullable=True),
    sa.Column('regDate', sa.DateTime(), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.business_id'], ),
    sa.PrimaryKeyConstraint('printer_id'),
    sa.UniqueConstraint('uri')
    )
    op.create_table('tonner',
    sa.Column('tonner_id', sa.Integer(), nullable=False),
    sa.Column('regDate', sa.DateTime(), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.business_id'], ),
    sa.PrimaryKeyConstraint('tonner_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('names', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.Column('user_type', sa.Integer(), nullable=True),
    sa.Column('regDate', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.business_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('printer_job',
    sa.Column('printer_job_id', sa.Integer(), nullable=False),
    sa.Column('tonner_cost', sa.Float(), nullable=True),
    sa.Column('file', sa.String(length=50), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('page_number', sa.Integer(), nullable=True),
    sa.Column('cyan', sa.Float(), nullable=True),
    sa.Column('magenta', sa.Float(), nullable=True),
    sa.Column('yellow', sa.Float(), nullable=True),
    sa.Column('black', sa.Float(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('paper_price', sa.Float(), nullable=True),
    sa.Column('taxes', sa.Float(), nullable=True),
    sa.Column('regDate', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.Column('paper_type_id', sa.Integer(), nullable=True),
    sa.Column('paper_size_id', sa.Integer(), nullable=True),
    sa.Column('tonner_id', sa.Integer(), nullable=True),
    sa.Column('printer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.business_id'], ),
    sa.ForeignKeyConstraint(['paper_size_id'], ['paper_size.size_id'], ),
    sa.ForeignKeyConstraint(['paper_type_id'], ['paper_type.type_id'], ),
    sa.ForeignKeyConstraint(['printer_id'], ['printer.printer_id'], ),
    sa.ForeignKeyConstraint(['tonner_id'], ['tonner.tonner_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('printer_job_id')
    )
    op.create_table('tonner_list',
    sa.Column('tonner_list_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('color', sa.String(length=15), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('tonner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tonner_id'], ['tonner.tonner_id'], ),
    sa.PrimaryKeyConstraint('tonner_list_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tonner_list')
    op.drop_table('printer_job')
    op.drop_table('user')
    op.drop_table('tonner')
    op.drop_table('printer')
    op.drop_table('paper_type')
    op.drop_table('paper_size')
    op.drop_table('business')
    ### end Alembic commands ###
