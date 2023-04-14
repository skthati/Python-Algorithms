
```Python
if seconds == 0:
        return "now"
    
    # compute the number of years, days, hours, minutes, and seconds
    year = seconds // (365 * 24 * 60 * 60)
    seconds %= 365 * 24 * 60 * 60
    day = seconds // (24 * 60 * 60)
    seconds %= 24 * 60 * 60
    hour = seconds // (60 * 60)
    seconds %= 60 * 60
    minute = seconds // 60
    seconds %= 60
    
    # build the string representation of the duration
    duration_parts = []
    if year > 0:
        duration_parts.append(f"{year} year{'s' if year > 1 else ''}")
    if day > 0:
        duration_parts.append(f"{day} day{'s' if day > 1 else ''}")
    if hour > 0:
        duration_parts.append(f"{hour} hour{'s' if hour > 1 else ''}")
    if minute > 0:
        duration_parts.append(f"{minute} minute{'s' if minute > 1 else ''}")
    if seconds > 0:
        duration_parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")
    
    # join the parts with commas and "and"
    if len(duration_parts) == 1:
        return duration_parts[0]
    elif len(duration_parts) == 2:
        return f"{duration_parts[0]} and {duration_parts[1]}"
    else:
        return f"{', '.join(duration_parts[:-1])}, and {duration_parts[-1]}"
    ``


```Python
y = int(seconds/31536000)
    d = int(seconds/86400)
    h = int((seconds%86400)/3600)
    m = int(((seconds%86400)%3600)/60)
    s = int((((seconds%86400)%3600)%60)%60)
    days = "days,"
    hours = "hours,"
    minutes = "minutes"
    seconds = "seconds"
    and1 = " and"
    h1 = 0
    d1 = 0
    
    
    if d == 1:
        days = days.strip("s,")
        if h == 0 or m == 0 or s == 0:
            days = days
        else:
            days = days + ","
    elif d == 0:
        days = ""
        d1 = d
        d = ""
        
        
    
    if h == 1:
        hours = hours.strip("s,")
        if m == 0 or s == 0:
            hours = hours
        else:
            hours = hours + ","
    elif h == 0:
        hours = ""
        h1 = h
        h = ""
        
    if m > 1:
        if s == 0:
            minutes = minutes
        else:
            minutes = minutes + and1
    elif m == 1:
        if s > 0:
            minutes = minutes.strip("s") + and1
        else:
            minutes = minutes.strip("s")
    elif m == 0:
        minutes = ""
        if d1 > 1 or h1 > 1:
            minutes = and1
        m = ""
        
    
    if s == 1:
        seconds = seconds.rstrip("s")
    elif s == 0:
        seconds = ""
        s = ""
        
    
    result = f"{d} {days} {h} {hours} {m} {minutes} {s} {seconds}"
    result = result.strip()
    return result
    ```
