"""empty message

Revision ID: d9e7065a18bb
Revises: 0360b335305b
Create Date: 2018-10-18 19:49:51.700003

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd9e7065a18bb'
down_revision = '0360b335305b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('axf_order', sa.Column('o_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('axf_order_ibfk_1', 'axf_order', type_='foreignkey')
    op.create_foreign_key(None, 'axf_order', 'axf_user', ['o_user_id'], ['id'])
    op.drop_column('axf_order', 'o_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('axf_order', sa.Column('o_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'axf_order', type_='foreignkey')
    op.create_foreign_key('axf_order_ibfk_1', 'axf_order', 'axf_user', ['o_user'], ['id'])
    op.drop_column('axf_order', 'o_user_id')
    # ### end Alembic commands ###
