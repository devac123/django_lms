from django.shortcuts import render,H
from django.contrib.auth.decorators import login_required
from slotify.slotifyModels.SlotifyUserData import SlotifyUserData


@login_required
def SlotifyDashboard(req):
    content = {}
    user_id = req.user.id
    data = SlotifyUserData.objects.get(user_id = user_id)
    if (data):
        content['user'] = data
        return render(req,'slotify/SlotifyDashboardTest.html',data)
    else:
        return render(req,'slotify/SlotifyDashboardTest.html')
    