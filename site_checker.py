import urllib.request, time

with open("Sites.txt") as f:
    sites = f.readlines()
   
maxtime = 10


def check_site(site, maxtime):
    try:
        start_time = time.perf_counter()
        with urllib.request.urlopen(site, timeout=maxtime) as response:
            end_time = time.perf_counter()
            answer = response.getcode()
            return 'OK', answer, end_time - start_time 
    except urllib.error.HTTPError as answer:
        end_time_http = time.perf_counter()
        answer = answer.getcode()
        return 'BAD', answer, end_time_http - start_time
    except urllib.error.URLError as answer:
        answer = answer.reason
        return 'BAD', answer, None 
    except TimeoutError:
        return 'BAD', 'нет ответа', None
    except ValueError as answer:
        return 'BAD', answer, None
    

for num, site in enumerate(sites, 1):
    site = site.strip()
    if site == '':
        print(f"{num}. Неверные входные данные")
    else:
        status, answer, answer_time = check_site(site, maxtime)
        if answer_time is None:
            print(f"{num}. {site} - {status} - по причине: {answer}")
        else:
            print(f"{num}. {site} - {status} - {answer}, время ответа: {answer_time:.2f} сек.")
