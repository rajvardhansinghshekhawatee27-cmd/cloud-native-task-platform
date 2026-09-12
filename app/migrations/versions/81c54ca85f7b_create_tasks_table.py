"""create tasks table

Revision ID: 81c54ca85f7b
Revises:
Create Date: 2026-09-12

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "81c54ca85f7b"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the tasks table."""
    op.create_table(
        "tasks",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "completed",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),
    )

    op.create_index(
        op.f("ix_tasks_id"),
        "tasks",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Drop the tasks table."""
    op.drop_index(
        op.f("ix_tasks_id"),
        table_name="tasks",
    )

    op.drop_table("tasks")