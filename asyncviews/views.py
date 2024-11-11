import asyncio
from django.http import HttpResponse

# Função assíncrona para o contador de tempo
async def time_counter():
    for i in range(1, 11):
        await asyncio.sleep(1)  # Simula uma pausa de 1 segundo
        print(f"Contador: {i}")
    return "Contador finalizado!"

# Nova view assíncrona que chama o contador de tempo
async def async_time_counter(request):
    loop = asyncio.get_event_loop()
    result = await time_counter()
    return HttpResponse(f"Processo assíncrono concluído: {result}")
