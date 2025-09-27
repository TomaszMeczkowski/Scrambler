import random
from django.shortcuts import render, redirect
from .forms import UploadFileForm


def scramble_word(word: str) -> str:
    if len(word) <= 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + "".join(middle) + word[-1]


def scramble_text(text: str) -> str:
    words = text.split()
    scrambled_words = [scramble_word(word) for word in words]
    return " ".join(scrambled_words)


def upload_file(request):
    """Main page with file upload form."""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            text = file.read().decode("utf-8")
            result = scramble_text(text)
            # zapisujemy wynik do sesji
            request.session["result"] = result
            return redirect("result")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def result_view(request):
    """Page that displays the scrambled result."""
    result = request.session.get("result", None)
    return render(request, "results.html", {"result": result})
