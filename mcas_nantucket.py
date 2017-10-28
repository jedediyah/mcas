

from mcas import *

def get_graduation_year(year,subject):
    # This method is Nantucket-specific, using the (currently) three schools.
    grade_3 = get_grade(year-9,'01970005',subject,3) # NES
    grade_4 = get_grade(year-8,'01970005',subject,4) 
    grade_5 = get_grade(year-7,'01970005',subject,5) 
    grade_6 = get_grade(year-6,'01970010',subject,6) # CPS
    grade_7 = get_grade(year-5,'01970010',subject,7) 
    grade_8 = get_grade(year-4,'01970010',subject,8) 
    grade_10 = get_grade(year-2,'01970505',subject,10) # NHS
    
    differential_with_state = [ grade_3[2],
                                grade_4[2],
                                grade_5[2],
                                grade_6[2],
                                grade_7[2],
                                grade_8[2],
                                grade_10[2] ]
                                
    print (subject + ' results for class of ' + str(year) + ':')
    grades = ['3','4','5','6','7','8','10']
    for i in range(7):
        diff = differential_with_state[i]
        if len(diff)>0:
            print 'Grade ' + grades[i] + ' ('+str(diff[0]+diff[1])+'), ' + str(diff) 

    return differential_with_state



if __name__ == "__main__":
    # Grabs data for English and prints it per graduating class.
    for year in range(2014,2020):
        print get_graduation_year(year,'ENG')
    
    
    
    
    
    


