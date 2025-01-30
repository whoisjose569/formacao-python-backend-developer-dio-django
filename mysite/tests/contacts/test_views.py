from http import HTTPStatus
from django.urls import reverse
import pytest
from django.contrib.auth.models import User, Permission


def test_contacts_thanks(client):
    name = 'Jhon'
    response = client.get(reverse("contacts:thanks", args=(name,)))
    
    assert response.status_code == HTTPStatus.OK
    assert f"Obrigado {name}" in response.content.decode()

def test_contact_create_with_unauthenticated_user(client):
    url = f"{reverse("accounts:login")}?next={reverse("contacts:create")}"
    
    response = client.get(reverse("contacts:create"))
    
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url

@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    user = django_user_model.objects.create_user(username='john', email='john@testmail.com', password='test')
    permission = Permission.objects.get(codename="add_contact")
    user.user_permissions.add(permission)
    
    data = {'subject': 'subject@testemail.com', 'message': 'Hello World', 'sender': 'sender@testemail.com', 'cc_myself': True}
    
    client.force_login(user)
    response = client.get(reverse("contacts:create"), data)
    
    assert response.status_code == HTTPStatus.OK

