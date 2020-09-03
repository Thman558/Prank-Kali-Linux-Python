



print("#################")
print("# Made By Riley #")
print("#     Enjoy!    #")
print("#  (Give Most   #")      
print("# Of The credit #")
print("#    To Alex    #")
print("#---------------#")
print("# |Fake Linux|  #")
print("#################")


def output1():
    
    no_response_cmds = ['Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']
    response_cmds = ['ls', 'pwd', 'alias', 'cd {ls}', 'find']

    print('Enter --help for available commands.')

    def output2():
        output = ''
        Cmdd = input(f'root@kali:~$ ')
        if Cmdd == '--help':
            output = f'{response_cmds}'
            pass
        elif Cmdd == f'ls':
            output = f'{no_response_cmds}'
            pass
        elif Cmdd == 'pwd':
            output = f'/Users/'
            pass
        elif Cmdd == 'alias':
            output = f'Unable to create alias'
            pass
         Hello123 = input(f'root@kali:~ ')
         if Hello123 == 'find':
            print('What Would You Like to Find?
                  if input == 'Desktop':
                  print(f'/Users/Desktop')
            pass
        elif Cmdd == 'cd':
            print('Enter directory name from ls or enter "back". (Enter "ls" for available directories)')
            directory = input()
            for command in no_response_cmds:
                if directory == command:
                    output = f'Nothing Here....'
                    break
                elif directory == 'back':
                    output = 'As you wish...'
                    break
                elif directory == 'ls':
                    print(f'{no_response_cmds}')
                    directory2 = input('Directory: ')
                    for command2 in no_response_cmds:
                        if directory2 == command2:
                            output = f'Nothing Here Bro'
                            break
                        else:
                            output = "Error: Directory Not Found"
                    break
                else:
                    output = "Error: Directory Not Found"
        else:
            output = "Error: Command Not Found"
        print(output)
    # End of def output2()

    output2()
    run_request = input(f'Another? [y/n]')
    if run_request == 'y':
      output2()
    else:
      print('Thank you. Request complete.')
# End of def output1()

output1()
