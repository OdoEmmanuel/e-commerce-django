import pytest 

@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """ 

    return django_user_model.object_supersuser("admin", "odoemmanuel@gmail.com", "password")

@pytest.fixture(scope="session")
def django_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixture    
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")