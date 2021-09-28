from django import template
from django.utils.safestring import mark_safe
from shop.models import Smartphone

register = template.Library()

TABLE_HEAD = """
            <table class="table">
                <tbody>
            """

TABLE_CONTENT = """
                  <tr>
                    <td>{name}</td>
                    <td>{value}</td>
                  </tr>
                """

TABLE_FOOTER = """
                </tbody>
            </table>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge',
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Заряд аккумулятора': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие слота sd карты': 'sd',
        'Максимальный объём памяти sd карты': 'sd_volume_max',
        'Камера (МП)': 'main_cam_mp',
        'Фронтальная камера (МП)': 'frontal_cam_mp',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Максимальный объём памяти sd карты')
        else:
            PRODUCT_SPEC['smartphone']['Максимальный объём памяти sd карты'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_FOOTER)
