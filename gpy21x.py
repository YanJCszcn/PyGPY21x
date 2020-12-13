from ser03 import ser03
import time

class gpy21x(ser03):
	def __init__(self):
		ser03.__init__(self)
		self.phy_id = int(input("Input the phy_id: "))
		self.w(0xf480, 0)
		print ("write 0xf480 = 0")
		self.w(0xf480, 0)
		print ("Read reg 0xf480")
		self.r(0xf480)
		self.help()

	def help(self):
		print(" ")
		print("g2 = gpy21x()")
		print("g2.r(addr)                  read direct register.  g2.r(addr, 0) no print the read value.")
		print("g2.w(addr, value)           write the direct register.")
		print("g2.mdior(reg)               Or g2.mdior(reg, 0), no print.")
		print("g2.mdiow(reg, value)")
		print("g2.mmdr(dev, reg)           Or g2.mmdr(dev, reg, 0), no print.")
		print("g2.mmdw(dev, value)")
		print("g2.rc()                     re-open the serial port (in case board hardware reset).")
		print("g2.ss()                     serial port open or not.")
		print("g2.help()                   display this command list.")
		print(" ")

	def mdior (self, reg, pr = 1):
		a = self.phy_id*32+0x800+reg
		ser03.w(self, 0xf408, a)
		v = ser03.r(self, 0xf409)
		if (pr==1) :
			print("read value: 0x"+'%04x'%v)
		return v

	def r(self, addr, pr = 1):
		v = ser03.r(self, addr)
		if (pr==1) :
			print("read value: 0x"+'%04x'%v)
		return v

	def mdiow (self, reg, value):
		a = self.phy_id*32+0x400+reg
		ser03.w(self, 0xf40a, value)
		ser03.w(self, 0xf408, a)	
	
	def mmdr(self, dev, reg, pr = 1):
		self.mdiow(0xd, dev)
		self.mdiow(0xe, reg)
		self.mdiow(0xd, dev+0x4000)
		v = self.mdior(0xe, 0)
		if (pr==1) :
			print("read value: 0x"+'%04x'%v)
		return v

	def mmdw(self, dev, reg, value):
		self.mdiow(0xd, dev)
		self.mdiow(0xe, reg)
		self.mdiow(0xd, dev+0x4000)
		self.mdiow(0xe, value)
	
	def rc(self):
		ser03.rc(self)
		self.w(0xf480, 0)
		print ("write 0xf480 = 0")
        #not sure why, seems need write twice when first reg write operation after the board reset and serial port re-open.
		self.w(0xf480, 0)
		print ("Read reg 0xf480")
		self.r(0xf480)
