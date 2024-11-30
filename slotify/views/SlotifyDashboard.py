from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from slotify.slotifyModels.SlotifyUserData import SlotifyUserData


@login_required
def SlotifyDashboard(req):
    content = {}
    user_id = req.user.id
    userData = SlotifyUserData.objects.get(user_id = user_id)
    if (userData):
        content = {
            'data' : userData
        }
        return render(req,'slotify/SlotifyDashboard.html',content)
    else:
        return HttpResponse('Somthing went Wrong on Slotify dashbord')
    