print("Converts xbox-now.com discount list to CSV")

games_list = []

def import_games():
    global games_list
    cleanup = [["â€™s","'"],["Â®",""],["â„¢",""],["â€”","-"],["Ã¶k","o"]]
    print("Enter a filename below (incl. extension) or BLANK for try.txt: ")
    filename = input("Filename: ").lower()
    if filename == "": filename = "try.txt"
    importfile = open(filename,"r")
    newrecord,output = True,["","","","",""]
    for line in importfile:
        if newrecord: #First Line is the title
            title = line.strip() #Strip and splitting need to be separate lines
            title = title[:len(title)//2]
            for item in cleanup:
                title = title.replace(item[0],item[1])
            output [0] = title
            newrecord = False
        elif line[0:10] == "Deal until": # Pickup Date
            usdate = line[12:-11].split("/")
            output[3] = usdate[1]+"/"+usdate[0]+"/"+usdate[2]
        elif line[0:5] == "from:": # Pickup price
            output[1] = line[6:-5]
        elif line[2] == "%" and len(line) < 20: #Pickup Discount
            output[2] = "0."+line[0:2]
        elif line[0:3] == "NEW": # Pickup NEW
            output[4] = "new"
        elif line[0:5] == "save ": # End of record
            games_list.append(output)
            newrecord = True
            output =["","","","",""]
    print("Successfully imported {} games.".format(len(games_list)))
    importfile.close()

def print_screen():
    global games_list
    print("You can sort the list by (t)itle*, (p)rice or (discount).")
    sort = input("Sort by: ")
    print("The are {} games. Show all* games or limit to a number per page?".format(len(games_list)))
    pagination = input("Games per page: ")
    if sort in ["p","d"]:
        games_list.sort(key = lambda x: x[1])
        games_list.sort(key = lambda x: x[2])
    else:
        games_list.sort(key = lambda x: x[0])
    print("Title - Price - Disc - Date - New")
    if pagination != "" and pagination.isdigit():
        pagination = int(pagination)
        for i in range(len(games_list)):
            print(" - ".join(games_list[i]))
            if i>0 and i%pagination == 0:
                  if input("q to quit of ENTER for next page: ").lower() == "q":
                      return
    else:
        for game in games_list:
            print(" - ".join(x for x in game))
        
def export_csv():
    global games_list
    confirm = "n"
    while confirm.lower() != "y":
        print("\nPlease enter a filename (incl. extension) or leave blank for export.csv")
        filename = input("Filename: ")
        if filename == "": filename = "export.csv"
        print("If {} exists, it will be overwritten.".format(filename))
        confirm = input("Please type y to confirm: ")
    open(filename,"w").close()
    exportfile = open(filename,"a")
    exportfile.write("\"Title\",\"Price\",\"Disc\",\"Date\",\"New\"\n")
    for game in games_list:
        exportfile.write("\""+"\",\"".join(x for x in game)+"\"\n")
    print("CSV exported.")
    exportfile.close()

def menu():
    choice =""
    while choice.lower() != "q":
        import_games()
        print("\nDo you want to display the games imported on screen?")
        choice = input("Display to Screen? (y*/n): ")
        if choice.lower() != "n":
            print_screen()
        print("\nDo you want to export the games as a CSV file?")
        choice = input("Export to CSV? (y*/n): ")
        if choice.lower() != "n":
            export_csv()
        choice = input("\nType q to quit or ENTER to re-do: ")
    exit()
menu()
