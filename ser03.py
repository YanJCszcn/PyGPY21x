import serial, string
import serial.tools.list_ports

class ser03:
	def __init__(self, pr = 0):
		if (pr == 1):
			print("Class ser03: portx, rate, timout.")
			print("             list_ports(), open_port(\"COMx\"), close_ports(), rc() reconnect.")
			print("             r(addr), w(addr, value).")
		self.list_ports()
		#pn = raw_input("Please input the port name (e.g. COMx): ")
		pn = input("Please input the port name (e.g. COMx): ")
		self.open_port(pn)
		
	def list_ports(self): 
		pl = list(serial.tools.list_ports.comports())
		#print(pl)
		if len(pl) == 0:
			print('No serial port found.')
		else:
			for i in range(0,len(pl)):
				print(pl[i])
		
	def open_port(self, portx, bps = 115200, timex = 5):		
		try:
			self.portx = portx
			self.bps = bps
			self.timex = timex
			self.ser=serial.Serial(self.portx, self.bps, timeout = self.timex)
			print ("Open serial port at: "+portx)
		except Exception as e:
			print("Failed to open serial port: "+portx,e)
    
	def rev(self):
		r = ""
		while True:
			if self.ser.in_waiting:
				str8=self.ser.read(self.ser.in_waiting ).decode("utf-8")
				if str8[-1]==">":
					#print("rev:",str)
					r = r+str8
					break
				else:
					#print("rev1:",str)
					r = r+str8
		return r
	
	def r(self, addr):
		addr = '%#06x'%addr
		addr = addr[2:6]
		sercom = "r "+addr+"\r\n"
		#print(sercom)
		result=self.ser.write(sercom.encode())
		ret = self.rev()
		#print("long: "+ret)
		ret = ret[8:12]
		#print("read value: 0x"+ret)
		#return string.atoi(ret, 16)
		return int(ret, 16)
	
	def w(self, addr, value):
		addr = '%#06x'%addr
		addr = addr[2:6]
		v = '%#06x'%value
		v = v[2:6]
		sercom = "w "+addr+" "+v+"\r\n"
		#print (sercom)
		result=self.ser.write(sercom.encode())
		self.rev()

	def close_port(self):
		try:
			self.ser.close()
			print ("Now close port at: "+self.ser.name)
		except:
			print ("Failed to close serial port: "+self.ser.name)
	
	def rc(self):
		self.close_port()
		self.open_port(self.portx)
					
	def ss(self):
		print( self.ser.isOpen() )


