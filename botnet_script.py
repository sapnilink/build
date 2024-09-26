import requests, csv, subprocess, tkinter, customtkinter
import ctypes, sys
ctypes.windll.shell32.IsUserAnAdmin() or (ctypes.windll.shell32.ShellExecuteW(
    None, "runas", sys.executable, " ".join(sys.argv), None, 1) > 32, exit())
#tkinter settings
customtkinter.set_appearance_mode("Dark")
app= customtkinter.CTk()
app.geometry("350x210")
app.title("Windows Firewall Blocker")
#custom script to block botnet ips
def button():
    responce = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text
    rule="netsh advfirewall firewall delete rule name = 'Bad IP' "
    subprocess.run(["Powershell", "-Command", rule])
    mycsv= csv.reader(filter(lambda x: not x.startswith("#"), responce.splitlines()))
    for row in mycsv:
        ip=row[1]
        if (ip)!=("dst_ip"):
            print("Added rule to block:", ip)
            rule = "netsh advfirewall firewall add rule name = 'Bad IP' Dir=Out Action=Block Remoteip=" +ip
            subprocess.run(["Powershell", "-Command", rule])
            rule = "netsh advfirewall firewall add rule name = 'Bad IP' Dir=In Action=Block Remoteip="+ip
            subprocess.run(["Powershell", "-Command", rule])

#reset button
def reset_button():
    rule = "netsh advfirewall firewall delete rule name = 'Bad IP' "
    subprocess.run[("Powershell", "-Command", rule)]
#exit button
def exit_button():
    sys.exit()
#button placement    
button = customtkinter.CTkButton(app, text="Run Script", command=button)
button.place(relx=0.5, rely=0.5, anchor="center")
exit_button=customtkinter.CTkButton(app, text="Exit", command=exit_button)
exit_button.place(relx=0.3, rely=0.7)
reset_button= customtkinter.CTkButton(app, text= "Reset all changes", command=reset_button)
reset_button.place(relx=0.6, rely=0.6)
#run app
app.mainloop()
