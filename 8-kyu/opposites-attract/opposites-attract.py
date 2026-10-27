def lovefunc( flower1, flower2 ):
    # Make it so that flower1 and flower2 are opposite or even and vis versa, 
    # All else should come out as false. Keep good syntax 
    if (flower1 % 2 == 0 and flower2 % 2 == 1 or flower2 % 2 == 0 and flower1 % 2 == 1):
       return True 
    else :
       return False 