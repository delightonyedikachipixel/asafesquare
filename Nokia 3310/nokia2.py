chat_menu = input("Select an option: ")
while True:
        print("\nCHAT")
        print("1. Start chat")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Starting chat...")
        elif choice == "0":
            back
        else:
            print("Invalid choice")


call_register = input("Select an option: ")
while True:
        print("\nCALL REGISTER")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Showing missed calls...")
        elif choice == "2":
            print("Showing received calls...")
        elif choice == "3":
            print("Showing dialled numbers...")
        elif choice == "4":
            print("Erasing recent call lists...")
        elif choice == "5":
            call_duration_menu()
        elif choice == "6":
            call_costs_menu()
        elif choice == "7":
            call_cost_settings_menu()
        elif choice == "8":
            print("Showing prepaid credit...")
        elif choice == "0":
            back
        else:
            print("Invalid choice")


call_duration = input("Select an option: ")
while True:
        print("\nSHOW CALL DURATION")
        print("1. Last call duration")
        print("2. All calls’ duration")
        print("3. Received calls’ duration")
        print("4. Dialled calls’ duration")
        print("5. Clear timers")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Last call duration...")
        elif choice == "2":
            print("All calls’ duration...")
        elif choice == "3":
            print("Received calls’ duration...")
        elif choice == "4":
            print("Dialled calls’ duration...")
        elif choice == "5":
            print("Clearing timers...")
        elif choice == "0":
            back
        else:
            print("Invalid choice")


call_costs_menu = input("Select an option: ")
while True:
        print("\nSHOW CALL COSTS")
        print("1. Last call cost")
        print("2. All calls’ cost")
        print("3. Clear counters")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Last call cost...")
        elif choice == "2":
            print("All calls’ cost...")
        elif choice == "3":
            print("Clearing counters...")
        elif choice == "0":
            back
        else:
            print("Invalid choice")


call_cost_settings = input("Select an option: ")
while True:
        print("\nCALL COST SETTINGS")
        print("1. Call cost limit")
        print("2. Show costs in")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Setting call cost limit...")
        elif choice == "2":
            print("Showing costs in...")
        elif choice == "0":
            back
        else:
            print("Invalid choice")


tones_menu = input("Select an option: ")
while True:
        print("\nTONES")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            print("Ringing tone...")
        elif c == "2":
            print("Ringing volume...")
        elif c == "3":
            print("Incoming call alert...")
        elif c == "4":
            print("Composer...")
        elif c == "5":
            print("Message alert tone...")
        elif c == "6":
            print("Keypad tones...")
        elif c == "7":
            print("Warning and game tones...")
        elif c == "8":
            print("Vibrating alert...")
        elif c == "9":
            print("Screen saver...")
        elif c == "0":
            back
        else:
            print("Invalid choice")


settings_menu = input("Select an option: ")
while True:
        print("\nSETTINGS")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            call_settings_menu()
        elif c == "2":
            phone_settings_menu()
        elif c == "3":
            security_settings_menu()
        elif c == "4":
            restore_factory_menu()
        elif c == "0":
            back
        else:
            print("Invalid choice")


call_settings = input("Select an option: ")
while True:
        print("\nCALL SETTINGS")
        print("1. Automatic redial")
        print("2. Speed dialling")
        print("3. Call waiting options")
        print("4. Own number sending")
        print("5. Phone line in use")
        print("6. Automatic answer")
        print("0. Back")

        c = input("Select an option: ")
        if c in ["1","2","3","4","5","6"]:
            print("Setting option", c)
        elif c == "0":
            back
        else:
            print("Invalid choice")


phone_settings_menu = input("Select an option: ")
while True:
        print("\nPHONE SETTINGS")
        print("1. Language")
        print("2. Cell info display")
        print("3. Welcome note")
        print("4. Network selection")
        print("5. Lights")
        print("6. Confirm SIM service actions")
        print("0. Back")

        c = input("Select an option: ")
        if c in ["1","2","3","4","5","6"]:
            print("Phone setting option", c)
        elif c == "0":
            back
        else:
            print("Invalid choice")


security_settings_menu = input("Select an option: ")
while True:
        print("\nSECURITY SETTINGS")
        print("1. PIN code request")
        print("2. Call barring service")
        print("3. Fixed dialling")
        print("4. Closed user group")
        print("5. Phone security")
        print("6. Change access codes")
        print("0. Back")

        c = input("Select an option: ")
        if c in ["1","2","3","4","5","6"]:
            print("Security option", c)
        elif c == "0":
            back
        else:
            print("Invalid choice")


restore_factory_menu = input("Select an option: ")
while True:
        print("\nRESTORE FACTORY SETTINGS")
        print("1. Restore")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            print("Restoring factory settings...")
        elif c == "0":
            back
        else:
            print("Invalid choice")


call_divert_menu = input("Select an option: ")
while True:
        print("\nCALL DIVERT")
        print("1. Divert options")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            print("Diverting...")
        elif c == "0":
            back
        else:
            print("Invalid choice")


games_menu = input("Select an option: ")
while True:
        print("\nGAMES")
        print("1. Snake")
        print("2. Space Impact")
        print("3. Bantumi")
        print("0. Back")

        c = input("Select an option: ")
        if c in ["1","2","3"]:
            print("Launching game", c)
        elif c == "0":
            back
        else:
            print("Invalid choice")


calculator_menu = input("Select an option: ")
while True:
        print("\nCALCULATOR")
        print("1. Open calculator")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            print("Calculator opened")
        elif c == "0":
            back
        else:
            print("Invalid choice")

reminders_menu = input("Select an option: ")
while True:
        print("\nREMINDERS")
        print("1. Add reminder")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            print("Adding reminder...")
        elif c == "0":
            back
        else:
            print("Invalid choice")


clock_menu = input("Select an option: ")
while True:
        print("\nCLOCK")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date setting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        print("0. Back")

        c = input("Select an option: ")
        if c in ["1","2","3","4","5","6"]:
            print("Clock option", c)
        elif c == "0":
            back
        else:
            print("Invalid choice")


profiles_menu = input("Select an option: ")
while True:
        print("\nPROFILES")
        print("1. General")
        print("2. Silent")
        print("3. Meeting")
        print("4. Outdoor")
        print("0. Back")

        c = input("Select an option: ")
        if c in ["1","2","3","4"]:
            print("Profile selected")
        elif c == "0":
            back
        else:
            print("Invalid choice")


sim_services_menu = input("Select an option: ")
while True:
        print("\nSIM SERVICES")
        print("1. Open SIM services")
        print("0. Back")

        c = input("Select an option: ")
        if c == "1":
            print("Opening SIM services...")
        elif c == "0":
            back
        else:
            print("Invalid choice")


