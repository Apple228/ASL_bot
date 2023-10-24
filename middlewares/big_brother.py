# import logging
#
# from aiogram import types
# from aiogram.dispatcher.handler import CancelHandler
# from aiogram.dispatcher.middlewares import BaseMiddleware
#
# from data.config import ALL_TG_ID
# from loader import db
#
#
# class BigBrother(BaseMiddleware):
#     async def on_pre_process_update(self, update: types.Update, data: dict):
#
#         if update.message:
#             user = update.message.from_user.id
#         # elif update.message.from_user.id:
#         #     user = update.callback_query.from_user.id
#         else:
#             return
#
#         if user not in ALL_TG_ID:
#             logging.info(f"Отказано в доступе для: {user}")
#             raise CancelHandler()
#
#
