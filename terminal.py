import model

while True:

    command=input()
    parameters=command.split()

    if parameters[0]=="cwd":
        model.cwd()
    
    elif parameters[0]=="browser":
        if(len(parameters)==1):
            model.browser()
        else:
            model.browser(parameters[1])
    
    elif parameters[0]=="search":
        model.search(parameters[1:])

    elif parameters[0]=="image":
        model.image(parameters[1:])

    else:
        print("Invalid option")
