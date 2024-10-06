from service_container.ServiceParameters import ServiceParameters
from views.web.Product.ProductView import ProductView

parameters = {
    ProductView: ServiceParameters(is_singleton=False)
}
