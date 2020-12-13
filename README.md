# PyGPY21x
UART tool for GPY21x evaluation boards (EASY GPY211, EASY GPY211 LBB...)

### Install Python 
https://www.python.org/downloads/
### Install sw module of UART in Python
In Windows CMD, run command: pip install python
### Clone this repository  

# How to use
### Use in Python
Python  
>>>from gpy21x import gpy21x  
>>>g2 = gpy21x()  
>>>g2.mdior(2)  
read value: 0x67c9    
  
### Use in vscode + Jupyter
Install vscode from microsoft web site.  
Run vscode  
In File manu, Open Folder, to open the folder of cloned repository.  
Open the .py file, vscode will automatically notify to install Python and a serial of tool including Jupyter. Install them.  
Open the gpy211app.ipynb file, vscode will automatically notify to install IPyKernel. Install it.  
Use shift + return to run cells in gpy211app.ipynb.  
  
### Use in Jupyter only
It is recommended to run the application with Jupyter only install of with vscode + Jupyter. Because Jupyter alone can run as web server, user can run the application with web browser via network from remote site.  
Please google how to install and use Jupyter.  
  



