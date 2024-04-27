from random import choice, randint
from typing import Union
from dotenv import load_dotenv
from discord import Intents, Client, Message
import time


def get_response(user_input: str, caller:str) -> Union[str,None]:
    lowered: str = user_input.lower()
    last_ppp_time = last_stored_time()[0]
    last_ppp_caller = last_stored_time()[1]
    timern = int(time.time())
    if lowered == "!help":
        return "!timern\n!lastppp or !timesincelastppp\n!pppinfo"
    elif lowered == "!ppp":
        return_message = f"First ppp since <t:{last_ppp_time}:R>"
        add_new_time(timern,caller)
        return return_message
    elif lowered == "!timern":
        return f"timern is <t:{timern}:R>"
    elif lowered == "!lastppp":
        return f"The most recent PPP was <t:{last_ppp_time}:R> by {last_ppp_caller}"
    elif lowered == "!timesincelastppp":
        return f"The most recent PPP was <t:{last_ppp_time}:R> by {last_ppp_caller}"
    elif lowered == "!pppinfo":
        pppinfo_list = ppp_info()
        return f"The 5 most recent PPPs have been at:\n<t:{pppinfo_list[0].split(",")[0]}:R> by {pppinfo_list[0].split(",")[1]}\n<t:{pppinfo_list[1].split(",")[0]}:R> by {pppinfo_list[1].split(",")[1]}\n<t:{pppinfo_list[2].split(",")[0]}:R> by {pppinfo_list[2].split(",")[1]}\n<t:{pppinfo_list[3].split(",")[0]}:R> by {pppinfo_list[3].split(",")[1]}\n<t:{pppinfo_list[4].split(",")[0]}:R> by {pppinfo_list[4].split(",")[1]}"
    else:
        return None



current_log = "ppplog.csv"

def last_stored_time() -> Union[str,int]:
    ppp_log = open(current_log,"r")
    last_ppp_str = ppp_log.readlines()[-1]
    ppp_log.close()
    return last_ppp_str.split(",")

def add_new_time(input_string: Union[int,str], caller: str) -> None:
    ppp_log = open(current_log,"a")
    ppp_log.write(f"\n{input_string},{caller}")
    ppp_log.close


def ppp_info():
    ppp_log = open(current_log,"r")
    last_ppp_str = ppp_log.readlines()[-5:]
    ppp_log.close()
    
    return last_ppp_str

def main() -> None:
    print(get_response("!pppinfo","TsubiClub"))

if __name__ == "__main__":
    main()