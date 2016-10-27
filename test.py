from discordWebhooks import Webhooks, Attachments, Fields

url = "XXX"
wh = Webhooks(url, "Coucou tout le monde", "Pseudo")

at = Attachments(author_name = "Derpolino", color = "#ff0000", title = "Discord webhooks")

field = Fields("Version", "1.0", True)
at.addField(field)
field = Fields("Last update", "27/10/2016", True)
at.addField(field)
field = Fields("Changelog", "Initiale release !", False)
at.addField(field)

wh.addAttachment(at)

at = Attachments(author_name = "Github", color = "#0000ff", title = "Hello world")
wh.addAttachment(at)

wh.post()
