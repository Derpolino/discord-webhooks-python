from discordWebhooks import Webhook, Attachment, Field

url = "XXX"
wh = Webhook(url, "Coucou tout le monde", "Pseudo")

at = Attachment(author_name = "Derpolino", color = "#ff0000", title = "Discord webhooks")

field = Field("Version", "1.0", True)
at.addField(field)
field = Field("Last update", "27/10/2016", True)
at.addField(field)
field = Field("Changelog", "Initiale release !", False)
at.addField(field)

wh.addAttachment(at)

at = Attachment(author_name = "Github", color = "#0000ff", title = "Hello world")
wh.addAttachment(at)

wh.post()
