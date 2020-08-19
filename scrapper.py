import requests
import io

startRollNo = 7611860
endRollNo =   7612000
schoolno = '50076'
centerno = 7051
string = ""

while True:

	try:	
		startRollNo = startRollNo + 1

		data={'regno': str(startRollNo), 'sch':schoolno, 'cno':str(centerno) , 'B2': 'Submit'}
		headers={'Referer':'http://resultsarchives.nic.in/cbseresults/cbseresults2018/class12zpq/Class12th18.htm'}
		r = requests.post("http://resultsarchives.nic.in/cbseresults/cbseresults2018/class12zpq/Class12th18.asp", data=data, headers=headers)
	

		if startRollNo == endRollNo + 1:
			with io.open("file1.txt", "w", encoding="utf-8") as f:
				f.write(string)
			print ("DONE")
			break
		
		else:
			string += r.text
			# print(string)
	
	except Exception as e:
		print ('Going to sleep for 30 seconds...\n')
		print (e)
		time.sleep(30)
		continue