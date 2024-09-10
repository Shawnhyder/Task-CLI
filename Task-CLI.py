import sys
# Defining main function
def main():

    argCount = len(sys.argv)
    if(argCount < 2):
        print("Must have atleast one argument other than the program name!")
        sys.exit()
    match argCount:
        case 2:
            # list
            if(sys.argv[2] == 'list'):
                print(3)
        case 3:
            # add "Description"
            #TODO: adding and making a new task to the list with given description returning an Id for the task
            # delete id
            #mark-in-progress id
            #mark-done id
            # list done
            # list todo
            # list in-progress

            print(3)
        case 4:
            print(4)
            # update id "description" 


# Using the special variable 
# __name__
if __name__=="__main__":
    main()