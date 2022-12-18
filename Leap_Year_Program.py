def is_leap(year):
    
    if (year%100==0):
        if (year%400!=0):
            return False
        else:
            return True
    else:
        if (year%4!=0):
            return False
        else:
            return True
        
      
year = int(input())
print(is_leap(year))
