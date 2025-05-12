def check_str(entry:str, digit:bool=True, checkList:list=None) -> bool:
    """
    Return bool if str is digit or in list\n
    - digit==True -> Default
    - checkList==list[] -> True if in checklist[...]
    """

    checking = bool()
    if digit:
        try:
            float(entry)
            checking = True
        except:
            checking = False

    if checkList:
        checking = True if entry in checkList else False

    return checking
