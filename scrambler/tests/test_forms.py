import pytest
from scrambler.forms import UploadFileForm
from django.core.files.uploadedfile import SimpleUploadedFile


def test_form_valid_txt_file():
    file = SimpleUploadedFile("test.txt", b"Hello world")
    form = UploadFileForm(data={}, files={"file": file})
    assert form.is_valid()


def test_form_rejects_non_txt_file():
    file = SimpleUploadedFile("image.jpg", b"fake-image-data")
    form = UploadFileForm(data={}, files={"file": file})
    assert not form.is_valid()
    assert "Dozwolone są tylko pliki .txt" in str(form.errors)


def test_form_rejects_large_file():
    big_content = b"x" * (2 * 1024 * 1024)  # 2 MB
    file = SimpleUploadedFile("big.txt", big_content)
    form = UploadFileForm(data={}, files={"file": file})
    assert not form.is_valid()
    assert "Plik jest za duży" in str(form.errors)
