from django.shortcuts import render
from .forms import GameRoomListForm
from . import UseSDK
import os

DIR_PATH = os.path.abspath(os.path.dirname('__file__'))


def make_game_room(request):
    form = GameRoomListForm()
    if request.method == "POST":
        form = GameRoomListForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GameRoomListForm()
    return render(request, "MakeGameRoom.html")


def mint(request):
    return render(request, "MintToken.html")


def sample(request):
    return render(request, "Sample.html")


def balance(request):
    # return render(request, "iconex_connect_sample.1.html")
    return render(request, "balance.html")


def room_list(request):
    _data=UseSDK.JsonRPCCalls()
    _data=_data.show_game_room_list()
    _out_data={}
    _room_number = 0
    for _ in _data:
        print(_)
        _temp={}
        _splited = _.split(".")
        _temp["Name"] = _splited[0]
        _temp["Address"] = _splited[0].split(" ")[0]
        _temp["Explain"] = _splited[1]
        _temp["Prize"] = _splited[2]
        _temp["Time"] = _splited[3]
        _out_data["RoomNo"+str(_room_number)] = _temp
        _room_number += 1
    return render(request, "game_room_list.html", {"WaitRoom" : _out_data})


def original(request):
    __data = UseSDK.JSONRPCcalls()
    return render(request, "Qury.html")

