import aminofix
import aminofix as amino
import asyncio
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
lz = []
def advertise(data):
    listusers = []
    for userId in data.profile.userId:
        listusers.append(userId)
    return listusers

async def main():
	client = amino.Client("19E59C8A47464ED6175052441C7D6778695B64E9966FBEEC4A595CA087646DB64C7DEEEC5A075DE695")
	email = input("Email >> ")
	password = input("Password >> ")
	msg = input("Message >> ")
	client.login(email=email, password=password)
	clients =  client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = amino.SubClient(comId=communityid, profile=client.profile)
	print("Sending Advertise")
	while True:
		try:
			users = sub_client.get_online_users(size=100)
			theusers = advertise(users)
			for i in lz:
				if i in theusers:
					theusers.remove(i)
			sub_client.start_chat(userId=theusers, message=msg)
			await asyncio.gather(*[asyncio.create_task(sub_client.start_chat(theusers, msg)) for _ in range(450)])
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
		except Exception as e:
			print(e)
			
asyncio.get_event_loop().run_until_complete(main())
