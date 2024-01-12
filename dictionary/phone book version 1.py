def phone_book():
    group = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit: "))
        if command == 3:
            break
        elif command == 2:
            name = input("name:")
            phone = int(input("phone number: "))
            group[name] = phone
            print("ok!")
        elif command == 1:
            name = input("name: ")
            if name in group:
                print(f"{group[name]}")
    print("quitting...")
phone_book()
