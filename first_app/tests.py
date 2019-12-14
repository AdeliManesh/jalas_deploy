from django.test import TestCase,Client
from django.urls import reverse
from django.http import HttpResponse
import json
from first_app.models import Meeting,Participant,Poll,Vote,Option

# Create your tests here.

class create_poll_add_vote_get_poll_test(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_poll_url = reverse("create_poll")

    def test_create_poll(self):
        req_url = self.create_poll_url
        d1 = json.dumps({"title":"poll_0",
                            "Options":[
                                {
                                    "start":"2019-12-20T18:00:00",
                                    "end":"2019-12-20T20:00:00"
                                }
                            ],
                            "Participants":[
                                {
                                    "name":"ali",
                                    "email":"ma.adelim@gmail.com"
                                }
                            ]
                        })
        d2 = json.dumps({
                            "Options":[
                                {
                                    "start":"2019-12-20T18:00:00",
                                    "end":"2019-12-20T20:00:00"
                                }
                            ],
                            "Participants":[
                                {
                                    "name":"ali",
                                    "email":"ma.adelim@gmail.com"
                                }
                            ]
                        })
        resp = HttpResponse()
        resp = self.client.post(path=req_url,data=d2,content_type="application/json")
        self.assertEqual(resp.status_code,400)
        resp = self.client.post(path=req_url,data=d1,content_type="application/json")
        self.assertEqual(resp.status_code,200)
        # print(len(Poll.objects.all()))

