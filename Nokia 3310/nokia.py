phonebook_menu = input("select option:")
while True:
        print("\nPHONE BOOK")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b’card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice tags")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            print("Searching...")
        elif choice == "2":
            print("Showing service numbers...")
        elif choice == "3":
            print("Adding name...")
        elif choice == "4":
            print("Erasing contact...")
        elif choice == "5":
            print("Editing contact...")
        elif choice == "6":
            print("Assigning tone...")
        elif choice == "7":
            print("Sending business card...")
        elif choice == "8":
            options_menu()
        elif choice == "9":
            print("Speed dials...")
        elif choice == "10":
            print("Voice tags...")
        elif choice == "0":
            break
        else:
            print("Invalid choice")




messages_menu = input("Select option:")
while True:
        print("\nMESSAGES")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Writing message...")
        elif choice == "2":
            print("Opening inbox...")
        elif choice == "3":
            print("Opening outbox...")
        elif choice == "4":
            print("Opening picture messages...")
        elif choice == "5":
            print("Opening templates...")
        elif choice == "6":
            print("Opening smileys...")
        elif choice == "7":
            message_settings_menu()
        elif choice == "8":
            print("Opening info service...")
        elif choice == "9":
            print("Voice mailbox number...")
        elif choice == "10":
            print("Service command editor...")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


message_settings_menu = input("Select option:")
while True:
        print("\nMESSAGE SETTINGS")
        print("1. Set 1")
        print("2. Common")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            set_1_menu()
        elif choice == "2":
            common_menu()
        elif choice == "0":
             back
        else:
            print("Invalid choice")

set_1_menu = input("Select option:")
while True:
        print("\nSET 1")
        print("1. Message centre number")
        print("2. Messages sent as")
        print("3. Message validity")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Message centre number...")
        elif choice == "2":
            print("Messages sent as...")
        elif choice == "3":
            print("Message validity...")
        elif choice == "0":
             back
else:
              print("Invalid choice")


common_menu = input("Select an option:")
while True:
        print("\nCOMMON")
        print("1. Delivery reports")
        print("2. Reply via same centre")
        print("3. Character support")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            print("Delivery reports...")
        elif choice == "2":
            print("Reply via same centre...")
        elif choice == "3":
            print("Character support...")
        elif choice == "0":
            back
else:
            print("Invalid choice")





