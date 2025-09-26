#  Django Text Scrambler

Aplikacja webowa napisana w Django, która umożliwia przesyłanie pliku tekstowego (`.txt`), a następnie przetwarza jego zawartość, mieszając litery w środku każdego wyrazu (pozostawiając pierwszą i ostatnią literę na miejscu).

---

## Funkcjonalności
- Przesyłanie pliku tekstowego przez formularz na stronie głównej.
- Walidacja pliku:
  - Dozwolone tylko pliki `.txt`
  - Maksymalny rozmiar pliku: **1 MB**
- Automatyczne przetwarzanie słów:
  - Jeśli słowo ma ≤ 3 znaki → zostaje bez zmian
  - W przeciwnym razie litery w środku zostają przemieszane
- Strona z wynikiem po przetworzeniu pliku
- Obsługa błędów i czytelne komunikaty walidacyjne
- Stylizacja z użyciem **Bootstrap 5**

---

## Instalacja i uruchomienie

### 1. Sklonuj repozytorium
```bash
git clone https://github.com/TwojeKonto/django-text-scrambler.git
cd django-text-scrambler

# Utwórz środowisko
python -m venv venv

# Aktywuj środowisko
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Zainstaluj zależności
pip install .

# Wykonaj migracje bazy danych
python manage.py migrate

# Uruchom serwer
python manage.py runserver