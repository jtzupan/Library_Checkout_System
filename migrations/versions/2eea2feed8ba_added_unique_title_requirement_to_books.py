"""added unique title requirement to books

Revision ID: 2eea2feed8ba
Revises: eb9cbe704aa3
Create Date: 2020-01-27 09:28:23.367713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eea2feed8ba'
down_revision = 'eb9cbe704aa3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'book', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='unique')
    # ### end Alembic commands ###
