#DROPBOX
class Meeting(object):
	def __init__(self,start,end):
		self.start = start
		self.end - end

#write a function that takes in a list of meetings and return the minimum num of rooms overlap

input = [
	Meeting(13, 15)
	Meeting(14, 16)
	Meeting(17, 29)
]

def scheduler(meetings):
	#greedy algorithm, linear fashion, go through elements one by one
	by_end = meetings.sort(key=lambda meeting:meeting.start)
	sort end time, pick next elem that doesnt overalap


	for meeting in meetings: #n^2 run time
		#check if overlap
		# not sure, have some ideas, bounce of u see where that goes
		#maybe sort meetings and iterate through start times
		#maybe ask about built in sort?
		
		#ie. list_string.sort(key=str.lower)


def scheduler(meetings):
	#type (List[Meeting]) --> int
	time_events = [] #list of timestamp, start or end
	for meeting in meetings: 
		time_events.append((meeting.start, 'start' ))
		time_events.append((meeting.end, 'end' ))
	time_events.sort()
	num_rooms = 0
	max_num_rooms = 0
	for timestamp,event in time_events:
		if event == 'start':
			num_rooms+=1
		else:
			num_rooms -=1
		max_num_rooms = max(num_rooms,max_num_rooms)
	return max_num_rooms

#get your foot in the door
#differentiate yourself, maybe chat about non-dropbox, more casual conversation
#interview prep
cracking the code interview
interviewing.io
questions database; hackerrank;leetcode
latency number that every programmer should know
concurrency

#RESUME TIPS
'''
UI is critical
be true to urself
real estate tradeoff space, quirky??
'''

#random
#dont pressure, entitle, expectation, I Have xyz offers, can u expedite.. NO
authentic
humble

#good questions, not just""whats it like" 
#- better: These are my important values, i am looking for _mentorship, what does dropbox have
#- new blog and I just saw u annouce _ what does that mean for future


