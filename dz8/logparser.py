import re, os, json
import argparse
from collections import defaultdict

def get_top_ip(d):
    top = []
    for i in range(3):
        keymax = max(d, key=d.get)
        top.append(keymax)
        _ = d.pop(keymax)
    return top

def log_parser(file):
    print(f"Отчет по логу файла {file}")
    with open(file) as f:
        lines = f.readlines()

    statistic = defaultdict()
    ips = defaultdict(int)
    methods = defaultdict(int)
    duration_list = []

    req_count = len(lines)
    print(f"Всего запросов: {req_count}")
    statistic["count of requests"] = req_count

    for line in lines:
        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match is not None:
            ip = ip_match.group()
            ips[ip] += 1
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)", line)
            if method is not None:
                methods[method.group(1)] += 1
                url = re.search(r"\d \"(.*?)\"", line)
                if url is None:
                    url = re.search(r"\d - \"(.*?)\"", line)
                timestamp = re.search(r"\[(.*?)\+", line)
                params = [ip, method.group(1), url.group(1), timestamp.group(1).rstrip()]
                duration_list.append((line.split(" ")[-1].rstrip(), params))
    
    top_ips = get_top_ip(ips)
    print(f"Наиболее популярные IP-адреса: {', '.join(top_ips)}")
    statistic["most popular IP"] = top_ips
    print(f"Используемые методы: {dict(methods)}")
    statistic["methods"] = dict(methods)
    max_duration = sorted(duration_list, reverse=True)[:3]
    print(f"Самые длительные запросы:")
    long_answers = []
    for params in max_duration:
        print(f"""Длительность: {params[0]} мс, 
ip: {params[1][0]}, 
метод: {params[1][1]}, 
url: {params[1][2]}, 
время: {params[1][3]}""")

        long_answers.append(
             {
                "duration" : int(params[0]),
                "ip" : params[1][0],
                "method" : params[1][1],
                "url" : params[1][2],
                "timestamp" : params[1][3]
             }
        )
    statistic["the longest answers"] = long_answers
    with open(file+'.json', 'w') as outfile:
        json.dump(statistic, outfile, indent=4)

parser = argparse.ArgumentParser(description='Анализ логов')
parser.add_argument('-f', dest='file', help='путь до логов')
args = parser.parse_args()

if os.path.isfile(args.file):
    log_parser(args.file)
elif os.path.isdir(args.file):
    for logfile in os.listdir(args.file):
        if ".log" in logfile:
            log_parser(logfile)
else:
    print("ERROR: Укажите файл или директорию")
