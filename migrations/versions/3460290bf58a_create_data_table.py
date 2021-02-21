"""create data_table

Revision ID: 3460290bf58a
Revises: 
Create Date: 2021-02-13 04:33:12.411214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3460290bf58a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_table',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('age', sa.Text(), nullable=True),
    sa.Column('tsh', sa.Text(), nullable=True),
    sa.Column('t3', sa.Text(), nullable=True),
    sa.Column('tt4', sa.Text(), nullable=True),
    sa.Column('t4u', sa.Text(), nullable=True),
    sa.Column('fti', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_table')
    # ### end Alembic commands ###