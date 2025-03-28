import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker
from io import BytesIO
from django_seed import Seed
from django.contrib.auth.models import User
from events.models import Event, Location, Category
from social.models import Comment , Like
from users.models import UserProfile
from django.contrib.auth import get_user_model  # Use this to get the correct User model
from users.models import UserProfile
import requests
User = get_user_model()  # This ensures compatibility with custom user models
fake = Faker()
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

         # Create 10 users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))

        # Create user profiles with fake avatars
        for user in users:
            profile = UserProfile.objects.create(
                user=user,
                bio=fake.text(max_nb_chars=200),
            )
            # Generate a fake avatar image
            image_url = fake.image_url()
            try:
                response = requests.get(image_url)
                response.raise_for_status()  # Check for HTTP errors
                image_name = f'{user.username}_avatar.jpg'
                profile.avatar.save(image_name, File(BytesIO(response.content)), save=True)
            except requests.RequestException as e:
                self.stdout.write(self.style.ERROR(f'Failed to download image: {e}'))
                continue
        # Create 100 events
           # Create 10 locations
        locations = [Location.objects.create(name=fake.city()) for _ in range(10)]
        self.stdout.write(self.style.SUCCESS('Created locations'))
        categories = [Category.objects.create(name=fake.word()) for _ in range(5)]
        events = []
        for _ in range(100):
            event = Event.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(max_nb_chars=500),
                date=fake.date_between(start_date='-30d', end_date='+30d'),
                location=random.choice(locations),
                organizer=random.choice(users),
            )
            event.categories.set(random.sample(categories, k=random.randint(1, 3)))
            events.append(event)
            self.stdout.write(self.style.SUCCESS(f'Created event: {event.title}'))

        # Create interactions (comments and likes)
        for event in events:
            for _ in range(random.randint(0, 10)):  # Up to 10 comments per event
                Comment.objects.create(
                    event=event,
                    user=random.choice(users),
                    text=fake.sentence(),
                )
            for _ in range(random.randint(0, 20)):  # Up to 20 likes per event
                Like.objects.create(
                    event=event,
                    user=random.choice(users),
                )

        self.stdout.write(self.style.SUCCESS('Data seeding completed!'))
