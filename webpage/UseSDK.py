import json
import os
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.icon_service import IconService

DIR_PATH = os.path.abspath(os.path.dirname('__file__'))


class JsonRPCCalls():

    def __init__(self, keywallet_address = "hxbbf22a5733d5afd3743d4fd39dc9448f481c8f15" , sample_game_score_address = "cx89245b4a663f2062a9fe52a219c44c281e1d6c36"):
        self.sample_game_score_address = sample_game_score_address
        self.keywallet_address = keywallet_address

    def show_game_room_list(self):

        # icon_service = IconService(HTTPProvider("http://localhost:9000/api/v3"))
        icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io/api/v3"))
        call = CallBuilder().from_(self.keywallet_address) \
            .to(self.sample_game_score_address) \
            .method("showGameRoomList") \
            .build()

        response = icon_service.call(call)

        return response

