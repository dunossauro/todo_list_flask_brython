"""Alterando tamanho do campo STATE

Revision ID: b383438641b9
Revises: 82b0f7c525e6
Create Date: 2020-09-23 09:51:04.054342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b383438641b9'
down_revision = '82b0f7c525e6'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.alter_column(
            'state',
            existing_type=sa.VARCHAR(length=5),
            type_=sa.String(length=15),
            existing_nullable=False,
        )


def downgrade():
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.alter_column(
            'state',
            existing_type=sa.String(length=15),
            type_=sa.VARCHAR(length=5),
            existing_nullable=False,
        )
