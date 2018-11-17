def decrypt (s , d ):
	""" List all possible decoded strings of s.

	>>> decrypt ( ’ alanturing ’, codes )
	[ ’ drink your ovaltine ’, ’spooky ghosts ’, ’spooky scary skeletons ’]
	"""
	if s == '':
		return []
	messages = []
	if s in d :
		messages.append ( d[ s ])
	for k in range (1 , len ( s )+1):
		first , suffix = s [: k ] , s [ k :]
		if first in d :
			for rest in decrypt ( suffix , d ):
				messages . append ( d [ first ] + '' + rest )
	return messages

	# if s == '':
	# 	return []
	# messages = []
	# if s in d :
	# 	messages.append ( d[ s ])
	# for k in range (len ( s )):
	# 	first , suffix = s [: k ] , s [ k :]
	# 	if decrypt(first,d):
	# 		for rest in range(len(suffix)):
	# 			messages . append ( decrypt(first,d)+ decrypt(suffix,d) )
	# return messages

codes = {
	'alan': '’spooky ’',
	'al': '’drink ’',
	'antu': '’your ’',
	'turing': '’ghosts ’',
	'tur': '’scary ’',
	'ing': '’skeletons ’',
	'ring': '’ovaltine ’'}
decrypt ( 'alanturing', codes )