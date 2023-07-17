from opentelemetry import trace
import requests

tracer = trace.get_tracer("request")


def make_request(method, url, params, operation_name):
    with tracer.start_as_current_span(f"Запрос к другому сервису: {operation_name}") as span:
        span.add_event(
            "Данные запроса",
            attributes=dict(
                params=str(params),
            ),
        )
        response = requests.request(method, url, params=params)
        if response.status_code != 200:
            raise Exception("Произошла ошибка на сервере")
        result = response.json()
        span.add_event(
            "Ответ",
            attributes=dict(
                result=result,
            ),
        )
        return result