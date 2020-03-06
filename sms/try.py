import requests
import json
from datetime import datetime
from datetime import timedelta
import time
import numpy as np
import cv2

shortcode = '21583948'
# access_token = 'BZNWGvRbrBjUjQUx9F_TIQfncWq5oQInV_bd6Woz3Ls'
# address = '9453696748'
clientCorrelator = 'cazhia'

time_startclasses = "18:56:00"
minutes_late = "00:00:15"
minutes_absent = "00:00:30"


students = [

  {
    'id_': "cazhia",
    'name': "Cazhia",
    'contact_info': "9453696748",
    'access_token': "BZNWGvRbrBjUjQUx9F_TIQfncWq5oQInV_bd6Woz3Ls",
    'image_path': ""
    }
  # }, {
  #   "id_": "ely",
  #   "name": "Ely",
  #   "contact_info": "9457060739",
  #   "access_token": "M2wJs35Kk1GDp78g_hCxHp-2Di6-gBvWMBNI_mzC42o",
  #   "image_path": ""
  # }, {
  #   "id_": "jagmoc",
  #   "name": "Jagmoc",
  #   "contact_info": "9958414120",
  #   "access_token": "Sgc1cOf8oRWyvpogUIXTDRRh6-O1LeQSMuZfZjB6ECA",
  #   "image_path": ""
  # }, {
  #   "id_": "lei",
  #   "name": "Lei",
  #   "contact_info": "9355542582",
  #   "access_token": "HCP2I5R791p5mqbPczjjIXKSB7QTu_VIV6WtgtI8ldU",
  #   "image_path": ""
  # }

]





# def send(id, name, contact_info, access_token, image_path, lenovo):
# 	now = datetime.now()
# 	message_late = '[LPIHS ADVISORY] Please be informed that your child is late ' + now.strftime("%m/%d/%Y, %H:%M:%S")+ '.'
# 	message_absent = '[LPIHS ADVISORY] Please be informed that your child is absent ' + now.strftime("%m/%d/%Y, %H:%M:%S")+ '.'
# 	if lenovo is 1:
# 		message = message_late

# 	if lenovo is 2:
# 		message = message_absent

# 	# message = '[LPIHS ADVISORY] Please be informed that your child is late ' + now.strftime("%m/%d/%Y, %H:%M:%S")+ '.'
# 	url = "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/"+shortcode+"/requests"

# 	querystring = {"access_token": access_token}

# 	payload = "{\"outboundSMSMessageRequest\": { \"clientCorrelator\": \""+clientCorrelator+"\", \"senderAddress\": \""+shortcode+"\", \"outboundSMSTextMessage\": {\"message\": \""+message+"\"}, \"address\": \""+contact_info+"\" } }"

# 	headers = { 'Content-Type': "application/json", 'Host': "devapi.globelabs.com.ph" }

# 	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)





	# x= json.dumps(response)

	# print(response.text)

	# return response.text

# for student in students:

# 	send("student['id_']", "student['name']", "student['contact_info']", "student['access_token']", "student['image_path']")

def check_late (late_time):
	print(late_time)
	present_date = datetime.now()
	if present_date <= late_time:
		print("False Late")
		return False
	else:
		print("True Late")
		return True

def check_absent (absent_time):
	print(absent_time)
	pres_date = datetime.now()
	if pres_date <= absent_time:
		print("False Absent")
		return False
	else:
		print("True Absent")
		return True

def main(hour, mins, seconds, minutes_late, minutes_absent):
	cap = cv2.VideoCapture(0)
	cur_date = datetime.now()
	start_time = datetime.now()
	# start_time = cur_date.replace(hour=hour, minute=mins, second=seconds)
	#late_time = start_time + timedelta(minutes=minutes_late)
	late_time = start_time + timedelta(seconds=minutes_late)
	# absent_time = start_time + timedelta(minutes=minutes_absent)
	absent_time = start_time + timedelta(seconds=minutes_absent)
	ha = False
	hatdog = False
	now = datetime.now()
	face_cascade = cv2.CascadeClassifier('sms/data/haarcascade_frontalface_alt2.xml')
	while True:
		ret, frame = cap.read()
		if ret == True:
			font = cv2.FONT_HERSHEY_SIMPLEX
			datet = "Time: " + str(datetime.now().time())
			frame = cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

	    # Display the resulting frame
			cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		check_late(late_time)
		check_absent(absent_time)

		# if ha is False:
		# 	if check_late(late_time) is True:
		# 		for student in students:
		# 			# message_late = '[LPIHS ADVISORY] Please be informed that your child is late ' + now.strftime("%m/%d/%Y, %H:%M:%S")+ '.'
		# 			send(student['id_'], student['name'], student['contact_info'], student['access_token'], student['image_path'], 1)
		# 		ha = True

		# if hatdog is False:
		# 	if check_absent(absent_time) is True:
		# 		for student in students:
		# 			# message_absent = '[LPIHS ADVISORY] Please be informed that your child is absent ' + now.strftime("%m/%d/%Y, %H:%M:%S")+ '.'
		# 			send(student['id_'], student['name'], student['contact_info'], student['access_token'], student['image_path'], 2)

		# 		hatdog = True	


		time.sleep(0.5)

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

	return late_time, absent_time

main(7, 0, 0, 10, 15)

#main(7, 0, 0, 15, 30)



# check_late()
	


