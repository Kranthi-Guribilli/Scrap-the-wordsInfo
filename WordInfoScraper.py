import requests
from bs4 import BeautifulSoup as bs
s="y"
while s=='y':
	try:
		word=input("Word: ")
		headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
		url=requests.get("https://dictionary.cambridge.org/dictionary/english/{}".format(word),headers=headers)
		total_content=url.content
		soup=bs(total_content,"html.parser")
		word=soup.find("span",attrs={"class":"hw dhw"}).text
		partsOfSpeech=soup.find("div",attrs={"class":"posgram dpos-g hdib lmr-5"}).text
		phonetic=soup.find("span",attrs={"class":"ipa dipa lpr-2 lpl-1"}).text
		meaning = soup.find("div",attrs={"class":"def ddef_d db"}).text
		example=soup.find("div",attrs={"class":"examp dexamp"}).text
		print("---------------------------------------------------------------------------------------------------")
		print("Word: ",word)
		print("Parts of speech: ",partsOfSpeech)
		print("Phonetic description: ",phonetic)
		print("Meaning:",meaning)
		print("Example: ",example)
		print("\n")

		#Storing the words for future reference in a text file 
		f=open("words.txt","a+")
		f.write("Word: "+word)
		#f.write("({})".format(phonetic))
		f.write("("+partsOfSpeech+")"+"\n"+"meaning:"+meaning+"\n"+"Example:"+example+"\n")
		f.write("\n\n")
		f.close()
	except AttributeError:
		print("Sorry, we didn't find the word")
	except requests.exceptions.ConnectionError:
		print("It seems your connection is too bad or no connection!!")
	s=input("Do you want to search for another one?[y/n]:")	
