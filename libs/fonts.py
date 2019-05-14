# -*- coding: utf-8 -*-

from colorama import Fore, Back, Style
import sys 

sys.ps1 = Fore.BLUE+Style.BRIGHT+"~>>> "+Style.RESET_ALL

newstl = Fore.WHITE+Style.BRIGHT
bacstl = Fore.RED+Style.NORMAL

banner = Fore.RED+"""
ooooo  oooo"""+newstl+"""  ooooooo"""+bacstl+"""     ooooooo8  
 888    88 """+newstl+"""o88     888"""+bacstl+""" o888    88  
  888  88  """+newstl+"""      o888 """+bacstl+""" 888    oooo 
   88888   """+newstl+"""   o888   o"""+bacstl+""" 888o    88  
    888    """+newstl+"""o8888oooo88"""+bacstl+"""  888ooo888  
ooooo             o88                         o8                        
 888  oo oooooo  oooo  ooooooooo8  ooooooo  o888oo ooooooo  oo oooooo   
 888   888   888  888 888oooooo8 888     888 888 888     888 888    888 
 888   888   888  888 888        888         888 888     888 888        
o888o o888o o888o 888   88oooo888  88ooo888   888o 88ooo88  o888o       
                 o88                                                    
"""+Style.RESET_ALL
