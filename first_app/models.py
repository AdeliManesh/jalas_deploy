from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=264)
    email = models.CharField(max_length=264)

    def __str__(self):
        return self.name


class Poll(models.Model):
    poll_url = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    participants = models.ManyToManyField(Participant)
    # owner = models.OneToOneField(Participant,on_delete=models.CASCADE,related_name="owner")
    def __str__(self):
        return self.title


class Option(models.Model):
    option_id = models.IntegerField(default=0)
    start = models.CharField(max_length=264)
    end = models.CharField(max_length=264)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.title + "_" + str(self.start)+ "_" + str(self.end)


class Vote(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    option_id = models.IntegerField(default=0)
    participant = models.ForeignKey(Participant,on_delete=models.CASCADE)
    val = models.IntegerField()

    def __str__(self):
        return self.poll.title+ "_" + str(self.val)


class Meeting(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    start = models.CharField(max_length=264)
    end = models.CharField(max_length=264)
    meeting_url = models.CharField(max_length=264)
    room_num = models.CharField(max_length=264)
    creator = models.CharField(max_length=264)

    def __str__(self):
        return self.creator
