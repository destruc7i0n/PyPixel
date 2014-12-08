
import urllib2

def urlopen(url, params):
	req = urllib2.Request(url, params, { 'User-Agent': 'Mozilla/5.0' }) # lol spoofed the user agent as firefox, seems legit
	html = urllib2.urlopen(req).read()
	return html


import json

class HypixelAPI:
	base = "https://api.hypixel.net/"
	def __init__(self, key):
		self.key = key
		self.baseParams = {"key": self.key}
	def keyRequest(self):
		url = self.base + "key"
		params = self.baseParams
		return json.loads(urlopen(url, params))
	def friends(self, username):
		url = self.base + "friends"
		params = self.baseParams
		params["player"] = username
		return json.loads(urlopen(url, params))
	def guildByMember(self, username):
		url = self.base + "findGuild"
		params = self.baseParams
		params["byPlayer"] = username
		return json.loads(urlopen(url, params))
	def guildByName(self, name):
		url = self.base + "findGuild"
		params = self.baseParams
		params["byName"] = name
		return json.loads(urlopen(url, params))
	def guildByID(self, guildId):
		url = self.base + "guild"
		params = self.baseParams
		params["id"] = guildID
		return json.loads(urlopen(url, params))
	def session(self, username):
		url = self.base + "session"
		params = self.baseParams
		params["player"] = username
		return json.loads(urlopen(url, params))
	def userByUUID(self, uuid):
		url = self.base + "player"
		params = self.baseParams
		params["uuid"] = uuid
		return json.loads(urlopen(url, params))
	def userByName(self, name):
		url = self.base + "player"
		params = self.baseParams
		params["name"] = name
		return json.loads(urlopen(url, params))


