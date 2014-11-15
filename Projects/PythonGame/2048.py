#!/usr/bin/evn python
import wx
class MyFrame(wx.Frame):
	def __init__(self,parent,ID,title):
		wx.Frame.__init__(self,parent,ID,title,wx.DefaultPosition,wx.Size(250,50))
		panel=wx.Panel(self,-1)

		wx.Button(panel,-1,'Button1',(0,0))
		wx.Button(panel,-1,'Button2',(100,0))
		wx.Button(panel,-1,'Button3',(200,0))

class MyApp(wx.App):
	def OnInit(self):
		frame=MyFrame(None,-1,'layout.py')
		frame.Show(True)
		frame.Centre()
		return True

app = MyApp(0)
app.MainLoop()