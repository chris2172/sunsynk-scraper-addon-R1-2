import datetime

login_endpoint = ('https://api.sunsynk.net/oauth/token')

plants_endpoint = ('https://api.sunsynk.net/api/v1/plants?page=1&limit=10&name=&status=')
                   
energy_base_url = "https://api.sunsynk.net/api/v1/plant/energy/"

inverter_list_url = "https://api.sunsynk.net/api/v1/inverters?page=1&limit=10&status=-1&type=-1"

flow_chart_endpoint = "flow"
day_readings_endpoint = "day?lan=en"
month_readings_endpoint = "month?lan=en"

def get_flow_chart_endpoint(plant_id, date: datetime.date):
    return f'{energy_base_url}{plant_id}/{flow_chart_endpoint}?date={date.strftime("%Y-%m-%d")}'

def get_day_readings_endpoint(plant_id, date: datetime.date):
    return f'{energy_base_url}{plant_id}/{day_readings_endpoint}&date={date.strftime("%Y-%m-%d")}'

def get_month_readings_endpoint(plant_id, date):
    return f'{energy_base_url}{plant_id}/{month_readings_endpoint}&date={date.strftime("%Y-%m")}&id={plant_id}'
