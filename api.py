import os
import sys
import webapp2
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from google.appengine.api import mail
from google.appengine.api import app_identity
import cloudstorage as gcs

import config


class SendMail(webapp2.RequestHandler):
    def post(self):
        if self.request.headers['apikey'] != config.authkey:
            self.response.set_status(401)
        else:
            try:
                # get json request
                req = self.request.body
                req = json.loads(req)
                # prepare data
                sender = "{} <no_reply@{}.appspotmail.com>".format(req.get("from"), app_identity.get_application_id())
                receiver = req.get("to")
                subject = req.get("subject")
                body_header = req.get("body_header")
                body_footer = req.get("body_footer")
                attach_list = []
                body_img = "<br>"
                if len(req.get("attach_list")) > 0:
                    for x in req.get("attach_list"):
                        file = gcs.open(x)
                        file_name = x.split("/")
                        file_attach = mail.Attachment(file_name[-1], file.read())
                        attach_list.append(file_attach)
                if len(req.get("img_list")) > 0:
                    for i, x in zip(range(len(req.get("img_list"))), req.get("img_list")):
                        img_file = gcs.open(x)
                        img_name = x.split("/")
                        img_attach = mail.Attachment(img_name[-1], img_file.read(), content_id='<image{}>'.format(i))
                        attach_list.append(img_attach)
                        body_img += '''<img src="cid:image{}" alt="image{}"><br>'''.format(i, i)
                # send email
                message = mail.EmailMessage(sender=sender, 
                                            subject=subject)
                message.to = receiver
                message.html = '''<html><pre>%s<br>%s<br>%s</pre></html>''' % (body_header, body_img, body_footer)
                if len(attach_list) > 0:
                    message.attachments = attach_list
                message.send()
                self.response.set_status(200)
            except Exception:
                self.response.set_status(400)


app = webapp2.WSGIApplication([
    ('/api', SendMail),
], debug=True)