
# MCAS data grabber
# Jedediyah Williams
# November 2016
# 
# http://profiles.doe.mass.edu/mcas/
# 
#   Nantucket Elementary School: 01970005
# Nantucket Intermediate School: 01970020
#    Cyrus Pierce Middle School: 01970010
#         Nantucket High School: 01970505
#
# To get results for a particular school [SCHOOL_ID] and year [YEAR], we use the URL:
# http://profiles.doe.mass.edu/mcas/achievement_level.aspx?linkid=32&orgcode=[SCHOOL_ID]&orgtypecode=6&&fycode=[YEAR]


import urllib2

def stripHTMLtags(line):
    # Given a string line, strips HTML tags and entities 
    first = ""
    add = True
    for c in line:
        if c == "<":
            add = False
        if add:
            first += c
        if c == ">" :
            add = True
    result = ""
    add = True
    for c in first:
        if c == "&":
            add = False
        if add:
            result += c
        if c == ";" :
            add = True
    return result     
    
def grab_MCAS_data(year,school_id):
    # School IDs are available from http://profiles.doe.mass.edu/search/search.aspx?leftNavId=11238
    # Available years are between 1998 and present.
    # Returns lists category percents in Advanced, Proficient, Needs Improvement, and Warning/Failing of the form:
    # [year,subject, school_data, state_data]
    # where each _data is [% advanced, % proficient, % NI, % warning]
    
    # Grab the HTML from Mass DOE
    baseurl = "http://profiles.doe.mass.edu/mcas/achievement_level.aspx?linkid=32&orgtypecode=5&orgcode=" + school_id + "&fycode=" + str(year)
    lines = urllib2.urlopen(baseurl).read().split('\n')
    raw_data = []
    for i in range(len(lines)):
        line = lines[i]
        if "START MCAS REPORT" in line:
            for j in range(i,len(lines)):
                line = lines[j]
                raw_data.append( stripHTMLtags( line ) )
                if "END MCAS REPORT" in line: 
                    break
            break 
            
    # Parse the HTML document 
    data = []
    for i in range(len(raw_data)):
		line = raw_data[i]
		try:
			if line[0:5] == 'GRADE':
				grade = 'Grade ' + line[6:8].rstrip()
				subject = line[11:14].rstrip()       
				#ack = int( raw_data[i+1].rstrip() )
				#state = int( raw_data[i+2].rstrip() )
				school = [ int( raw_data[i+3].rstrip() ), 
				           int( raw_data[i+5].rstrip() ),
				           int( raw_data[i+7].rstrip() ),
				           int( raw_data[i+9].rstrip() ) ]
				state = [ int( raw_data[i+4].rstrip() ), 
				           int( raw_data[i+6].rstrip() ),
				           int( raw_data[i+8].rstrip() ),
				           int( raw_data[i+10].rstrip() ) ]
				data.append( [year, subject, grade, school, state] )
		except:
			print 'Skipping line of missing data in ' + str(year) + ' for school ' + school_id
    return data
	
   
def get_subject(year,school_id,subject):
    # Returns school_data, state_data, differential_data
    school_data = []
    state_data = []
    differential_data = []
    year_data = grab_MCAS_data(year,school_id)
    for data in year_data:
        if data[1] == subject:
            school_data.append(data[3])
            state_data.append(data[4])
            differential_data.append([data[3][0]-data[4][0],data[3][1]-data[4][1],data[3][2]-data[4][2],data[3][3]-data[4][3]])
    return school_data, state_data, differential_data

def get_grade(year,school_id,subject,grade):
    # Returns school_data, state_data, differential_data
    year_data = grab_MCAS_data(year,school_id)
    for data in year_data:
        if data[1] == subject and str(grade) in data[2]:
            return  data[3], \
                    data[4], \
                    [data[3][0]-data[4][0],data[3][1]-data[4][1],data[3][2]-data[4][2],data[3][3]-data[4][3]]
    return [],[],[]


if __name__ == "__main__":
    #result = grab_MCAS_data(2016,'01970005')
    #print result
    school_data, state_data, diff_data = get_subject(2014,'01970005','MAT')
    print school_data
    print state_data
    print diff_data

