from django.shortcuts import render
from .forms import NetForm, Article, GameRoomlistForm
from .models import Network, MakeGameRoom
from . import UseSDK
import os
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
DIR_PATH = os.path.abspath(os.path.dirname('__file__'))

# def first(request):
#     # template = loader.get_template('templates/index.html')
#     template = loader.get_template('/index.html')
#     context = {
#         'latest_question_list': "test",
#     }
#     return HttpResponse(template.render(context, request))



#
# def first(request):
#     form = Network()
#     if request.method == "POST":
#         form = NetForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = NetForm()
#     return render(request, "index.html",  {"form" : form})

def MakeGameRoom(request):
    form = GameRoomlistForm()
    if request.method == "POST":
        form = NetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NetForm()
    return render(request, "MakeGameRoom.html",  {"form" : form})
    # return render(request, "index.html")


def Mint(request):
    return render(request, "MintToken.html")

def Sample(request):
    return render(request, "Sample.html")

def balance(request):
    # return render(request, "iconex_connect_sample.1.html")
    return render(request, "balance.html")


def RoomList(request):

    __data=UseSDK.JsonRPCCalls()
    _data=__data.show_game_room_list()
    out_data={}
    roomnumber = 0
    for readdata in _data:
        print(readdata)
        temp={}
        splited = readdata.split(".")
        temp["Name"] = splited[0]
        temp["Explain"] = splited[1]
        temp["Prize"] = splited[2]
        temp["Time"] = splited[3]
        out_data["RoomNo"+str(roomnumber)] = temp
        roomnumber += 1
    return render(request, "game_room_list.html", {"WaitRoom" : out_data})

def Original(request):

    __data = UseSDK.JSONRPCcalls()

    return render(request, "Qury.html")