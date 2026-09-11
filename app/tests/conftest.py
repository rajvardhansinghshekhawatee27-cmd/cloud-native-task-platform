import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.database import Base
from src.main import app
from src.database import get_db


TEST_DATABASE_URL = (
    "postgresql+psycopg2://"
    "taskuser:taskpassword@localhost:5432/taskdb_test"
)


test_engine = create_engine(
    TEST_DATABASE_URL,
    pool_pre_ping=True
)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False
)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=test_engine)

    yield

    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(autouse=True)
def clean_database():
    db = TestingSessionLocal()

    try:
        db.execute(text("TRUNCATE TABLE tasks RESTART IDENTITY"))
        db.commit()
    finally:
        db.close()


@pytest.fixture(autouse=True)
def override_database():
    def get_test_db():
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = get_test_db

    yield

    app.dependency_overrides.clear()