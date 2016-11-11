#Examples using all parameters

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from discordWebhooks import Webhook, Attachment, Field

url = "https://ptb.discordapp.com/api/webhooks/246756716346212352/hztlLeSpjVaEKegZNivD6gvUA86wdRLmIx29_g2onRIGuaYD0pZfVor8LcNnhpSHnBtR"
wh = Webhook(url, "Text content", "Username", "https://www.facebook.com/favicon.ico")

at = Attachment(author_name = "Author Name", author_icon = "https://www.facebook.com/favicon.ico", color = "#ffffff", pretext = "pretext", title = "title (with title_link)", title_link = "http://github.com", image_url = "http://www.cekane.fr/wp-content/uploads/2015/10/googlelogosept12015.png", footer = "footer (with footer_icon)", footer_icon = "https://www.facebook.com/favicon.ico", ts="1000197000")

field = Field("Field title", "Field value with Short (aligned)", True)
at.addField(field)
field = Field("Field title", "Field value with Short (aligned)", True)
at.addField(field)
field = Field("Field title", "Field value with Short (aligned)", True)
at.addField(field)
field = Field("Field title", "Field value without Short", False)
at.addField(field)
field = Field("Field title", "Field value without Short", False)
at.addField(field)

wh.addAttachment(at)

at = Attachment(author_name = "Second Attachment Author Name", color = "#0000ff", title = "Title")
wh.addAttachment(at)

wh.post()
