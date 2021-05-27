publish_key=""
subscribe_key=""
team_members=[]

def Configure_Program():
    mainf = open("Main.py","r")
    appf = open("app.py","w")

    codefile = mainf.readlines()
    for code in codefile:
        if "name_dict={" in code:
            print("[*]Adding Team names to Dictionary")
            line = "name_dict={"
            for name in team_members:
                 line = line +"\""+name+"\":0,"
            line = line[:-1] + "}"  
            try:   
                appf.write(line)
                print("\033[92m[+]Team names added Successfully \033[0m")
            except:
                print("\033[91m[-]Could not add Team Names \033[0m")

        elif "pnconfig.publish_key=" in code:
            print("[*]Adding Publish Key to File")
            line = "pnconfig.publish_key=\'"+publish_key+"\'\n"
            try:
                appf.write(line)
                print("\033[92m[+]Publish Key added Successfully \033[0m")
            except:
                print("\033[91m[-]Could not add Publish Key \033[0m")


        elif "pnconfig.subscribe_key=" in code:
            print("[*]Adding Subscribe Key to File")
            line = "pnconfig.subscribe_key=\'"+subscribe_key+"\'"
            try:
                appf.write(line)
                print("\033[92m[+]Subscribe Key added Successfully \033[0m")
            except:
                print("\033[91m[-]Could not add Subscribe Key \033[0m")

        else:
            appf.write(code)
	
    print()
    print("\033[92mConfiguration Successfull \033[0m")
    print("Run \"python3 app.py\" to run the chat app")
    mainf.close()
    appf.close()


print("Anon-Chat Configure Wizard")
print("==========================")
print()
print("Please read README.md before proceeding")
print()
print("Step 1:")
print()
print("Enter the pubnub publish key :")
publish_key=input(">>>")
print("Enter the pubnub subscribe key :")    
subscribe_key=input(">>>")
print()
print("Step 2:")
print()
print("Enter names of the team members in a single line, separated by a space :")
team_members = list(map(str, input("Enter a multiple value: ").split()))
print()
print("Configuring Program...")
print()
Configure_Program()

    