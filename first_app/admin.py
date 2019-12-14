from django.contrib import admin
from first_app.models import Option,Poll,Vote, Participant,Meeting

# Register your models here.
admin.site.register(Option)
admin.site.register(Participant)
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Meeting)
