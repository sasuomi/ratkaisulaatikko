 # This Python file uses the following encoding: utf-8

from google.appengine.api import mail

def sendConfirmationEmail(name, email):
	mail.send_mail(sender="Ratkaisulaatikko <ratkaisulaatikko@ratkaisulaatikko.appspotmail.com>",
	              to=name + " <" + email + ">",
	              subject="Vahvista sähköpostiosoitteesi - Ratkaisulaatikko",
	              body="""
	Hei,

	Olet melkein valmis! Klikkaa alla olevaa linkkiä, jotta voimme varmistaa sähköpostiosoitteesi:

	http://ratkaisulaatikko.appspot.com/vahvista?id=123456789

	Terveisin,
	Ratkaisulaatikko
	""")
def tempSendSolutionMail():
	sendSolutionPageLink("Samuli Suomi", "samulisuomi@yahoo.fi")

def sendSolutionPageLink(name, email):
	mail.send_mail(sender="Ratkaisulaatikko <ratkaisulaatikko@ratkaisulaatikko.appspotmail.com>",
              to=name + " <" + email + ">",
              subject="Ratkaisulinkkisi - Ratkaisulaatikko",
              body="""
	Hei,

	Voit seurata ongelmasi tilannetta seuraavalla sivulla:

	http://ratkaisulaatikko.appspot.com/ratkaisusivu?id=a1b2c3d4e5

	Voit tallentaa sivun myös kirjanmerkiksi.

	Terveisin,
	Ratkaisulaatikko
	""")

def tempSendNewOffersNotification():
	sendNewOffersNotification("Samuli Suomi", "samulisuomi@yahoo.fi")

def sendNewOffersNotification(name, email):
	mail.send_mail(sender="Ratkaisulaatikko <ratkaisulaatikko@ratkaisulaatikko.appspotmail.com>",
              to=name + " <" + email + ">",
              subject="Uusia tarjouksia ongelmaasi! - Ratkaisulaatikko",
              body="""
	Hei,

	Olet saanut uusia tarjouksia ongelmaasi. Voit tarkastella niitä ratkaisusivullasi:

	http://ratkaisulaatikko.appspot.com/ratkaisusivu?id=a1b2c3d4e5demo

	Terveisin,
	Ratkaisulaatikko
	""")
