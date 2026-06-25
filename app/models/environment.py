from sqlalchemy import Boolean, String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, BaseModelMixin


class Environment(BaseModelMixin, Base):
    __tablename__ = "environments"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    observation_space: Mapped[str | None] = mapped_column(String(255), nullable=True)
    action_space: Mapped[str | None] = mapped_column(String(255), nullable=True)

    max_episode: Mapped[int | None] = mapped_column(Integer, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)