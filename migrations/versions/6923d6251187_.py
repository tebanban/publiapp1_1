"""empty message

Revision ID: 6923d6251187
Revises: 6a4cdf557a26
Create Date: 2023-06-13 21:30:39.087193

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6923d6251187'
down_revision = '6a4cdf557a26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_ibfk_2', 'order', type_='foreignkey')
    op.drop_column('order', 'user_id')
    op.alter_column('role', 'name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.add_column('order', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('order_ibfk_2', 'order', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###