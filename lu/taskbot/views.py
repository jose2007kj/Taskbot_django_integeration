# # -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
import logging
import traceback
import sys

from predict_test.lu import *

logger = logging.getLogger(__name__)


def index(request):
    # return render(request,"taskbot/chat.html")
    if request.method == 'POST':
        resp = {'resp_str': 'something wrong', 'action':{'diaact': 'broken'}}
        user_input = request.POST['input']
        uid = request.COOKIES['csrftoken']
        
        try:
            resp['sementic'], resp['status'], resp['action'], resp['resp_str'] = multi_turn_lu3(uid, user_input)
            logger.debug('%s -> %s\n%s' % (user_input, resp['resp_str'], str(resp)))
           
            resp['id'] = "kj"
        except Exception:
            traceback.print_exc(file=sys.stdout)
   

        return HttpResponse(json.dumps(resp), content_type="application/json")

    return render(request,"taskbot/chat.html", {})

