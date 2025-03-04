"""tercer cambio

Revision ID: 97cf89a2305d
Revises: 32350a23fa17
Create Date: 2025-02-23 19:36:30.441836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97cf89a2305d'
down_revision: Union[str, None] = '32350a23fa17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gatos',
    sa.Column('id_gato', sa.Integer(), nullable=False),
    sa.Column('maullido', sa.String(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_gato'),
    sa.UniqueConstraint('maullido')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gatos')
    # ### end Alembic commands ###
