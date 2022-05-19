def add_time(start, duration, day = None):

  # Working on 24h clock
  # Formatting data for start argument
  start_1st_split = start.split()
  start_2nd_split = start_1st_split[0].split(":")
  start_hour = int(start_2nd_split[0])
  start_minute = int(start_2nd_split[1])
  suffix = start_1st_split[1]

  if start_hour != 12:
    if suffix == "PM":
      start_hour += 12
      suffix = "AM"

  # Formatting data for duration argument
  duration_split = duration.split(":")
  duration_hour = int(duration_split[0])
  duration_minute = int(duration_split[1])

  # Time in minutes
  start_time = start_hour * 60 + start_minute
  duration_time = duration_hour * 60 + duration_minute

  time = start_time + duration_time

  # Time after counting
  time_hour = time // 60
  time_minute = time - time_hour * 60

  if time_minute < 10:
    time_minute = "0{}".format(time_minute)
  
  # Week days
  week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  
  # Days
  if day != None:
    day_index = week.index(day.lower())

    # If day is today
    day_of_week = week[day_index]

  # Next day
  if time_hour >= 24 and time_hour < 48:
    time_hour -= 24
    next_day = "(next day)"

    # Day next day
    if day != None:
      day_index += 1
      day_of_week = week[day_index]
    
  # n days later
  elif time_hour >= 48:
    next_day_time = time_hour // 24
    time_hour -= next_day_time * 24
    next_day = "({} days later)".format(next_day_time)

    # Day n days later
    if day != None:
      day_index += next_day_time
      if day_index >= 7:
        day_index %= 7
      day_of_week = week[day_index]
  
  else:
    next_day = None
    
  # Hours 12 - 24
  if time_hour >= 12 and time_hour < 24:
    time_hour -= 12
    suffix = "PM"

  # Handling hour 12
  if time_hour == 0:
    time_hour = 12
    
  # new_time formatting
  # Only day count
  if next_day != None:
    new_time = "{}:{} {} {}".format(time_hour, time_minute, suffix, next_day)
    
    # Day count and day string
    if day != None:
      new_time = "{}:{} {}, {} {}".format(time_hour, time_minute, suffix, day_of_week.capitalize(), next_day)
    
  # Only day string
  elif day != None:
    new_time = "{}:{} {}, {}".format(time_hour, time_minute, suffix, day_of_week.capitalize())
  
  # Only time
  else:
    new_time = "{}:{} {}".format(time_hour, time_minute, suffix)
  return new_time