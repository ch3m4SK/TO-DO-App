from app import create_app
from app.models import db, Task
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/todo_db'
    app.config['TESTING'] = True
    
    with app.app_context():
        db.create_all()
    
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page():  # ¡El nombre DEBE empezar con "test_"
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200