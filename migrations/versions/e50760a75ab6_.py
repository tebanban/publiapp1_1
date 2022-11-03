"""empty message

Revision ID: e50760a75ab6
Revises: d4f9fb9d138f
Create Date: 2022-11-01 20:23:40.876139

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e50760a75ab6'
down_revision = 'd4f9fb9d138f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('check_in', sa.DateTime(), nullable=True))
    op.add_column('order', sa.Column('check_out', sa.DateTime(), nullable=True))
    op.drop_column('order', 'start_rent_on')
    op.drop_column('order', 'end_rent_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('end_rent_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('order', sa.Column('start_rent_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('order', 'check_out')
    op.drop_column('order', 'check_in')
    # ### end Alembic commands ###