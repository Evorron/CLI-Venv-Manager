# Libraries
import os
import time
import venv

# Main Menu
def menu():
    clear_screen()
    print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
    print(f"\nMain Menu\n")
    print(f"1. Add Python Virtual Environment(Venv)")
    print(f"2. Manage Virtual Environments")
    print(f"0. Exit the Program")
    print(f"{"="*65}")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
# Menu for option 1
def menu_1():
    clear_screen()
    print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
    print(f"\nAdd Python Virtual Environment(Venv)")
    print(f"{"="*65}")
    venv_name = input("\nName of Virtual Environment:\n")
    path = input("\nEnter The File Path To Be Added (\"Blank\" -> Use Current Directory):\n")
    
    # Checks file path is specified or not
    if not path:
        path = os.getcwd()

    venv_info = [path, venv_name]
    venv_path = os.path.join(venv_info[0], venv_info[1])

    # Initial Checks
    if os.path.exists(venv_path):
        print(f"{"="*65}")
        print(f"\n\"{venv_path}\" Cannot Be Created As It Already Exists!\n\n>>> Please Specify A Different Path/Filename <<<")
        input("\nPress Enter To Continue... ")
        return menu_1()
    else:
        print(f"{"="*65}")
        print(f"\nVirtual Environment Can Created at \"{venv_path}\"")
        input("\nPress Enter To Continue...")

    # Confirm Creation OR Edit Path/Filename
    

    while True:
        clear_screen()
        print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
        print(f"\nConfirmation Menu\n")
        print(f"1. Create Virtual Environment - \"{venv_path}\"")
        print(f"2. Rename Virtual Environment")
        print(f"3. Specify New Directory")
        print("0. Cancel Creation")
        print(f"{"="*65}")
        option = input(f"\nSelect the following Option: ")

        # Create Virtual Environment
        if option == "1":
            try:
                venv.create(venv_path)
                for i in range(5,0,-1):
                    print(f"Creation Successful...Returning To Main Menu In: {i}", end="\r")
                    time.sleep(1)
                clear_screen()
                break
            except:
                print("Error: Creation Failed (Please Check The specified Path/Filename)")
                time.sleep(3)
        
        # Rename Virtual Environment
        elif option == "2":
            clear_screen()
            print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
            rename_venv = input(f"\nRenaming Virtual Environment to: \n")
            
            
            while True:
                if os.path.exists(os.path.join(venv_info[0], rename_venv)):
                    existing_path = os.path.join(venv_info[0], rename_venv)
                    print(f"{"="*65}")
                    print(f"\n\"{existing_path}\" Cannot Be Created As It Already Exists!\n>>> Please Specify A Different Path/Filename <<<")
                    input("\nPress Enter To Continue... ")
                    break
                
                else:
                    venv_info[1] = rename_venv
                    venv_path = os.path.join(venv_info[0], rename_venv)
                    print(f"{"="*65}")
                    print(f"\nVirtual Environment Can Created at \"{venv_path}\"")
                    input("\nPress Enter To Continue... ")
                    break


        # Specify New Directory
        elif option == "3":
            clear_screen()
            print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
            rename_path = str(input(f"\nSpecify New Directory (\"Blank\" -> Use Current Directory):\n"))
            
            while True:
                if rename_path == "":
                    rename_path = os.getcwd()
                    if os.path.exists(os.path.join(rename_path, venv_info[1])):
                        existing_path = os.path.join(rename_path, venv_info[1])
                        print(f"{"="*65}")
                        print(f"\n\"{existing_path}\" Cannot Be Created As It Already Exists!\n>>> Please Specify A Different Path/Filename <<<")
                        input("\nPress Enter To Continue... ")
                        break

                    else:
                        venv_info[0] = rename_path
                        venv_path = os.path.join(venv_info[0], venv_info[1])
                        print(f"{"="*65}")
                        print(f"\nVirtual Environment Can Created at \"{venv_path}\"")
                        input("\nPress Enter To Continue... ")
                        break


                else:
                    if os.path.exists(os.path.join(rename_path, venv_info[1])):
                        existing_path = os.path.join(rename_path, venv_info[1])
                        print(f"{"="*65}")
                        print(f"\n\"{existing_path}\" Cannot Be Created As It Already Exists!\n>>> Please Specify A Different Path/Filename <<<")
                        input("\nPress Enter To Continue... ")
                        break
                    
                    else:
                        venv_info[0] = rename_path
                        venv_path = os.path.join(venv_info[0], venv_info[1])
                        print(f"{"="*65}")
                        print(f"\nVirtual Environment Can Created at \"{venv_path}\"")
                        input("\nPress Enter To Continue... ")
                        break
        #
        elif option == "0":
            for i in range(5,0,-1):
                    print(f"Stopping Virtual Environment Creation... Returning To Main Menu In: {i}", end="\r")
                    time.sleep(1)
            clear_screen()
            break
        else:
            print(f"Please Enter A Valid Option")


# Menu for option 2
def menu_2():
    while True:
        clear_screen()
        print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
        print(f"\nManage Virtual Environments")
        print(f"\n1. View Virtual Environments")
        print(f"0. Return to Main Menu")
        print(f"{"="*65}")
        option = input("\nSelect the following Option: ")
        

        if option == "1":
            view_venv()

        elif option == "0":
            clear_screen()
            break
        

def view_venv():
    while True:
        clear_screen()
        print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
        print(f"\nView Virtual Environments\n")
        print(f"1. Search Virtual Environments On System")
        print(f"0. Return To Manage Virtual Environments")
        print(f"{"="*65}")
        option = input("\nSelect the following Option: ")

        venv_identifer = 'pyvenv.cfg'
        venv_count = 0

        if option == "1":
            clear_screen()
            print(f"\n{"="*20} Python Venv CLI Manager {"="*20}")
            print("\nSearching For A Virtual Environment On System")
            print(f"{"="*65}")
            
            search_env = input("Enter The Name To Search For (\"Blank\") -> List all Virtual Environments on System): \n")

            for drive in os.listdrives():
                print(f"\nSearching for {search_env} In {drive} Drive", end="\n")
                print(f"{"="*65}")
                for root, dirs, files in os.walk(drive):
                    if (f"\\$recycle.bin") not in root.lower() and root.endswith(search_env) and venv_identifer in files:
                        creation_date = time.ctime((os.path.getctime(root)))
                        print(f"{root} | Created: {creation_date}")

            print(f"{"="*65}")
            input("\nPress Enter to continue...")

        
        elif option == "0":
            clear_screen()
            break
        else:
            print("Invalid Option")


# Main function
def main():
    clear_screen()
    while True:
        menu()
        option = input(f"\nSelect The following Option: ")
        if option == "1":
            menu_1()
        elif option == "2":
            menu_2()
        elif option == "0":
            for i in range(5,0,-1):
                print(f"Exiting Program in... : {i}", end="\r",)
                time.sleep(1)
            clear_screen()
            return
        else:
            print("!! Invalid Option !!")

main()