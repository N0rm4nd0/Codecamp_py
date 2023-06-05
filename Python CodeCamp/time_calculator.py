def add_time(start_time, duration, starting_day=None):
    # Parse the start time and duration
    start_time_parts = start_time.split()
    start_time_numbers = start_time_parts[0].split(":")
    start_time_hours = int(start_time_numbers[0])
    start_time_minutes = int(start_time_numbers[1])
    am_pm = start_time_parts[1]
    duration_parts = duration.split(":")
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    # Add the duration to the start time
    end_time_minutes = start_time_minutes + duration_minutes
    end_time_hours = start_time_hours + duration_hours
    if end_time_minutes >= 60:
        end_time_minutes -= 60
        end_time_hours += 1
    end_time_am_pm = am_pm
    if end_time_hours >= 12:
        end_time_hours -= 12
        end_time_am_pm = "PM" if am_pm == "AM" else "AM"
    if end_time_hours == 0:
        end_time_hours = 12

    # Determine the number of days later and adjust the end time and am/pm accordingly
    days_later = end_time_hours // 12
    if days_later == 1:
        day_suffix = " (next day)"
    elif days_later > 1:
        day_suffix = " ({} days later)".format(days_later)
    else:
        day_suffix = ""
    end_time_hours = end_time_hours % 12
    if end_time_hours == 0:
        end_time_hours = 12

    # Construct the final output string
    end_time = "{:d}:{:02d} {}".format(end_time_hours, end_time_minutes, end_time_am_pm)
    if starting_day is not None:
        starting_day = starting_day.lower().capitalize()
        day_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(starting_day)
        day_index = (day_index + days_later) % 7
        day_name = ", " + ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day_index]
    else:
        day_name = ""
    return end_time + day_name + day_suffix