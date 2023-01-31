import json
import os
from flask import Flask
from flask import request
from flask import make_response
from datetime import datetime
from mysql.connector import connect, Error


# Flask
app = Flask(__name__)


@app.route('/', methods=['POST'])
def MainFunction():
    # รับ intent จาก Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)
    # print(question_from_dailogflow_raw)

    global lineID
    lineID = question_from_dailogflow_raw["originalDetectIntentRequest"]["payload"]["data"]["source"]["userId"]
    print('lineID:', lineID)

    # เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)

    # ตอบกลับไปที่ Dailogflow
    r = make_response(answer_from_bot)
    r.headers['Content-Type'] = 'application/json'  # การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป
    return r

def generating_answer(question_from_dailogflow_dict):
    # Print intent ที่รับมาจาก Dailogflow
    # print(json.dumps(question_from_dailogflow_dict, indent=4, ensure_ascii=False))
    # เก็บต่า ชื่อของ intent ที่รับมาจาก Dailogflow
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"]

    # print('intent ', intent_group_question_str)

    if intent_group_question_str == "Available":
        
        try:
            with connect(
                host="192.168.1.121",
                user="toruser",
                password="64011340",
                database="project",
            ) as connection:
                select_movies_query = "SELECT refer FROM yord WHERE state = 'available' "
                with connection.cursor() as cursor:
                    cursor.execute(select_movies_query)
                    answer_str=''
                    for item in cursor.fetchall():
                        answer_str+='Machine :'+str(item[0])+'\n'
        except Error as e:
            print(e)
        
        if answer_str=='':
            answer_str='No Machine are available'

    if intent_group_question_str == 'UserInfo':
        answer_str = Regis(question_from_dailogflow_dict)

    if intent_group_question_str == 'time_left':
        answer_str = Timee()

    # สร้างการแสดงของ dict
    answer_from_bot = {"fulfillmentText": answer_str}
    # แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4)
    return answer_from_bot


def Regis(respond_dict):

    user_num = respond_dict["queryResult"]["outputContexts"][0]["parameters"]["regis_number.original"]
    print(user_num,type(user_num))
    
    try:
        with connect(
            host="192.168.1.121",
            user="toruser",
            password="64011340",
            database="project",
        ) as connection:
            select_movies_query = "SELECT * FROM yord "
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                data=cursor.fetchall()
                for i in data:
                    if user_num[0] == str(i[0])and i[5]=='':
                        if user_num==i[1] and i[5]=='':
                            val_tuple=(lineID,i[0])
                            update_query = "UPDATE yord SET idline=%s WHERE refer=%s"
                            cursor.execute(update_query,val_tuple)
                            connection.commit()
                            
                            answer_function = 'Registered'
                            return answer_function
                    elif user_num==i[1] and i[5]==lineID:
                        return 'Register successful'

                return 'numbers dont match'
    except Error as e:
        print(e) 


def Timee():
    value=''
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    
    try:
        with connect(
            host="192.168.1.121",
            user="toruser",
            password="64011340",
            database="project",
        ) as connection:
            select_movies_query = "SELECT * FROM yord "
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                for item in cursor.fetchall():
                    if item[5]==lineID:
                        time_stamp=item[3]

                        hour = time_stamp[0:2]
                        minute = time_stamp[3:5]
                        sec = time_stamp[6:8]
                        # current second
                        current_second = current_time[6:8]
                        print('current second', current_second)

                        mode = item[4]

                        # Mode(second)
                        if mode == 'Quick wash':
                            work_time = 20
                        if mode == 'Delicate wash':
                            work_time = 25
                        if mode == 'Power wash':
                            work_time = 30

                        # print('work time', work_time)
                        # print('stamp second', sec)

                        finish_second = int(sec) + work_time
                        # print('finish second', finish_second)

                        carry = int(finish_second) // 60
                        # print('carry', carry)
                        # print('stamp minute', minute)
                        finish_minute = (int(minute) + carry) % 60
                        # print('finish minute', finish_minute)
                        carry1 = int(finish_minute) // 60

                        finish_time = str(int(hour) + carry1) + ':' + str(finish_minute) + ':' + str(finish_second % 60)
                        
                        time_remain = int(finish_second) - int(current_second)
                        # print(finish_time)
                        if time_remain>0:
                            value += 'Machine: '+str(item[0])+'timeleft: '+str(time_remain)+', finish time: '+finish_time+'\n'  
                        else:
                            value += 'Machine: '+str(item[0])+'is finished!!'+'\n'
            
    except Error as e:
        print(e)
    if value=='':
        value='Cannot find your registered ID'
    return value
    print("The current date and time is", current_time)
    # iterate through time stamp
    # hour = time_stamp[0:2]
    # minute = time_stamp[3:5]
    # sec = time_stamp[6:8]
    # # current second
    # current_second = current_time[6:8]
    # print('current second', current_second)

    # mode = test[0][4]

    # # Mode(second)
    # if mode == 'quickwash':
    #     work_time = 20
    # if mode == 'delicate':
    #     work_time = 20
    # if mode == 'powerwash':
    #     work_time = 30

    # print('work time', work_time)
    # print('stamp second', sec)

    # finish_second = int(sec) + work_time
    # print('finish second', finish_second)

    # carry = int(finish_second) // 60
    # print('carry', carry)
    # print('stamp minute', minute)
    # finish_minute = (int(minute) + carry) % 60
    # print('finish minute', finish_minute)
    # carry1 = int(finish_minute) // 60

    # finish_time = str(int(hour) + carry1) + ':' + str(finish_minute) + ':' + str(finish_second % 60)
    # global time_remain
    # time_remain = int(finish_second) - int(current_second)
    # print(finish_time)

    # value = str(time_remain) + ' second left' + '----->' + finish_time

    


# Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)