"""empty message

Revision ID: ca153d1be704
Revises: f48a79808cbb
Create Date: 2018-04-13 10:28:26.313666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca153d1be704'
down_revision = 'f48a79808cbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_bus_stops_name'), 'bus_stops', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bus_stops_name'), table_name='bus_stops')
    # ### end Alembic commands ###
