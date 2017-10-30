

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

def makeHTML(year,subject):
    diff = get_graduation_year(year,subject)
    
    var = 'data'+str(year)+subject
    print '############ START HTML ############'
    
    print '<div id="chart_div_'+var+'" style="width: 700px; height: 400px"></div>'
    
    print '<script type="text/javascript">'
    print 'var ' + var + ' = new google.visualization.DataTable();' 
    print var + ".addColumn('number', 'Grade');"
    print var + ".addColumn('number', 'Nantucket');"
    print var + ".addColumn('number', 'State');"
    print var + ".addRows([ "
    grade_3 = get_grade(year-9,'01970005',subject,3) # NES
    grade_4 = get_grade(year-8,'01970005',subject,4) 
    grade_5 = get_grade(year-7,'01970005',subject,5) 
    grade_6 = get_grade(year-6,'01970010',subject,6) # CPS
    grade_7 = get_grade(year-5,'01970010',subject,7) 
    grade_8 = get_grade(year-4,'01970010',subject,8) 
    grade_10 = get_grade(year-2,'01970505',subject,10) # NHS
    if len(grade_3[0])>0:
        print [3,grade_3[0][0]+grade_3[0][1],grade_3[1][0]+grade_3[1][1]], ','
    if len(grade_4[0])>0:
        print [4,grade_4[0][0]+grade_4[0][1],grade_4[1][0]+grade_4[1][1]], ','
    if len(grade_5[0])>0:
        print [5,grade_5[0][0]+grade_5[0][1],grade_5[1][0]+grade_5[1][1]], ','
    if len(grade_6[0])>0:
        print [6,grade_6[0][0]+grade_6[0][1],grade_6[1][0]+grade_6[1][1]], ','
    if len(grade_7[0])>0:
        print [7,grade_7[0][0]+grade_7[0][1],grade_7[1][0]+grade_7[1][1]], ','
    if len(grade_8[0])>0:
        print [8,grade_8[0][0]+grade_8[0][1],grade_8[1][0]+grade_8[1][1]], ','
    if len(grade_10[0])>0:
        print [10,grade_10[0][0]+grade_10[0][1],grade_10[1][0]+grade_10[1][1]]
    print ']);'
    
    print "var options" + var + "= {"
    print "  title: 'Class of "+str(year)+", MCAS "+subject+"',"
    print " pointSize: 3,"
    print "    hAxis: {"
    print "      title: 'Grade',"
    print "    format: 'decimal',"
    print "      minValue: 2,"
    print "      maxValue: 10"
    print "    },"
    print "        vAxis: {"
    print "          title: '% Proficient or Better',"
    print "          minValue: 0,"
    print "          maxValue: 100"
    print "        },"
    print "        backgroundColor: '#ffffff'"
    print "      };"

    print " var chart" + var +" = new google.visualization.LineChart(document.getElementById('chart_div_"+var+"'));"
    print " chart"+var+".draw("+var+", options"+var+");"
    print '</script>'
    print '############ END HTML ############'


if __name__ == "__main__":
    # Grabs data for English and prints it per graduating class.
    #for year in range(2014,2020):
    #    print get_graduation_year(year,'ENG')
    
    for year in [2004]:
        makeHTML(year,'MAT')
    
    
    
    
    



