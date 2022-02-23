import subprocess
import sys
import time

def get_ps_aux():
    data = subprocess.run(["ps", "aux"], 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')
    if data.stderr:
        print("Ошибка выролнения команды ps aux")
        print(data.stderr)
        sys.exit(0)

    data_list = data.stdout.split("\n")
    return data_list[1:-1]

def data_parse(data):
    params_list = []
    for st in data:
        st = st.split(" ")
        val = [x for x in st if x]
        if len(val) >= 11:
            params_list.append(
                {
                    "USER" : val.pop(0),
                    "PID" : val.pop(0),
                    "CPU" : val.pop(0),
                    "MEM" : val.pop(0),
                    "VSZ" : val.pop(0),
                    "RSS" : val.pop(0),
                    "TTY" : val.pop(0),
                    "STAT" : val.pop(0),
                    "START" : val.pop(0),
                    "TIME" : val.pop(0),
                    "CMD" : " ".join(val)
                }
            )
        else:
            raise IndexError

    return params_list

def check_users(data):
    users = []
    for param in data:
        users.append(param["USER"])
    all_users = list(set(users))
    users_list = []
    for user in all_users:
        users_list.append(f"{user} : {users.count(user)}\n")
    
    return all_users, users_list

def get_timestamp():

    return time.strftime('%d-%m-%Y-%H-%M', time.localtime(time.time()))


def create_report(params):
    report = f"Отчёт о состоянии системы:\n\
Пользователи системы: {', '.join(params['users'])} \n\
Процессов запущено: {params['process']} \n\
Пользовательских процессов: \n{''.join(params['users_list'])}\
Всего памяти используется: {params['mem']}\n\
Всего CPU используется: {params['cpu']}\n\
Больше всего памяти использует: {params['max_mem'][:20]}\n\
Больше всего CPU использует: {params['max_cpu'][:20]}"

    print(report)
    tstamp = get_timestamp()
    with open(f'{tstamp}-scan.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(report)

def check_hard_params(data, param):
    all_param = 0.0
    param_list = []
    for params in data:
        all_param += float(params[param])
        param_list.append((float(params[param]), params["CMD"]))
    
    return round(all_param, 2), max(param_list)[1]

def run_scan():

    data = get_ps_aux()
    data_list = data_parse(data)
    all_users, users_list = check_users(data_list)
    mem, max_mem = check_hard_params(data_list, "MEM")
    cpu, max_cpu = check_hard_params(data_list, "CPU")
    
    params = {
        "process" :len(data_list),
        "users" : all_users,
        "users_list" : users_list,
        "mem" : mem,
        "max_mem" : max_mem,
        "cpu" : cpu,
        "max_cpu" : max_cpu
    }

    create_report(params)
    


if __name__ == "__main__":
    run_scan()
