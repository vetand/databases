import json

from django.http import HttpResponseRedirect

from scripts.select_drivers import select_driver
from scripts.insert_driver import insert_new_driver
from scripts.update_driver_status import update_driver_status

def chage_status(request):
    data = request.POST
 
    driver_id = data.get('driver_id', None)
    new_active_status = data.get('is_active', None)
    new_has_order_status = data.get('has_order', None)

    driver = select_driver(driver_id)

    if not (new_active_status == 'False' and driver[7]):
        update_driver_status(new_active_status, new_has_order_status, driver_id)

    return HttpResponseRedirect('/driver-profile?driver_id={}'.format(driver_id))
