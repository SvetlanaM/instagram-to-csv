from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import csv
import os, glob
from urllib.error import URLError, HTTPError
import socket
import ssl

if __name__ == '__main__':
    final_list = []
    final_list.append(["code", "date", "comments", "likes", "caption", "image"])
    count = 0

    instagram_account = input("Enter the name of the instagram_account: ")
    def get_page(max_id):
        global count
        count += 1

        ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://www.instagram.com/" + instagram_account + "/?max_id=" + str(max_id)
        try:
            page = urlopen(url)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            exit(1)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            exit(1)
        soup = BeautifulSoup(page, "html.parser")
        HTML =str(soup)
        JSON = re.compile('window._sharedData = ({.*?});', re.DOTALL)

        matches = JSON.search(HTML)
        data = matches.group(1)

        try:
            json_acceptable_string = data.replace("'", "]")
            d = json.loads(json_acceptable_string)
            new_data = d["entry_data"]["ProfilePage"][0]["user"]["media"]["nodes"]
        except:
            print ("Data in older format")
            exit(1)

        for i in new_data:
            try:
                final_list.append([i["code"], i["date"], i["comments"]["count"], i["likes"]["count"], i["caption"], i["thumbnail_src"]])
            except:
                final_list.append([i["code"], i["date"], i["comments"]["count"], i["likes"]["count"], "", i["thumbnail_src"]])

        next_page = d["entry_data"]["ProfilePage"][0]["user"]["media"]["page_info"]["end_cursor"]
        next_true = d["entry_data"]["ProfilePage"][0]["user"]["media"]["page_info"]["has_next_page"]

        while next_true != False:
            get_page(next_page)
            break

    try:
        if count == 0:
            if instagram_account == "":
                print ("No instagram_account")
                exit(1)
    except socket.error as ex:
        print (ex)

    get_page(1)

    with open('csv/' + instagram_account + '.csv', 'w') as csv_file:
        a = csv.writer(csv_file, delimiter=',')
        data = final_list
        a.writerows(data)
