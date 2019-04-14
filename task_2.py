import queue
from threading import Thread
import requests
import re
import time
from time import sleep


''' Reads the Plain text files containing URLS, Reads the Json Data and Prints the First 80 characters of URL'S Response,'''

def test_urls(que,links):
    url_link = re.sub('[\n]',' ',links[0])
    start = time.time()
    data_json = requests.get(url_link)
    print(url_link)
    # sleep(1)
    if data_json:
        result = data_json.json()
        stop = time.time()
        if result['data']:
            final_data = []

            count = 0
            for x in result['data']:
                for k, v in x.items():
                    for row in list(k):
                        count += 1
                        if count <= 80:
                            final_data.extend(list(row))
            print('First 80 Characters of URL: ',final_data)
        return (stop - start)


'''Fetches the URL in parallel(Multithreading),Records and prints the Taken taken per URL.'''
que = queue.Queue()
thread_list = []
with open('input_file_2.txt','r') as f:
    for line in f.readlines():
        ques_thread1 = Thread(target=lambda qq, args1: qq.put(test_urls(qq,args1)),
                              name='thread{}'.format('1'),
                              args=(que, [line]))
        ques_thread1.start()
        thread_list.append(ques_thread1)

        ques_thread2 = Thread(target=lambda qq, args1: qq.put(test_urls(qq,args1)),
                              name='thread{}'.format('2'),
                              args=(que, [line]))
        ques_thread2.start()
        thread_list.append(ques_thread2)

        ques_thread3 = Thread(target=lambda qq, args1: qq.put(test_urls(qq, args1)),
                              name='thread{}'.format('3'),
                              args=(que, [line]))
        ques_thread3.start()
        thread_list.append(ques_thread3)

    for threads_qs in thread_list:
        print('{} has started \n'.format(threads_qs.name))
        threads_qs.join(0.1)
        try:
            total_execution_time = que.get()
            if total_execution_time:
                print('Time Taken: {0} secs'.format(round(total_execution_time,4)))

        except queue.Empty:
            pass





