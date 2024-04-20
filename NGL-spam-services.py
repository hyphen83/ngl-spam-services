import requests
import keyboard
import time
import random
import tkinter as tk
import threading

from tkinter import messagebox

print("""    

    _   __      __                                                             _               
   / | / /___ _/ /      _________  ____ _____ ___        ________  ______   __(_)_______  _____
  /  |/ / __ `/ /      / ___/ __ \/ __ `/ __ `__ \______/ ___/ _ \/ ___/ | / / / ___/ _ \/ ___/
 / /|  / /_/ / /___   (__  ) /_/ / /_/ / / / / / /_____(__  )  __/ /   | |/ / / /__/  __(__  ) 
/_/ |_/\__, /_____/  /____/ .___/\__,_/_/ /_/ /_/     /____/\___/_/    |___/_/\___/\___/____/  
      /____/             /_/                                                                   
""")
print("""
Made by: https://github.com/hyphen83
Im not responsible for anithing you do with this program. 
Only for educational purposes.
""")

runing = False
root = tk.Tk()
root.title("NGL BOT")
root.geometry("370x200")
root.config(bg="grey")

root_lable = tk.Label(root,text="Welcome to NGL bot spam",font=("Bebas Neue",15), bg="grey")
root_lable.pack(pady = 10)

def start():
    global runing
    global Phrase
    global Name
    runing = True
    Phrase = root_Entry2.get()
    Name = root_Entry.get()
    root.destroy()


Phrase = str()
Name = str()
root_Entry = tk.Entry(root, textvariable = Name,  font=("Bebas Neue", 15), bg="white", )
root_Entry.pack(pady=5)
root_Entry.insert(0,"Target username")
root_Entry2 = tk.Entry(root,text="Phrase to spam" , textvariable = Phrase,  font=("Bebas Neue", 15), bg="white", )
root_Entry2.pack(pady=5)
root_Entry2.insert(0,"Phrase to spam")
#my_button = Button(root, text="ok",  font=("Bebas Neue", 15), bg = "grey")
#my_button.pack(pady=10)
my_button2 = tk.Button(root, text="Start",command = start,  font=("Bebas Neue", 15), bg = "grey")
my_button2.pack(pady=10)

root.mainloop()




# Definice hlaviček a dat
url = "https://ngl.link/api/submit"
hlavicky = {
    "Host": "ngl.link",
    "Cookie": "_ga=GA1.1.1849455986.1706028122; __stripe_mid=7425abb8-480d-400a-85c7-1dab6820b11b913689; __stripe_sid=f48dec38-0a4a-41cf-80d5-c0c87c36f01e4d6540; mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18d37333dbcc3f-0f58e810f968ea-61325e53-1fa400-18d37333dbcc40%22%2C%22%24device_id%22%3A%20%2218d37333dbcc3f-0f58e810f968ea-61325e53-1fa400-18d37333dbcc40%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _ga_5DV1ZR5ZHG=GS1.1.1706028122.1.1.1706028196.0.0.0",
    "Content-Length": "132",
    "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Origin": "https://ngl.link",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": f"https://ngl.link/{Name}" ,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "cs-CZ,cs;q=0.9",
    "Priority": "u=1, i",
}

data = {
    "username": Name,
    "question": f"{Phrase}",
    "deviceId": "8ab1474b-b423-4e86-81ab-30ed28c93717",
    "gameSlug": "",
    "referrer": "",
}
pocet = 0


        

# Vytvoření okna
root2 = tk.Tk()
root2.title("NGL SENDING")
root2.config(bg="grey")

# Vytvoření proměnné pro label
label_var = tk.StringVar()
label_var.set("První aktualizace")

# Vytvoření labelu
label = tk.Label(root2, textvariable=label_var, font=("Helvetica", 16), bg="grey")
label.pack(padx=20, pady=20)












# Odeslání POST požadavku
def send():
    global runing
    global pocet
    global odpoved
    while runing:
    

    
        odpoved = requests.post(url, headers=hlavicky, data=data)
        pocet += 1
        # Výpis odpovědi
    
        
        time.sleep(random.uniform(1, 5))

        # Výpis odpovědi
        print(odpoved.status_code)
        print(F"{odpoved.text} pocet poslanych otazek: {pocet}")
    
        
    
        if keyboard.is_pressed("q"):
            runing = False
        if odpoved.status_code == 429:
            pocet -= 1
            time.sleep(15)


            


other_activity_thread = threading.Thread(target=send)
other_activity_thread.start()

time.sleep(5)



def update_label():
    
    global label_var
    
    while True:
        
        new_text = f"Number of sent messages: {pocet}    Response code: {odpoved.status_code}     Response message: {odpoved.text}"
        label_var.set(new_text)
        time.sleep(0.1)

label_thread = threading.Thread(target=update_label)
label_thread.start()




other_activity_thread2 = threading.Thread(target=root2.mainloop())
other_activity_thread2.start()
