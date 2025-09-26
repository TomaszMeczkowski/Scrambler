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
``` 

### 2. Utwórz i aktywuj środowisko
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```


### 3. Skonfiguruj zmienne środowiskowe
Utwórz w katalogu config projektu plik `.env` z następującą zawartością (Sekret Django zmień na własny unikalny ciąg znaków):

```env
SECRET_KEY=django-insecure-moj-sekret
DEBUG=True
```

### 4. Zainstaluj zależności
```bash
pip install .
```

### 5. Wykonaj migracje bazy danych
```bash
python manage.py migrate
```

### 6. Uruchom serwer
```bash
python manage.py runserver
```