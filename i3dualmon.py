#!/usr/bin/env python3
import os,re
def getmonitors():
    monitors = os.popen("xrandr | grep ' connected '").readlines()
    if len(monitors)<=0:
        print("Sorry I can't find a monitor :(")
    else:
        mons = []
        for mon in monitors:
            mons.append(re.search('([A-Z-a-z-0-9]*)( connected )',mon).group(1))
        return mons
    
connected_mons = getmonitors()
formatted_mons = [connected_mons[0],connected_mons[1], connected_mons[0]]
 
left_of_primary = "xrandr --output {0} --auto --output {1} --left-of {2}".format(*formatted_mons)
right_of_primary = "xrandr --output {0} --auto --output {1} --right-of {2}".format(*formatted_mons)
if __name__ =='__main__':
    print("Menu::::Make::::Your::::Choice\n1. Second Monitor is left on the primary monitor.\n"+
    "2. Second Monitor is right on the primary monitor.")
    choice = input("Make your choice: ")
    try:
        if int(choice)==1:
            os.system(left_of_primary)
            print("Thanks for using...")
        elif int(choice)==2:
            os.system(right_of_primary)
            print("Thanks for using...")
        else:
            print("Wrong Selection..")
    except:
        print("Please press 1 or 2")
    