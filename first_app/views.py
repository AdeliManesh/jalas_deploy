import json
from django.urls import reverse
from django.utils.crypto import get_random_string
from first_app.functions import *
from first_app.models import Poll, Participant

timeout_flag = 0
shared_response = HttpResponse()



def index(request):
    return HttpResponse("Hello God")


def create_poll(request):
    try:
        list_email = []
        print("here_create_poll")
        body = request.body.decode("utf-8")
        my_json = json.loads(body)
        unique_url = get_random_string(length=10)
        poll = Poll.objects.create(title=my_json["title"], poll_url=unique_url,)
        poll.save()
        for index, i in enumerate(my_json["Options"]):
            option = Option.objects.create(start=i["start"], end=i["end"], poll=poll, option_id=index)
            option.save()
        for i in my_json["Participants"]:
            participant = Participant.objects.create(name=i["name"], email=i["email"])
            participant.save()
            poll.participants.add(participant)
            list_email.append(i["email"])
        resp = HttpResponse(unique_url)
        resp.status_code = 200
        print(request.get_host())
        email(list_email,subject="Poll Creation",body="Poll created http://%s%s%s%s" %(request.get_host(),reverse("get_poll"),"?poll_url=",unique_url))
        return resp
    except:
        return HttpResponse(status=400)


def get_poll(request):
    poll_url = request.GET["poll_url"]
    poll = Poll.objects.filter(poll_url=poll_url)[0]
    res_json = poll_json_creator(poll)
    resp = HttpResponse(json.dumps(res_json), content_type="application/json")
    return resp


def get_all_polls(request):
    all_polls = Poll.objects.all()
    all_poll_array = []
    for i in all_polls:
        all_poll_array.append(poll_json_creator(i))
    resp = HttpResponse(json.dumps({"Polls": all_poll_array}), content_type="application/json")
    return resp


def delete_poll(request):
    poll_url = request.GET["poll_url"]
    Poll.objects.filter(poll_url=poll_url).delete()
    return HttpResponse("deleted_poll")


def add_vote(request):
    poll_url = request.GET["poll_url"]
    poll = Poll.objects.filter(poll_url=poll_url)[0]
    option_id = request.GET["option_id"]
    val = request.GET["vote_val"]
    voter_name = request.GET["voter_name"]
    participant = Participant.objects.filter(name=voter_name)[0]
    Vote.objects.create(poll=poll, option_id=option_id, val=val, participant=participant)
    return HttpResponse("add_vote")


def get_rooms(request):
    poll_url = request.GET["poll_url"]
    option_id = int(request.GET["option_id"])
    poll = Poll.objects.filter(poll_url=poll_url)
    option = Option.objects.filter(poll__poll_url=poll_url, option_id=option_id)[0]
    print(option)
    resp = send_room_request(option.start,option.end)
    return resp


def reserve_room(request):
    poll_url = request.GET["poll_url"]
    option_id = int(request.GET["option_id"])
    room_num = request.GET["room_num"]
    poll = Poll.objects.filter(poll_url=poll_url)[0]
    option = Option.objects.filter(poll__poll_url=poll_url, option_id=option_id)[0]
    resp = reserve_room_request(option.start,option.end,room_num)
    if resp.status_code == 200:
        json_string = json.loads(resp.content)
        unique_url = get_random_string(length=10)
        json_string["meeting_url"]=unique_url
        resp.content = str(json_string)
        particopants = poll.participants.all()
        list_email = []
        for i in particopants:
            list_email.append(i.email)
        email(list_email,"Meeting","Hello you have meeting in date %s %s" %(option.start,option.end))
        meeting= Meeting.objects.create(poll=poll,start=option.start,end=option.end,creator="ali",room_num=room_num,meeting_url=unique_url)
    return resp

def get_meeting(request):
    print(request.GET)
    meeting_url = request.GET["meeting_url"]
    meeting = Meeting.objects.filter(meeting_url=meeting_url)[0]
    return HttpResponse(json.dumps( meeting_json_creator(meeting)), content_type="application/json")

def get_all_meetings(request):
    meetings = Meeting.objects.all()
    array_meetings = []
    for i in meetings:
        array_meetings.append(meeting_json_creator(i))
    return HttpResponse(json.dumps({"Meetings":array_meetings}), content_type="application/json")