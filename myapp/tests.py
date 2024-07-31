import pytest
from django.urls import reverse
from django.test import Client
from .utils import addition
from .models import Author
from django.utils import timezone

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

    
@pytest.mark.django_db
def test_author_creation():

    author1=Author.objects.create(
        name='Naveen',
        dob=timezone.now().date()
    )

      # Check that the instance was created correctly
    assert author1.author_id is not None
    assert author1.name == 'Naveen'
    assert author1.dob is not None

