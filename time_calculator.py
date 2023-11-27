
def divide_and_remainder(divisor, num):
  return [num // divisor, num % divisor]

def handle_meridian(meridian , total_hours):
  option_of_meridian = ["AM","PM"]
  if meridian == option_of_meridian[1]:
     new_meridian = "PM" if(total_hours % 2 == 0) else "AM"
     return new_meridian
  else:
     new_meridian = "AM" if(total_hours % 2 == 0) else "PM"
     return new_meridian 
  
def handle_days(time_spend , duration_time_m , new_time , day_of_week = None):
  week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  if duration_time_m >= 24*60 - time_spend and (duration_time_m) - (24*60 - time_spend) < 24*60:
    if day_of_week == None:
      new_time += " (next day)"
    else:
      new_time += f", { week[week.index(day_of_week.lower())+1].capitalize()} (next day)"
  else:
    if day_of_week == None:
     days_for_add = ((duration_time_m) - (24*60 - time_spend))//(24*60) 
     new_time += f" ({days_for_add + 1} days later)" if (days_for_add > 0) else ""
    else:
      days_for_add = ((duration_time_m) - (24*60 - time_spend))//(24*60) 
      new_time += f", {week[(week.index(day_of_week.lower())+days_for_add + 1)%7].capitalize()} ({days_for_add + 1} days later)" if (days_for_add > 0) else f", {day_of_week.capitalize()}"
    
  return new_time  

def add_time(start, duration, day_of_week=None):
  # Parse inputs
  start_hour, start_minute, meridian = map(str.strip, start[:-2].split(":") + [start[-2:]])
  duration_hour, duration_minute = map(int, duration.split(":"))
  # Perform time addition
  total_minutes = (int(start_hour) * 60 + int(start_minute) + int(duration_hour) * 60 + duration_minute) % (12 * 60)
  new_hour, new_minute = divide_and_remainder(60, total_minutes)
  total_hours = (int(start_hour) * 60 + int(start_minute) + int(duration_hour) * 60 + duration_minute) // (12 * 60)
  #Handle AM/PM
  new_meridian = handle_meridian(meridian, total_hours)

  # Format the result
  if new_hour == 0:
      new_hour = 12
  new_time = f"{new_hour}:{new_minute:02d} {new_meridian}"
  
  # Handle number of Days
  if meridian == "PM":
     time_spend = (12*60) + int(start_hour) * 60 + int(start_minute)
     duration_time_m = int(duration_hour) * 60 + duration_minute
     new_time = handle_days(time_spend , duration_time_m , new_time , day_of_week)
  else:
    time_spend = int(start_hour)*60 + int(start_minute)
    duration_time_m = int(duration_hour) * 60 + duration_minute
    new_time = handle_days(time_spend , duration_time_m , new_time , day_of_week)
  

  return new_time


# Test cases
print(add_time("3:30 PM", "2:12"))  # Expected: 6:10 PM
print(add_time("11:55 AM", "3:12"))  # Expected: 2:02 PM, Monday
print(add_time("9:15 PM", "5:30"))  # Expected: 12:03 PM
print(add_time("11:40 AM", "0:25"))  # Expected: 1:40 AM (next day)
print(add_time("2:59 AM", "24:00"))  # Expected: 12:03 AM, Thursday (2 days later)
print(add_time("11:59 PM", "24:05"))  # Expected: 7:42 AM (9 days later)
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))