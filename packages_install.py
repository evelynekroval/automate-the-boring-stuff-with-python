spaced_packages = """beautifulsoup4==4.12.3
matplotlib
openpyxl==3.1.5
pdfminer.six==20240706
pillow==10.4.0
playsound3==2.4.0
playwright==1.47.0
PyPDF==5.0.1
python-docx==1.1.2
pyttsx3==2.98
requests==2.32.3
selenium==4.25.0
send2trash==1.8.3
xmltodict==0.13.0
bext
ezgmail
ezsheets
humre
pyautogui
pymsgbox
pyperclip
pyperclipimg
yt-dlp"""


unspaced_packages = "pip install " + " ".join(spaced_packages.split("\n"))
print(unspaced_packages)
