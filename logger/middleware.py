from datetime import datetime, timedelta, timezone, date
import os
import tarfile
import shutil

IRAN = timezone(timedelta(hours=3.5))

def cleanup():
    now = datetime.now()
    first_day = now.replace(day=1)
    last_day = first_day - timedelta(days=1)
    py, pm = last_day.year, last_day.month

    logs_dir = f"logger/logs/{py}-{pm:02d}"

    if not os.path.exists(logs_dir):
        return

    gzip_path = f"logger/logs/{py}-{pm:02d}.tar.gz"
    with tarfile.open(gzip_path, 'w:gz') as tar:
        for root, dirs, files in os.walk(logs_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=logs_dir)
                tar.add(file_path, arcname=arcname)

    shutil.rmtree(logs_dir)


def write_to_file(content: str):
    cleanup()

    date = datetime.now()
    full = date.strftime("%Y-%m-%d")
    month = date.strftime("%Y-%m")
    dir_prefix = 'logger/logs'
    logs_dir = f'{dir_prefix}/{month}'

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    file_name = f'{logs_dir}/{full}.txt'
    with open(file_name, 'a') as f:
        f.write(content + '\n')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class LoggerMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_request(self, request):
        pass


    def process_response(self, request, response):
        time = datetime.now(IRAN).strftime("%Y-%m-%d %H:%M:%S")
        log_data = f"[{time}] {response.status_code} {request.method} {get_client_ip(request)} {request.get_full_path()}"

        write_to_file(log_data)
        return response

