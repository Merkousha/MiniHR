from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
     
     User.objects.create_superuser(
        username='admin',
        email='admin@amr.ae',
        password='1234'
    )

    #  users = [
    #         {'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'},
    #         {'username': 'user2', 'email': 'user2@example.com', 'password': 'password2'},
    #         {'username': 'user3', 'email': 'user3@example.com', 'password': 'password3'},
    #  ]   
        
    #  for user_data in users:
    #         User.objects.create_user(
    #             username=user_data['username'],
    #             email=user_data['email'],
    #             password=user_data['password']
    #  )