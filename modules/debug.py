import json

from lib.cog import Cog, event
from lib.command import makeCommand, Command
from lib.objects import User, Status, HandleChange, Message, UpdateUserList


class Debug(Cog):

    #####
    # Events
    #####
    @makeCommand(name="userlist",description= "test")
    async def vagina(self, c: Command):
        await self.send_message(json.dumps(await self.bot.userlist))
        #await self.send_message("Test")

    @event(event="room::message")
    async def message(self, message: Message):
        print(message.message)
        pass

    @event(event="room::updateUserList")
    async def updateUserList(self, userlist: UpdateUserList):
        print("that" + userlist.user.handle)
        pass