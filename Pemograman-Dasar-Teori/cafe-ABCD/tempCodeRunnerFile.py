def clear() :
    if os.name == 'nt' :
        return(os.system('cls'))
    else :
        return(os.system('clear'))