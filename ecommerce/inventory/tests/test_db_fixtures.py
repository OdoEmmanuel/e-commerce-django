import pytest
from ecommerce.inventory import models

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (19, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),

    ]
)
def test_inventory_category_dbfixture(
    db, django_db_setup, id, name, slug, is_active
):
    result = models.Category.object.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active

@pytest.mark.dbfixture
@pytest.mark.parametrize(
   "name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (19, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),

    ]
)
def text_inventory_db_ctegory_insert_data(
    db, category_factory, name, slug, is_active
):
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active 