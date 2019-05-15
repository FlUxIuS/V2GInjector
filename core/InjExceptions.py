# -*- coding: utf-8 -*-

from colorama import Fore, Back, Style

class DecodeError(Exception):
    def __init__(self, message, errors):
        pmessage = "[-] {message} -> {errors}".format(
                                message=message,
                                errors=errors)
        self.message = Fore.RED+pmessage+Style.RESET_ALL

    def __str__(self):
        return self.message
