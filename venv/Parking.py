# -*- coding= utf-8 -*-
import requests
import json
from .. import Const_Parking, methods
from .. import Const_Platform, methods
from urllib import unquote
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()
class Parking(object):

    def send_post_request_parking_querychargingrate(self, headerargs, bodyargs, paramargs):
        #headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print body
        paramargs=paramargs.encode('utf-8')
        #req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_querychargingrate, params=paramargs, data = body,headers=headers, verify=False)
        req  = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_querychargingrate, params=paramargs, data=body,headers=headers, verify=False)
        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url+body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    def send_post_request_parking_queryfee(self, headerargs, bodyargs, paramargs):
        #headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs=paramargs.encode('utf-8')
        # req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_querychargingrate, params=paramargs, data = body,headers=headers, verify=False)
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryfee, params=paramargs, data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'


    # def send_post_request_parking_queryparkingrec(self, tspToken,key, tspUserId,userId, vin,idType, idValue, longitude,latitude,startTime,endTime,pageSize,pageNo,sortBy):
    #     headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
    #     print 'headers:>>> %s' % headers
    #     data = 'userId=' + userId +'&vin='+str(vin)+ '&startTime=' + str(startTime)+ '&endTime=' + str(endTime)+ '&pageSize=' + str(pageSize)+ '&pageNo=' + str(pageNo)+ '&sortBy=' + sortBy
    #     body = json.dumps({'idType': idType, 'idValue': idValue, 'longitude': longitude, 'latitude': latitude})
    #     req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkingrec, params=data, data=body,headers=headers, verify=False)
    #     print 'URL:>>>> %s' % unquote(req.url)
    #     self.resp = req
    #     self.req = unquote(req.url+body)
    #     self.status_code = req.status_code

    def send_post_request_parking_queryparkingrec(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkingrec, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'


    def send_post_request_parking_queryparkinglotlist(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkinglotlist, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'


    def send_post_request_parking_queryfuzzyparkinglotlist(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryfuzzyparkinglotlist, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'



    def send_post_request_parking_queryparkinglotdetail(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkinglotdetail, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'




    def send_post_request_parking_queryparkinglotstatus(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkinglotstatus, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'


    def send_post_request_parking_queryorderlist(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryorderlist, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'


    def send_post_request_parking_queryparkingrecord(self, headerargs, bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkingrecord, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    def send_post_request_parking_3rdparty_request(self, headerargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps({})
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_3rdparty_request, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    def send_post_request_parking_3rdparty_idunbinding(self, headerargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers

        body = json.dumps({})
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_3rdparty_idunbinding, params=paramargs,
                            data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url + body)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'





    def send_get_request_parking_ratingsummary(self, headerargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers


        paramargs = paramargs.encode('utf-8')
        req = requests.get(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_ratingsummary, params=paramargs, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    def send_get_request_parking_myrating(self, headerargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        req = requests.get(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_myrating, params=paramargs, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'
    def send_get_request_parking_expense_report(self, headerargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        req = requests.get(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_expense_report, params=paramargs, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'
    def send_get_request_parking_status(self, headerargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        req = requests.get(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_status, params=paramargs, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'
    def send_post_request_parking_queryparkinglot_bymaid(self, headerargs,bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_queryparkinglot_bymaid, params=paramargs,data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    #6.2.31 v1
    def send_post_request_parking_checkspauthorizationstatus_v1(self, headerargs,paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        # body = json.dumps(bodyargs)
        # print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_checkspauthorizationstatus, params=paramargs,headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    #6.2.31 v2
    def send_post_request_parking_checkspauthorizationstatus_v2(self, headerargs,paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        # body = json.dumps(bodyargs)
        # print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v2 + Const_Parking.parking_checkspauthorizationstatus, params=paramargs,headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    #6.2.36 查询车辆能否开通停车服务
    def send_post_request_parking_isallowenableparkingservice(self, headerargs,bodyargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        #paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_isallowenableparkingservice,data=body, headers=headers, verify=False)
        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    def send_post_request_parking_depts(self, headerargs,bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_depts, params=paramargs,data=body, headers=headers, verify=False)

        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

    #6.2.30车牌找回
    def send_post_request_parking_plateno_retrieve(self, headerargs,bodyargs, paramargs):
        # headers = {key: tspToken, 'Content-Type': 'application/json;charset=UTF-8','tspUserId':tspUserId}
        headers = {'Content-Type': 'application/json;charset=UTF-8 '}
        if (headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        body = json.dumps(bodyargs)
        print 'body:>>> %s' % body
        paramargs = paramargs.encode('utf-8')
        req = requests.post(self.Domain_maezia + self.ezia_v1 + Const_Parking.parking_plateno_retrieve, params=paramargs,data=body, headers=headers, verify=False)
        print 'URL:>>>> %s' % unquote(req.url)
        print 'alex'
        self.resp = req
        print 'alex'
        self.req = unquote(req.url)
        print 'alex'
        self.status_code = req.status_code
        print 'alex'

##################ParkMaster相关方法########################
    def master_parking_post_request(self, urllink,headerargs=None,paramargs=None,bodyargs=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        body = json.dumps(bodyargs)
        print 'body:>>>%s' % body
        if headers =={} and bodyargs != {}:
            req = requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs, data=body,
                                 verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers !={} :
            req  =   requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers =={}:
            req = requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs, verify=False)
        else:
            req = requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs,data = body,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code

    def master_TJD_parking_post_request(self, urllink,headerargs=None,paramargs=None,plateNum=None,NoticeCode=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        message = {"Data":{"PlateNum":plateNum,"PlateNumColor":"蓝","RequestClientIP":"192.5.0.251"},"NoticeCode":NoticeCode}
        messageString = json.dumps(message)
        dictMessage = {"interfaceName":"NoticeMobileTransfer","interfaceVersion":"1.0","pmParkId":"7715622dff834b34a44448b801c27607","message":messageString}
#body = {'message': '{"Data": {"PlateNum": plateNum, "PlateNumColor": "蓝", "RequestClientIP": "192.5.0.251"},"NoticeCode": 8007}',"interfaceName": "NoticeMobileTransfer", "interfaceVersion": "1.0","pmParkId": "7715622dff834b34a44448b801c27607"}

        #body = json.dumps(dictMessage)
        print 'body:>>>%s' % dictMessage
        req = requests.post(urllink, params=paramargs,data = dictMessage,headers = headers, verify=False)
        print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code

    def master_parkingStatus_get_request(self, urllink,headerargs=None,paramargs=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        req = requests.get(urllink, params=paramargs,headers = headers, verify=False)
        print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code
    def master_TJD_parking_exitVerify_post_request(self, urllink,headerargs=None,paramargs=None,plateNum=None,NoticeCode=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        message = {"Data":{"RequestClientIP":"192.5.0.251"},"NoticeCode":NoticeCode}
        messageString = json.dumps(message)
        dictMessage = {"interfaceName":"NoticeMobileTransfer","interfaceVersion":"1.0","pmParkId":"7715622dff834b34a44448b801c27607","message":messageString}
        print 'body:>>>%s' % dictMessage
        req = requests.post(urllink, params=paramargs,data = dictMessage,headers = headers, verify=False)
        print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code

#below ETCP -Kodai

    def master_parking_createCar_post_request(self, urllink,headerargs=None,paramargs=None,bodyargs=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        body = json.dumps(bodyargs)
        print 'body:>>>%s' % body
        if headers =={} and bodyargs != {}:
            req = requests.post(self.Domain_ma_ingress_maezia + self.account_car_v3 + urllink, params=paramargs, data=body,
                                 verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers !={} :
            req  =   requests.post(self.Domain_ma_ingress_maezia + self.account_car_v3 + urllink, params=paramargs,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers =={}:
            req = requests.post(self.Domain_ma_ingress_maezia + self.account_car_v3 + urllink, params=paramargs, verify=False)
        else:
            req = requests.post(self.Domain_ma_ingress_maezia + self.account_car_v3 + urllink, params=paramargs,data = body,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code

    def master_parking_KODAI_post_request(self, urllink,headerargs=None,paramargs=None,bodyargs=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        body = json.dumps(bodyargs)
        print 'body:>>>%s' % body
        if headers =={} and bodyargs != {}:
            req = requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs, data=body,
                                 verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers !={} :
            req  =   requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers =={}:
            req = requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs, verify=False)
        else:
            req = requests.post(self.Domain_maezia + self.ezia_v1 + urllink, params=paramargs,data = body,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code

    def master_parking_kodaiMock_post_request(self, urllink,headerargs=None,paramargs=None,bodyargs=None):
        headers = {}
        if(headerargs is not None and headerargs != {}):
            headers.update(headerargs)
        print 'headers:>>> %s' % headers
        paramargs = paramargs.encode('utf-8')
        print 'params:>>>%s' % paramargs
        body = json.dumps(bodyargs)
        print 'body:>>>%s' % body
        if headers =={} and bodyargs != {}:
            req = requests.post(urllink, params=paramargs, data=body,
                                 verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers !={} :
            req  =   requests.post(urllink, params=paramargs,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        elif bodyargs == {} and headers =={}:
            req = requests.post(urllink, params=paramargs, verify=False)
        else:
            req = requests.post(urllink, params=paramargs,data = body,headers = headers, verify=False)
            print 'URL:>>>> %s' % unquote(req.url)
        self.resp = req
        self.req = unquote(req.url)
        self.status_code = req.status_code