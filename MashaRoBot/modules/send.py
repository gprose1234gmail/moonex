from telegram.ext import run_async

from MashaRoBot import dispatcher
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from MashaRoBot.modules.helper_funcs.alternate import send_message
from MashaRoBot.modules.helper_funcs.chat_status import dev_plus


@run_async
@dev_plus
def reply(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message.reply_to_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("kitty", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["kitty"]
__handlers__ = [ADD_CCHAT_HANDLER]
