# Semana 1 

## Entrada 1

promt: Genera 5 funciones puras sobre reading, debes tomar en cuenta el formato de los type hints actuales, quiero que una sea para cambiar de celsius fahrenheit, una de escritura en formato csv y otra de un umbral de temperatura, las otras que sean facilmente verificables. 

Respuesta de la IA:

Se agregaron 5 funciones puras para `Reading` en dia1_python_idiomatico.py:

- `convert_temperature_celsius_to_fahrenheit(r: Reading) -> Reading`
- `format_reading_as_csv(r: Reading) -> str`
- `is_temperature_above_threshold(r: Reading, threshold: float) -> bool`
- `reading_summary(r: Reading) -> str`
- `with_scaled_value(r: Reading, factor: float) -> Reading`

Decisión:
Las 5 funciones cumplen con el criterio de solo funcionanildad de Reading, decidí conservar las 5. 


## Entrada 2 (actividade del martes)

**Promt:** I build this demo of an Finite State Machine, now I want to test it with pytest. Create 4 easy test in my "test_fsm.py" archive. 

IA propuso 4 funciones
**Respuesta de IA:** 
I created 4 easy tests in test_fsm.py for your FSM demo:

- `test_initial_state_is_red`
- `test_transition_red_to_green`
- `test_full_cycle_returns_to_red`
- `test_cycle_count_increments`

**Decisión** 
Despúes de ver que la IA introdujo correctamente los conceptos que hemos visto como "assert" para las pruebas y las declaraciones de las funciones, realicé pruebas y usé las 4 pruebas que me dio la IA, todas pasaron. 


## entrada 3 (actividad miercoles)

**Promt:** genera ejemplos de los principios SOLID, s, o y l, toma como erferencia el fragmento de código en el archivo, escribe 1 de la forma correcta y 1 forma incorrecta de cada principio. 


**Respuesta de IA**
Devolvió ejemplos muy claros sobre los principios de Responsabilidad única, principio de abierto/cerrado y el principio de sustitución de Liskov. 


**Decisión**
Dejé todos los ejemplos ya que ilustra muy bien las buenas prácticas de cómo sí declarar funciones siguiendo los principios SOLID, y dejé 1 ejemplo de cómo no hacerlo. 

## Entrada 4 (actividad miercoles)

**Promt:**
ahora genera los test para pytest de cada función en el archivo actual


La IA asignó 6 pruebas para las funciones creadas para los principios S ,O, L de SOLID. 

**Decisión**
copilot free escribió las los test en el archivo test_solid_srp_ocp_lsp.py y al al correr las pruebas, todas pasaron.