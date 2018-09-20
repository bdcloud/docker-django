#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
#from lib.common import token_verify
#from pymongo import MongoClient
#from config.views import get_dir
from django.shortcuts import HttpResponse
import time
import os
from django.views.decorators.csrf import csrf_exempt
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka:9092','kafka:9093','kafka:9094'],retries=30, acks='all',retry_backoff_ms=20000,reconnect_backoff_ms=20000,linger_ms=50,compression_type='gzip')

class GetSysData(object):
#    collection = get_dir("mongodb_collection")

    def __init__(self, hostname, monitor_item, timing, no=0):
        self.hostname = hostname
        self.monitor_item = monitor_item
        self.timing = timing
        self.no = no


@csrf_exempt
def received_asm_status_info(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        print received_json_data
        dict_received_data = received_json_data[0]
        dict_received_data.update(timeStamp=time.time())
        print dict_received_data
        json_data = json.dumps(dict_received_data)
#        topic = time.strftime('%Y%m%d', time.localtime(time.time()))
#	print topic

        producer.send('StatusInfo', json_data)

	producer.flush()

        return HttpResponse("Post the system Monitor Data successfully!")
    else:
        return HttpResponse("Your push have errors, Please Check your data!")
