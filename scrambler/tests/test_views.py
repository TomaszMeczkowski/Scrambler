import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_upload_file_view_get(client):
    url = reverse("upload_file")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_upload_file_view_post(client):
    url = reverse("upload_file")
    file = SimpleUploadedFile("test.txt", b"Hello world")
    response = client.post(url, {"file": file})
    assert response.status_code == 302  # redirect na result


@pytest.mark.django_db
def test_result_view(client):
    session = client.session
    session["result"] = "Hello wrlod"
    session.save()

    url = reverse("result")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Hello wrlod" in response.content
