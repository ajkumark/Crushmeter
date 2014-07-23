from django.db import models

class Crush(models.Model):
	"""To save the details"""
	
	first_name = models.CharField(max_length=30)
	crush_name = models.CharField(max_length=30)
	crush = models.IntegerField()

	def __unicode__(self):	
		return self.first_name +' - '+ self.crush_name+' - '+ str(self.crush) + '%'


def count_char(word):
    result = []
    for w in word:
        count= word.count(w)
        if count != 0:
            result.append(count)
        word = word.replace(w,'')
    return result

def list_maker(result):
    newlist = []
    while(range(len(result)>1)):
        newlist.append(result[0]+result[-1])
        del result[0],result[-1]
    if result:
        newlist.append(result[0])
    return newlist


def calculate(result):
    while(len(result)>2):	
        result = list_maker(result)
    final = str(result[0])+str(result[1])
    if int(final) >= 100:
    	result = 100
    else:
    	result = final
    return result