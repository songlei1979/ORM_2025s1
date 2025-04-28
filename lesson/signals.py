from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from postmarker.core import PostmarkClient

from ORM.settings import POSTMARK_API_KEY

postmark = PostmarkClient(server_token=POSTMARK_API_KEY)

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        print('****************')
        print('user created!')
        print('****************')
        postmark.emails.send(
            From='lsong@unitec.ac.nz',
            To=instance.email,
            Subject="Welcome to my blog",
            HtmlBody="Hi, " + instance.first_name + " welcome to my blog"
        )


@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created is False:
        User.objects.save(user=instance)
        print('****************')
        print('USer Updated!')
        print('****************')
        postmark.emails.send(
            From='lsong@unitec.ac.nz',
            To=instance.email,
            Subject="Welcome to my blog",
            HtmlBody="Hi, " + instance.first_name + " your file have been updated"
        )