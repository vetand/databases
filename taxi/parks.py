from django.http import HttpResponse
from scripts.select_drivers import select_drivers
from scripts.select_orders import select_taxi_orders

template = """
<!DOCTYPE html>
<html>

<head> 
    <meta charset="UTF-8">
    <title>Таксопарк</title>
</head>

<body>

<h1>Водители вашего таксопарка:</h1>

<table>
  <tr>
    <th>ID</th>
    <th>Имя</th>
    <th>Бренд модели автомобиля</th>
    <th>Модель автомобиля</th>
    <th>Гос. номер автомобиля</th>
    <th>Готов принимать заказы</th>
    <th>Выполняет заказ</th>
  </tr>
  {}
</table>

<h1>Активные заказы:</h1>

<table>
  <tr>
    <th>ID</th>
    <th>Цена</th>
    <th>ID пассажира</th>
    <th>ID водителя</th>
    <th>Создан</th>
    <th>Завершен</th>
  </tr>
  {}
</table>

</body>
</html>
"""

driver_template = """
<tr>
    <td><a href="/driver-profile?driver_id={}">{}</a></td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
</tr>
"""

order_template = """
<tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td><a href="/driver-profile?driver_id={}">{}</a></td>
    <td>{}</td>
    <td>{}</td>
</tr>
"""

def index(request):
    drivers = select_drivers(10000)
    orders = select_taxi_orders(10000)

    drivers_section = str()
    for driver in drivers:
        drivers_section += driver_template.format(
            driver[0],
            driver[0],
            driver[1],
            driver[4],
            driver[5],
            driver[3],
            driver[6],
            driver[7],
        )

    orders_section = str()
    for order in orders:
        orders_section += order_template.format(
            order[0],
            order[1],
            order[2],
            order[3],
            order[3],
            order[4],
            order[5],
        )

    return HttpResponse(template.format(drivers_section, orders_section))
