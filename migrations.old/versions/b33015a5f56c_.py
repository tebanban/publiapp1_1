"""empty message

Revision ID: b33015a5f56c
Revises: 108a98a86d56
Create Date: 2023-05-18 23:09:57.558369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b33015a5f56c'
down_revision = '108a98a86d56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('format', sa.Column('code', sa.String(length=10), nullable=True))
    op.alter_column('format', 'area',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.create_unique_constraint(None, 'format', ['code'])
    op.add_column('order', sa.Column('code', sa.String(length=15), nullable=False))
    op.create_unique_constraint(None, 'order', ['code'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order', type_='unique')
    op.drop_column('order', 'code')
    op.drop_constraint(None, 'format', type_='unique')
    op.alter_column('format', 'area',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.drop_column('format', 'code')
    # ### end Alembic commands ###