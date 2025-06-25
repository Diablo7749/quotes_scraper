import json
from mongoengine import connect, disconnect, Document, StringField, ListField, ReferenceField


disconnect()

# Підключення до MongoDB Atlas (замінити значення на свої)
connect(
    db="quotes_db",
    username="26012003mark",
    password="77Jetta49",
    host="mongodb+srv://cluster0.18xievb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    authentication_source="admin"
)

# Модель автора
class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# Модель цитати
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)

# Завантажуємо авторів
with open("authors_cleaned.json", encoding="utf-8") as f:
    authors_data = json.load(f)

for author in authors_data:
    if not Author.objects(fullname=author['fullname']):
        Author(
            fullname=author['fullname'],
            born_date=author.get('born_date'),
            born_location=author.get('born_location'),
            description=author.get('description')
        ).save()

# Завантажуємо цитати
with open("quotes_cleaned.json", encoding="utf-8") as f:
    quotes_data = json.load(f)

for quote in quotes_data:
    author = Author.objects(fullname=quote['author']).first()
    if author:
        Quote(
            tags=quote.get('tags', []),
            author=author,
            quote=quote['quote']
        ).save()

print("✅ Дані успішно завантажено в MongoDB!")
