from sqlmodel import SQLModel, create_engine

from hexon.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
