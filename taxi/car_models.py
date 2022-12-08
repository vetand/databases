from django.http import HttpResponse
from scripts.select_drivers import select_drivers
from scripts.select_orders import select_taxi_orders
from scripts.select_car_models import select_car_models

template = """
<!DOCTYPE html>
<html>

<head> 
    <meta charset="UTF-8">
    <title>Модели автомобилей</title>
</head>

<body>

<h1>Модели автомобилей:</h1>

<table>
  <tr>
    <th>ID</th>
    <th>Бренд</th>
    <th>Модель автомобиля</th>
    <th>Описание</th>
  </tr>
  {}
</table>

</body>
</html>
"""

model_template = """
<tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
</tr>
"""

def index(request):
    car_models = select_car_models(1000000)

    models_section = str()
    for model in car_models:
        models_section += model_template.format(
            model[0],
            model[1],
            model[2],
            model[3]
        )

    return HttpResponse(template.format(models_section))
