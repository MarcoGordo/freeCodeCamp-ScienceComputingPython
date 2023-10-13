
def add_time(start_time , duration_time,  day='Monday'):
    step_one = start_time.split(" ")
    start_time_div = step_one[0].split(":")
    duration_time_div = duration_time.split(":")
    total_of_time = start_time + duration_time
    #my_check =  total_of_time/24
    return step_one[1]
print(add_time("3:25 PM","6:08"))