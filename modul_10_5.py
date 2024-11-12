import time
from multiprocessing import Pool


def read_info(file_name):
    all_data = []
    try:
        file = open(file_name, 'r')
        for line in file:
            if len(line) != 0:
                file.readline()
                all_data.append(line)
        file.close()
    except Exception:
        print('что то пошло не так')
    finally:
        file.close()


files_name = [f'./file {number}.txt' for number in range(1, 5)]

time_start = time.time()
for name in files_name:
    read_info(name)

time_stop = time.time()
print(time_stop - time_start)

if __name__ == '__main__':

    with Pool(processes=4) as pool:
        time_start = time.time()
        pool.map(read_info, files_name)
        time_stop = time.time()
        print(time_stop - time_start)
