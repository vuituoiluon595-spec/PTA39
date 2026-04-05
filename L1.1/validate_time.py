# in put 
input_time = input("")

#ham cat hh:mm:ss
def slipt_time(input_time):
    try:
        time_list = input_time.slpit(":")
        hour = int(time_list[0])
        minute = int(time_list[1])
        second = int(time_list[2])
        return hour , minute , second #tupl
    except :
        print("invalid time format")
        return None
    #ham kiem tra hop le 
    def vaildate_time(hour=None, minute=None, second=None):
        if hour == None or minute == None or second == None:
            return "khong hop le "
        if hour < 0 or hour > 23 :
            return "khong hop le "
        if minute < 0 or  minute > 59 :
            return "khong hop le "
        if second < 0 or second > 59:
            return "khong hop le "
        
        return "hop le"

    