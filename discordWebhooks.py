#encode: utf-8

import json
import requests

class Webhooks():
    def __init__(self, url, content, username="", icon_url=""):
        self.url = url if "/slack" in url else url + "/slack"
        self.content = content
        self.username = username
        self.icon_url = icon_url
        self.formated = ""

        self.attachments = []

    def addAttachment(self, attachment):
        if attachment.__class__.__name__ == "Attachments":
            self.attachments.append(attachment)
        else:
            raise Exception("The attachment is not a correct attachment object")

    def format(self):
        data = {}
        data["username"] = self.username
        data["text"] = self.content
        data["icon_url"] = self.icon_url

        data["attachments"] = []
        for attachment in self.attachments:
            att = {}
            att["author_name"] = attachment.author_name
            att["author_icon"] = attachment.author_icon
            att["color"] = attachment.color
            att["pretext"] = attachment.pretext
            att["title"] = attachment.title
            att["title_link"] = attachment.title_link
            att["image_url"] = attachment.image_url
            att["footer"] = attachment.footer
            att["footer_icon"] = attachment.footer_icon
            att["ts"] = attachment.ts

            att["fields"] = []
            for field in attachment.fields:
                f = {}
                f["title"] = field.title
                f["value"] = field.value
                f["short"] = field.short
                att["fields"].append(f)

            data["attachments"].append(att)

        self.formated = json.dumps(data)

    def post(self):
        self.format()
        result = requests.post(self.url, data=self.formated).text
        if result == "ok":
            return True
        else:
            raise Exception("Error on post : " + str(result))

class Attachments(classmethod):
    def __init__(self, **args):
        self.author_name = args["author_name"] if "author_name" in args else ""
        self.author_icon = args["author_icon"] if "author_icon" in args else ""
        self.color = args["color"] if "color" in args else ""
        self.pretext = args["pretext"] if "pretext" in args else ""
        self.title = args["title"] if "title" in args else ""
        self.title_link = args["title_link"] if "title_link" in args else ""
        self.image_url = args["image_url"] if "image_url" in args else ""
        self.footer = args["footer"] if "footer" in args else ""
        self.footer_icon = args["footer_icon"] if "footer_icon" in args else ""
        self.ts = args["ts"] if "ts" in args else ""

        self.fields = []

    def addField(self, field):
        if field.__class__.__name__ == "Fields":
            self.fields.append(field)
        else:
            raise Exception("The field is not a correct field object")

class Fields():
    def __init__(self, title="", value="", short=False):
        self.title = title
        self.value = value
        self.short = short
