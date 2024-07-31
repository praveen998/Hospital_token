import pytest
from django.urls import reverse
from django.test import Client
from .utils import addition

@pytest.mark.django_db
def test_home_views():
    client=Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert response.content.decode() == "success"


def test_addition():
    assert addition(1,2)==3
    assert addition(2,2)==4
    assert addition(7,2)==9
    assert addition(1,3)==4

    
