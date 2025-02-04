import datetime
import os
import tarfile
import shutil

IRAN = datetime.timezone(datetime.timedelta(hours=3.5))

def cleanup():
    now = datetime.datetime.now(IRAN)
    # get last month
    first_day = now.replace(day=1)
    last_day = first_day - datetime.timedelta(days=1)
    py, pm = last_day.year, last_day.month

    logs_dir = f'gunicorn/logs/{py}-{pm:02d}'

    if not os.path.exists(logs_dir):
        return

    gzip_path = f'gunicorn/logs/{py}-{pm:02d}.tar.gz'
    try:
        with tarfile.open(gzip_path, 'w:gz') as tar:
            for root, dirs, files in os.walk(logs_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=logs_dir)
                    tar.add(file_path, arcname=arcname)
        shutil.rmtree(logs_dir)
    except Exception as e:
        print("ERROR when creating tar.gz file")
        print(e)


def write_to_file(content):
    cleanup()

    date = datetime.datetime.now(IRAN)
    now = date.strftime("%Y-%m-%d %H:%M:%S")
    full = date.strftime("%Y-%m-%d")
    month = date.strftime("%Y-%m")

    dir_prefix = 'gunicorn/logs'
    logs_dir = f'{dir_prefix}/{month}'

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    file_name = f'{logs_dir}/{full}.txt'

    try:
        with open(file_name, 'a') as f:
            f.write(f"[{now}] {content}\n")
    except Exception as e:
        print("ERROR writing to log file")
        print(e)


def post_request(worker, request, env, response):
    try:
        write_to_file(f"{response.status_code} {request.method} {request.remote_addr[0]} {request.uri}")
    except Exception as e:
        print("ERROR when calling write_to_file function")
        print(e)

