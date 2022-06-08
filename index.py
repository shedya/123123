# -*- coding: utf8 -*-
import requests
import io
import json
import bs4
def main_handler(event, context):

    param = event["queryString"]
    uid = param["uid"]
    html = str(requests.get("https://enka.shinshin.moe/u/" + uid).content, "utf-8")
    bs = bs4.BeautifulSoup(html, features="html.parser")
    name = bs.find(name="h1", attrs={"class": "svelte-qvi7br"}).text
    sign = bs.find(name="div", attrs={"class": "signature svelte-qvi7br"}).text
    img_url = bs.find(name="img", attrs={"class": "svelte-qvi7br"}).get("src")
    string = bs.find(name="div", attrs={"class": "ar svelte-qvi7br"}).text
    ar = string.replace("AR ","")[:string.find("WL")-3]
    resp = {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"name":name,"sign":sign,"img_url":"https://enka.shinshin.moe"+img_url,"ar":ar})
        }

    return resp
