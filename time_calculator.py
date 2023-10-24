
def add_time(start_time , duration_time,  day='Monday'):
    string_for_back = ""
    step_one = start_time.split(" ")
    #Spliting arguments
    start_time_div = step_one[0].split(":")
    duration_time_div = duration_time.split(":")
    #Checking houres and minutes
    total_of_hours = int(start_time_div[0]) + int(duration_time_div[0]) 
    total_of_minutes = int(start_time_div[1]) + int(duration_time_div[1])
    #number of days that exist in the information
    total_of_days_after = total_of_hours//24 
    total_of_hours -= total_of_days_after * 24 
    if total_of_hours > 12:
        total_of_hours -= 12
    #working the strings
    
    if total_of_minutes/60 > 1:
        total_of_hours += total_of_minutes//60 
        total_of_minutes -= (total_of_minutes//60)*60    
        string_for_back = str(total_of_hours) + ":" + str(total_of_minutes)
        return string_for_back
    
    else:
        string_for_back = str(total_of_hours) + ":" + str(total_of_minutes) + " " + step_one[1]
        return string_for_back         
    


print(add_time("6:30 PM","205:12")) 