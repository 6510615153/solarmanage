from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Member

import secrets

def code_generate_member():
    while True:
        member_code = secrets.token_hex(8)
        if not Member.objects.filter(member_code=member_code).exists():
            return member_code

@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(member_user=instance, 
                                member_fname = instance.first_name,
                                member_lname = instance.last_name,
                                member_info = "No Information",
                                member_code = code_generate_member(),
                              )