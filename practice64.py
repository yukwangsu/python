def stat_func(*data):
    
    a = sum(data)
    mean = a/len(data)

    b = 0 
    for i in range(len(data)):
        b += (data[i]-mean)**2 
    variance = b/len(data)

    standard = (variance)**(1/2)

    return(mean, variance, standard)
