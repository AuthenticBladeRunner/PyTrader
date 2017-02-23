# encoding: UTF-8

# 默认空值
EMPTY_STRING = ''
EMPTY_UNICODE = ''
EMPTY_INT = 0
EMPTY_FLOAT = 0.0

# 方向常量
DIRECTION_NONE = '无方向'
DIRECTION_LONG = '多'
DIRECTION_SHORT = '空'
DIRECTION_UNKNOWN = '未知'
DIRECTION_NET = '净'
DIRECTION_SELL = '卖出'      # IB接口

# 开平常量
OFFSET_NONE = '无开平'
OFFSET_OPEN = '开仓'
OFFSET_CLOSE = '平仓'
OFFSET_CLOSETODAY = '平今'
OFFSET_CLOSEYESTERDAY = '平昨'
OFFSET_UNKNOWN = '未知'

# 状态常量
STATUS_NOTTRADED = '未成交'
STATUS_PARTTRADED = '部分成交'
STATUS_ALLTRADED = '全部成交'
STATUS_CANCELLED = '已撤销'
STATUS_UNKNOWN = '未知'

# 合约类型常量
PRODUCT_EQUITY = '股票'
PRODUCT_FUTURES = '期货'
PRODUCT_OPTION = '期权'
PRODUCT_INDEX = '指数'
PRODUCT_COMBINATION = '组合'
PRODUCT_FOREX = '外汇'
PRODUCT_UNKNOWN = '未知'
PRODUCT_SPOT = '现货'
PRODUCT_DEFER = '延期'
PRODUCT_NONE = ''

# 价格类型常量
PRICETYPE_LIMITPRICE = '限价'
PRICETYPE_MARKETPRICE = '市价'
PRICETYPE_FAK = 'FAK'
PRICETYPE_FOK = 'FOK'

# 期权类型
OPTION_CALL = '看涨期权'
OPTION_PUT = '看跌期权'

# 交易所类型
EXCHANGE_SSE = 'SSE'       # 上交所
EXCHANGE_SZSE = 'SZSE'     # 深交所
EXCHANGE_CFFEX = 'CFFEX'   # 中金所
EXCHANGE_SHFE = 'SHFE'     # 上期所
EXCHANGE_CZCE = 'CZCE'     # 郑商所
EXCHANGE_DCE = 'DCE'       # 大商所
EXCHANGE_SGE = 'SGE'       # 上金所
EXCHANGE_UNKNOWN = 'UNKNOWN'# 未知交易所
EXCHANGE_NONE = ''          # 空交易所
EXCHANGE_HKEX = 'HKEX'      # 港交所

EXCHANGE_SMART = 'SMART'       # IB智能路由（股票、期权）
EXCHANGE_NYMEX = 'NYMEX'       # IB 期货
EXCHANGE_GLOBEX = 'GLOBEX'     # CME电子交易平台
EXCHANGE_IDEALPRO = 'IDEALPRO' # IB外汇ECN

EXCHANGE_CME = 'CME'           # CME交易所
EXCHANGE_ICE = 'ICE'           # ICE交易所

EXCHANGE_OANDA = 'OANDA'       # OANDA外汇做市商
EXCHANGE_OKCOIN = 'OKCOIN'     # OKCOIN比特币交易所

# 货币类型
CURRENCY_USD = 'USD'            # 美元
CURRENCY_CNY = 'CNY'            # 人民币
CURRENCY_UNKNOWN = 'UNKNOWN'    # 未知货币
CURRENCY_NONE = ''              # 空货币