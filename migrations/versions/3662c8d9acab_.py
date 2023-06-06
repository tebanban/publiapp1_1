"""empty message

Revision ID: 3662c8d9acab
Revises: ba5fbead7b20
Create Date: 2023-05-23 23:16:13.557342

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3662c8d9acab'
down_revision = 'ba5fbead7b20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('contact', sa.String(length=150), nullable=False))
    op.drop_column('client', 'contact_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('contact_name', mysql.VARCHAR(length=150), nullable=False))
    op.drop_column('client', 'contact')
    # ### end Alembic commands ###