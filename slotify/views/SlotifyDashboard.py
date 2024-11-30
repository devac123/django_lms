from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from slotify.slotifyModels.SlotifyUserData import SlotifyUserData


@login_required
def SlotifyDashboard(req):
    content = {}
    user_id = req.user.id
    data = SlotifyUserData.objects.get(user_id = user_id)
    content['user'] = data
    return render(req,'slotify/SlotifyDashboard.html',content)