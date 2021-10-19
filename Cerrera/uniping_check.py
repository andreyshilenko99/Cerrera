import requests
import re

lines_control_map = {
    'обогрев': 1,
    'вентилятор_команда': 2,
    'БП ПЭВМ': 4,
    'БП Шелест': 6,
    'БП АПЕМ': 8,
    'ЭВМ1': 9,
    'ЭВМ2': 13,
    'вентилятор': 16,
}

# словарь для отправки команд в uniping
lines_map = {'обогрев': 1,
             'вентилятор_команда': 2,
             'БП ПЭВМ': 3,
             'БП Шелест': 5,
             'БП АПЕМ': 7,
             'ЭВМ1': 10,
             'ЭВМ2': 14,
             'РЕЗЕТ': 15,
             }

auth = ('user', '555')


# получение состояния одного блока через url запрос
def obtain_state(url, line_name):
    result_state = 0
    line = lines_control_map.get(line_name)
    try:
        stroka = requests.get(url + 'io.cgi?io{}'.format(line), auth=auth, timeout=0.05) \
            .content.decode("utf-8")

    except:
        stroka = 'err in connection to uniping'

    stroka_list = re.findall('[0-9]+', stroka)
    if 'ok' in stroka and len(stroka_list) == 3:
        result_state = stroka_list[1]
    state = "включен" if int(result_state) == 1 else "выключен"

    return state


# отправка url команды для включения, выключение АПЕМ
def send_line_command(url, line_name, arg):
    # arg = 0 or 1
    line = lines_map.get(line_name)
    try:
        result_get = requests.get(url + 'io.cgi?io{}={}'.format(line, arg), auth=auth, timeout=0.05) \
            .content.decode("utf-8")
    except:
        result_get = 'ошибка uniping'

    print("{}".format(result_get))


def main_check(url):
    temperature = ''
    temperature_state = ''
    humidity = ''
    wetness_state = ''
    try:
        temp = requests.get(url + 'thermo.cgi?t1', auth=auth, timeout=0.05)
        temp_str = temp.content.decode("utf-8")
        temp_list = re.findall('[0-9]+', temp_str)
        if len(temp_list) > 0:
            temperature = temp_list[0]
            temperature_condition = temp_list[1]
            send_line_command(url, 'вентилятор_команда', arg=1)
            # все круто
            if temperature_condition == '2':
                temperature_state = 'temp_is_ok'
                send_line_command(url, 'обогрев', arg=0)
            #     жарко
            elif temperature_condition == '3':
                temperature_state = 'tempe_not_ok'
                send_line_command(url, 'обогрев', arg=0)
            #     холодно
            elif temperature_condition == '1':
                temperature_state = 'tempe_not_ok'
                send_line_command(url, 'обогрев', arg=1)
            else:
                temperature_state = 'ошибка uniping'
    except:
        temperature = 'ошибка uniping'
    try:
        hum = requests.get(url + 'relhum.cgi?h1', auth=auth, timeout=0.05)
        hum_str = hum.content.decode("utf-8")
        hum_list = re.findall('[0-9]+', hum_str)
        if len(hum_list) > 1:
            humidity = hum_list[0]
            humidity_condition = hum_list[2]
            if humidity_condition == '2':
                wetness_state = 'wetness_is_ok'
            elif humidity_condition == '3':
                wetness_state = 'wetness_not_ok'
                send_line_command(url, 'обогрев', arg=1)
            elif humidity_condition == '1':
                wetness_state = 'wetness_not_ok'
            else:
                wetness_state = 'ошибка uniping'
    except:
        humidity = 'ошибка uniping'

    try:
        cooler = obtain_state(url, 'вентилятор')
    except:
        cooler = 'error'
    try:
        heater_state = obtain_state(url, 'обогрев')
    except:
        heater_state = 'error'
    print(*(temperature, humidity, temperature_state, wetness_state, cooler, heater_state))
    dict_state = {'cooler': cooler,
                  'wetness_state': wetness_state,
                  'temperature_state': temperature_state,
                  'temperature': str(temperature),
                  'wetness': str(humidity),
                  'heater_state': heater_state
                  }

    return dict_state


# # получение состояния всех блоков в комплексе
# def get_complex_state(url):
#     states_map = {0: 'вентилятор', 1: "БП ПЭВМ",
#                   2: 'БП Шелест', 3: "БП АПЕМ",
#                   4: 'ЭВМ2', 5: "ЭВМ2"}
#     states = [obtain_state(url, val) for key, val in states_map.items()]
#
#     states_off = [i for i, e in enumerate(states) if e == 'выкл']
#     if len(states_off) == 0:
#         complex_state = 'включен'
#     elif len(states_off) == 6:
#         complex_state = 'выключен'
#     else:
#         complex_state = 'выключен '
#         for i, stat in enumerate(states_off):
#             if i == 0:
#                 complex_state += states_map[stat]
#             else:
#                 complex_state += f", {states_map[stat]}"
#     return complex_state


if __name__ == "__main__":
    url = 'http://192.168.2.51/'
    x = main_check(url)
