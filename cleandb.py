import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled.settings')

import django

django.setup()

import random
from first_app.models import  Poll, Option, Vote,Participant,Meeting
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news', 'games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        top2 = add_topic()
        tt= [top,top2]



if __name__ == '__main__':
    print("Populating")
    # populate(20)
    # top = add_topic()
    # fake_url = fakegen.url()
    # fake_date = fakegen.date()
    # fake_name = fakegen.company()
    # wbpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
    # fake_url = fakegen.url()
    # fake_date = fakegen.date()
    # fake_name = fakegen.company()
    # wbpg2 = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
    # print(Webpage.objects.filter(topic__top_name="heshmat"))/
    # t = Topic.objects.all()[1]
    # print(t.webpage_set.all())
    # print(t.top_name)
    # poll = Poll.objects.create(title="hello",poll_url="3")
    Option.objects.all().delete()
    Poll.objects.all().delete()
    Vote.objects.all().delete()
    Participant.objects.all().delete()
    Meeting.objects.all().delete()
    print("End")




