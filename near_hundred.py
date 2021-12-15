def near_hundred(n):
    return(abs(100-n)<=10 or (n>100 and (abs(200-n)<=10)))