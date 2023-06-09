""" 
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
"""

def century_from_year(year: int) -> int:
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
    
print(century_from_year(1900)) # 19