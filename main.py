import ollama
from collections import defaultdict
import os
import re
import json

import requests

api_ip = "10.42.0.47"

def get_response(prompt):

    # prompt = """What can be the next contextual passoword which easy to remember based on the cintextual information
    #     input = {
    #     "email" : "harshsharma2024@gmail.com",
    #     "password1" : "harsh123",
    #     "password2" : "harshsharma123"
    #     }

    #     Don;t write any extra information except the JSON output,
    #     predicted_password should be easy to remember and should be based on the input provided
    #     output format : {"password": predicted_password}
    #     """
    # print(get_response(prompt))

    response = ollama.generate(model='llama3.2:3b',
                                prompt=prompt)
    return response['response']


def get_api_call(email, password):
    r = requests.get(api_ip,params={"email":email, "password":password})

    data = r.json()
    return data

def main():
    st = ['a']
    dict_save = open("dict.txt", "a")
    for inp in st:
        addr = "/home/harsh/Downloads/BreachCompilation/data/h/" + inp

        # Create a map of emails to passwords
        dict = defaultdict(list)

        file = open(addr, "r", encoding="latin-1")

        print(addr)
        for line in file:
            try:
                email, password = re.split(r'[ ;:\t|]', line, maxsplit=1)
                email = email.split("@")[0]
                password = password[:-1]
                dict[email].append(password)    
            except:
                print(line)
                continue
            
            

        for email in dict:
            if len(dict[email])>=3:
                dict_save.write(email + " : " + str(dict[email]) + "\n")

        
        file.close()
    dict_save.close()



def compare_main_func():
    dict_file = open("dict.txt", "r")
    for line in dict_file:
        email, passwords = line.split(" : ")
        passwords = json.loads(passwords[1:-2].split(", "))
        data = ""

        data = get_api_call(email, passwords)
        predicted_passwords = data["password"]

        # Check 
    dict_file.close()
        

    


# def send_req():


if __name__ == "__main__":
    # main()

    



