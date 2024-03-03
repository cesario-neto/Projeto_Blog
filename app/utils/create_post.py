"""
Only run this script if you want test posts
"""
import os
import sys
import django
from django.conf import settings
from pathlib import Path

path = Path(__file__).parent.parent
sys.path.append(str(path))

os.environ["DJANGO_SETTINGS_MODULE"] = "app.settings"
django.setup()

if __name__ == '__main__':
    from post.models import Category, Post
    from django.contrib.auth.models import User
    from django.utils.text import slugify
    from random import randint
    from faker import Faker
    from faker.providers import lorem

    fake = Faker()
    fake.add_provider(lorem)

    QNT_CATEGORY = 3
    QNT_POST = 100

    for x in range(QNT_CATEGORY):
        category_name = fake.text(max_nb_chars=30)
        Category.objects.create(name=category_name)

    categories = Category.objects.all()
    user = User.objects.all().first()
    for x in range(QNT_POST):
        post_title = fake.text(max_nb_chars=30)
        post_description = fake.text(max_nb_chars=100)
        post_content = fake.paragraph(nb_sentences=20)
        post_slug = slugify(fake.text(max_nb_chars=10))
        post_category = categories[randint(0, (len(categories)) - 1)]
        post_is_publishe = True
        post_author = user
        Post.objects.create(
            title=post_title, description=post_description,
            content=post_content, category=post_category,
            is_publishe=post_is_publishe, author=post_author,
            slug=post_slug)
