"""add_field_address_

Revision ID: de87b2a1220e
Revises: 200431f7ac76
Create Date: 2023-08-16 13:56:16.157291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de87b2a1220e'
down_revision: Union[str, None] = '200431f7ac76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('address', sa.String(length=150), nullable=False))
    op.add_column('teachers', sa.Column('address', sa.String(length=150), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teachers', 'address')
    op.drop_column('students', 'address')
    # ### end Alembic commands ###