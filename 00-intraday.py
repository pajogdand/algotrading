from fyers_api import fyersModel
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app_id = config['fyers']['app_id']
app_secret_key = config['fyers']['app_secret_key']
access_token = config['fyers']['access_token']
redirect_uri = config['fyers']['redirect_uri']

fyers = fyersModel.FyersModel(app_id=app_id, secret_key=app_secret_key, 
                              redirect_uri=redirect_uri, token=access_token)

nifty50 = fyers.get_nse_quote('NIFTY 50')
price = nifty50['ltp']

order_id = fyers.place_order(tradingsymbol='NIFTY 50',
                             quantity=1,
                             transaction_type='BUY', 
                             order_type='LIMIT', 
                             product_type='INTRADAY',
                             price=price, 
                             limit_price=price,
                             stop_price=0,
                             validity='DAY', 
                             disclosed_quantity=0, 
                             trigger_price=0)

print('Order placed successfully:', order_id)
