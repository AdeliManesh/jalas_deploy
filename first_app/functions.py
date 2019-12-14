import threading
import requests
from asgiref.timeout import timeout
from django.core.mail import send_mail
from django.http import HttpResponse
from setuptools.package_index import socket_timeout

from first_app import views as fv
from first_app.models import Option, Vote, Meeting
from untitled import settings


def poll_json_creator(poll):
    options = Option.objects.filter(poll__poll_url=poll.poll_url)
    votes = Vote.objects.filter(poll__poll_url=poll.poll_url)
    participants = poll.participants.all()
    participants_array = []
    for i in participants:
        participants_array.append({"name": i.name, "email": i.email})
    print(votes)
    options_array = []
    for i in options:
        pos_votes = 0
        neg_votes = 0
        for j in votes:
            if j.option_id == i.option_id:
                if j.val == 0:
                    neg_votes += 1
                else:
                    pos_votes += 1
        options_array.append({"option_id": i.option_id,"start": i.start,"end": i.end,"pos_votes": pos_votes, "neg_votes": neg_votes})
    res_json = {"title": poll.title, "poll_url": poll.poll_url, "Options": options_array,
                "Participants": participants_array}
    return res_json

def meeting_json_creator(meeting:Meeting):
    return {"title":meeting.poll.title,"start":meeting.start,"end":meeting.end,"room_num":meeting.room_num}


def try_to_request_room (start,end):
    try:
        fv.shared_response = HttpResponse()
        print("here and trying")
        url = "http://5.253.27.176/available_rooms/?start=" + start + "&end=" + end
        print(url)
        resp = requests.get(url=url)
        fv.shared_response.status_code = resp.status_code
        fv.shared_response.content = resp.text
        print(resp.status_code==200)
        print("all right")
        # print(resp.text)
        print(resp.status_code,resp.text)
        print("here in functions")
        fv.timeout_flag = 200
    except Exception as e:
            print("Exception:",e)


def try_to_request_reserve(start,end,username,room_num):
    try:
        fv.shared_response = HttpResponse()
        print("try_to_request_reserve")
        url = "http://5.253.27.176/rooms/" + room_num + "/reserve/"
        print(url)
        data = {"username": username,
                "start": start,
                "end": end}
        resp = requests.post(url=url,data=data)
        fv.shared_response.status_code = resp.status_code
        fv.shared_response.content = resp.text
        if resp.status_code == 200:
            print("Reserverd")
        else:
            print("Notreserved")
        print(resp.status_code,resp.text)
        fv.timeout_flag = 200
    except Exception as e:
            print("Exception:",e)


def bad_request():
    fv.timeout_flag = 600
    print("boo is 600")


def email(recipient_list,subject,body):
    timeout_flag = 0
    fv.shared_response = HttpResponse()
    subject = subject
    message = body
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)


def send_room_request(start,end):

    fv.timeout_flag = 0
    fv.shared_response = HttpResponse()

    t1 = threading.Thread(target=try_to_request_room,args=(start,end))
    t1.start()
    timer = threading.Timer(4, bad_request)
    timer.start()
    print("timer started")
    while True:
        if fv.timeout_flag == 200:
            print("Server responded")
            timer.cancel()
            break
        if fv.timeout_flag == 600:
            print("Server timeout")
            fv.shared_response.status_code = 400
            fv.shared_response.content = "Server timeout"
            break
    return fv.shared_response


def reserve_room_request(start,end,room_num):

    fv.timeout_flag = 0
    fv.shared_response = HttpResponse()

    t1 = threading.Thread(target=try_to_request_reserve,args=(start,end,"ali",room_num))
    t1.start()
    timer = threading.Timer(4, bad_request)
    timer.start()
    print("timer started")
    while True:
        if fv.timeout_flag == 200:
            print("Server responded")
            timer.cancel()
            break
        if fv.timeout_flag == 600:
            print("Server timeout")
            fv.shared_response.status_code = 400
            fv.shared_response.content = "Server timeout"
            break
    return fv.shared_response
