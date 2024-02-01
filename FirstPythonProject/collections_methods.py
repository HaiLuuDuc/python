def insert(xau,vitri,giatri):
    if(isinstance(xau, str)):
        return xau[:vitri:] + str(giatri) + xau[vitri::]
    else:
        return xau[:vitri:] + [giatri] + xau[vitri::]
    
def remove(xau,vitri):
    return xau[:vitri:] + xau[vitri+1::]
    
def replace(xau,vitri,giatri):
    if(isinstance(xau, str)):
        return xau[:vitri:] + str(giatri) + xau[vitri+1::]
    else:
        return xau[:vitri:] + [giatri] + xau[vitri+1::]
  