
def add_time(start_time , duration_time,  day='Monday'):
    step_one = start_time.split(" ")
    start_time_div = step_one[0].split(":")
    duration_time_div = duration_time.split(":")
    total_of_hours = int(start_time_div[0]) + int(duration_time_div[0]) 
    total_of_minutes = int(start_time_div[1]) + int(duration_time_div[1])
    total_of_days = total_of_hours/24
    if total_of_minutes/60 > 1:
        total_of_hours += total_of_minutes//60    
    return total_of_hours


print(add_time("3:25 PM","6:45")) 