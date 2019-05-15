# -*- coding: utf-8 -*-

#    V2GInjector is a tool to penetrate V2G network through PowerLine, monitor and inject traffic
#    Copyright (C) 2019  Sebastien Dudek (@FlUxIuS)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
