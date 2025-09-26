from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Wybierz plik tekstowy (.txt)",
        widget=forms.ClearableFileInput(attrs={"class": "form-control w-50", "accept": ".txt"}),
        error_messages={
            "required": "Musisz wybrać plik do przesłania.",
            "invalid": "Nieprawidłowy plik."
        }
    )

    def clean_file(self):
        file = self.cleaned_data["file"]

        # Sprawdzenie rozszerzenia
        if not file.name.lower().endswith(".txt"):
            raise forms.ValidationError("Dozwolone są tylko pliki .txt")

        # Walidacja rozmiaru (max 1 MB)
        max_size = 1 * 1024 * 1024  # 1 MB w bajtach
        if file.size > max_size:
            raise forms.ValidationError("Plik jest za duży – maksymalny rozmiar to 1 MB")

        return file

        return file
