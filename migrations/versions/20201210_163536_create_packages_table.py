"""create packages table

Revision ID: 1afd0eb71c44
Revises: 
Create Date: 2020-12-10 16:35:36.121372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1afd0eb71c44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('packages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('recipient', sa.String(length=20), nullable=False),
    sa.Column('origin', sa.String(length=20), nullable=False),
    sa.Column('destination', sa.String(length=20), nullable=False),
    sa.Column('location', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packages')
    # ### end Alembic commands ###
