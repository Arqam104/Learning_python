import json
def load_anime():
    with open("anime_data.json","r") as file :
        data=json.load(file)
        return data 
def save_anime():
    with open ("anime_data.json","w") as file:
        json.dump(anime_list,file,indent=4)

def print_menu():
    while True:
        print("================================")
        print("        🎌 ANIME TRACKER")
        print("================================")

        print("1. Add Anime")
        print("2. View Anime")
        print("3. Update Anime")
        print("4. Delete Anime")
        print("5. Search Anime")
        print("6. Statistics")
        print("7. Exit")
        choice=input("choose an option :")
        if choice=="1":
            add_anime()
        elif choice=="2":
            view_anime()  
        elif choice=="3":
            update_anime() 
        elif choice=="4":
            remove_anime() 
        elif choice=="5":
            search_anime()
        elif choice=="6":
            statistics()            
        elif choice=="7":
            print("goodbye!")
            break
        else:
            print("invalid option")

def choose_status():
    statuses=[
        "completed",
        "watching",
        "plan to watch",
        "On hold",
        "Dropped"
    ]
    for i,status in enumerate(statuses,start=1):
        print(f"{i}.{status}")
    while True:
        try:
            chose_status=int(input("Choose your Status:"))
            if 1<=chose_status<=5:
                break
            else:
                print("please Enter Valid number ")
        except ValueError:
            print("Enter a number ")
    return statuses[chose_status-1]



anime_list=load_anime()
def add_anime():
    title=input("Enter Anime Name :")
    while True: 
        try:   
            total_eps=int(input("Enter No of Total Episodes:"))
            if total_eps>0:
                break 
            else:
                print("Total eps should be greater than 0")
        except ValueError:
            print("please Enter Number ")
    while True:
        try:
            eps_watched=int(input("Enter no eps you've watched:"))
            if 0<=eps_watched<=total_eps:
                break
            else:
                print("You cant watch more eps than anime has, Dumb")
        except ValueError:
            print("Please Enter Number")
    status=choose_status() 
    while True:
        try:
            rating=float(input("Give rating out of 10:"))
            if  0<=rating <=10:
                break 
            else:
                print("Rating must be between 0 and 10")
        except ValueError:
            print("Please Enter Number ")
    anime_data={
        "title":title,
        "total_eps":total_eps,
        "eps_watched":eps_watched,
        "status":status,
        "rating":rating
            }
    anime_list.append(anime_data)
    save_anime()
    print(f"{title} is added sucessfully")
def view_anime():
    if not anime_list:
        print("No anime in your list")
        return
    print("\n============= My Anime ===================")
    for i,anime in enumerate(anime_list,start=1):        
        print(f"\n{i}.Title:{anime['title']}")
        print(f"episodes:{anime['eps_watched']}/{anime['total_eps']}")
        print(f"Status:{anime['status']}")
        print(f"Rating:{anime['rating']}/10")
def update_anime():
    view_anime()
    while True:
        try:
            user_choice=int(input("which anime do you want to update "))
            if 0<user_choice<=len(anime_list):
                selected_anime=anime_list[user_choice-1]
                break 
            else:
                print("please enter valid anime number")
        except ValueError:
            print("please enter number")
    while True:
        change=input("what do you want to change \n 1.eps watched \n 2.status \n 3.rating:")
        if change=="1":
            while True:
                try:
                    new_eps=int(input("Enter new eps watched:"))
                    if 0<=new_eps<=selected_anime["total_eps"]:                    
                        selected_anime["eps_watched"]=new_eps
                        save_anime()
                        break
                    else:
                        print("You cant watch more eps than anime has, Dumb")
                except ValueError:
                    print("Please Enter Number")
        elif change=="2":
            new_status=choose_status()
            selected_anime["status"]=new_status
            save_anime()
        elif change=="3":
            while True:
                try:
                    new_rating=float(input("Enter new rating out of 10"))
                    if 0<=new_rating <=10:
                        break
                    else:
                        print("Rating must be between 0 and 10")
                except ValueError:
                    print("please enter number")
            selected_anime["rating"]=new_rating
            save_anime()
        else:
            print("Invalid Option")
        upd_check=input("press Enter to keep updating or q to quit updating")
        if upd_check=="q":
             break
def remove_anime():
    view_anime()
    while True:
        try:
            user_rem=int(input("Which anime do you want to remove, Enter its number"))
            if 0<user_rem<=len(anime_list):
                deleted_anime= anime_list.pop(user_rem-1)
                save_anime()
                print(f"{deleted_anime['title']} deleted successfully")
                rem_check=input("Press Enter to keep removing or s to stop ")
                if rem_check=="s":
                    break
            else:
                print("please enter valid anime no")  
        except ValueError:
            print("please Enter number")
def search_anime():
    search_anime=input("Which anime do you want to Search").lower()
    found=False
    for anime in anime_list:
        if search_anime in anime["title"].lower():
            print("============== Search Result =================")
            print(f"Title: {anime['title']}")
            print(f"Episodes:{anime['eps_watched']}/{anime['total_eps']}")
            print(f"Status:{anime['status']}")
            print(f"Rating:{anime['rating']}/10")
            found=True
    if not found:
        print("this anime is not in your list ")
def statistics():
    if not anime_list:
        print("No anime in your list")
        return
    print(f"Total Anime:{len(anime_list)} ")
    completed=0
    watching=0
    plan_to_watch=0
    for anime in anime_list:
        if anime['status'].lower()=="completed":
            completed +=1
        elif anime['status'].lower()=="watching":
            watching+=1
        elif anime['status'].lower()=="plan to watch":
            plan_to_watch+=1
    print(f"Completed Anime:{completed}")
    print(f"Watching:{watching}")
    print(f"plan to watch:{plan_to_watch}")
    total_eps=0
    total_rating=0
    for anime in anime_list:
        total_eps+=anime['eps_watched']
        total_rating+=anime['rating']
    print(f"Total eps watched:{total_eps}")
    print(f"Average Rating is {total_rating/len(anime_list)}")
    comp_per=(completed/len(anime_list))*100
    print(f"Completion Rate: {comp_per}%") 
print_menu()



