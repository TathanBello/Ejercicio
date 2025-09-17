Propiedades de los Lenguajes Regulares, Decisión y Minimización de DFA

-Descripción

1.Propiedades de clausura: unión, intersección, complemento, concatenación y estrella de Kleen
2.Decisión: cómo verificar si una cadena pertenece a un lenguaje usando un DFA.
3.Minimización de autómatas: reducción del número de estados manteniendo el mismo l

-Resumen Teórico
1️⃣ Propiedades de Clausura
Los lenguajes regulares son cerrados bajo:

°Unión ( ∪ ) → Si L1 y L2 son regulares, L1 ∪ L2 también lo es.
°Intersección ( ∩ ) → Si L1 y L2 son regulares, L1 ∩ L2 también lo es.
°Complemento ( ¬L ) → Invirtiendo los estados de aceptación en un DFA obtenemos el complemento
°Concatenación ( L1L2 ) → Juntar cadenas de L1 seguidas de cadenas de L2 genera un nuevo lenguaje regular.
Estrella de Kleene ( L )* → Repetir un lenguaje regular cualquier número de veces sigue siendo regular.

➤(En el código, los lenguajes se representan como conjuntos de Python y se aplican operaciones de conjuntos.)


2️⃣ Procedimiento de Decisión
Se implementa un Autómata Finito Determinista (DFA) que acepta cadenas que terminan en ab.

°La cadena es aceptada si termina en un estado de aceptación.
°Esto demuestra que se puede decidir si una cadena pertenece a un lenguaje regular.

3️⃣ Minimización de DFA
Se usa el algoritmo de refinamiento de particiones:

°Dividir los estados en dos grupos: aceptadores y no aceptadores.
°Refinar grupos con base en las transiciones hasta que no se puedan dividir más.
°Combinar estados equivalentes en un único estado.

➤(El resultado es un DFA más pequeño, que reconoce el mismo lenguaje pero con menos estados.)

⏺︎Ejemplo de Salida
Cuando ejecutas el código, verás

L1 = {'ab', 'a'}, L2 = {'b', 'ba'}
Unión: {'ab', 'b', 'a', 'ba'}
Intersección: set()
Complemento de L1: {'aa', 'bb', 'b', 'ba'}
Concatenación: {'aba', 'ab', 'abb', 'abba'}
Estrella de Kleene de L1: {'', 'a', 'ab', 'aba', ...}

☀Por qué da este resultado:
°Unión: Combina todos los elementos de L1 y L2 → {'ab', 'b', 'a', 'ba'}.
°Intersección: No hay elementos en común entre L1 y L2, por eso da set() (vacío).
°Complemento: Muestra las cadenas posibles (de longitud ≤ 2 en nuestro ejemplo) que NO están en L1.
°Concatenación: Une cada elemento de L1 con cada elemento de L2 (por ejemplo, a + ba = aba).
°Kleene Star: Genera todas las combinaciones posibles de repetir elementos de L1, incluyendo la cadena vacía "".

Conclusión: Los resultados demuestran que los lenguajes regulares se mantienen regulares bajo estas operaciones (propiedad de clausura).

☀Revisión de Pertenencia con DFA

Cadena 'ab' aceptada? Sí
Cadena 'aab' aceptada? Sí
Cadena 'bba' aceptada? No
Cadena 'bbab' aceptada? Sí

➤Por qué da este resultado:
°El DFA está diseñado para aceptar cadenas que terminen en ab.
°'ab' → termina en ab ✅ aceptada.
°'aab' → termina en ab ✅ aceptada.
°'bba' → termina en a ❌ rechazada.
°'bbab' → termina en ab ✅ aceptada.

Conclusión: Esto prueba la propiedad de decisión: con un DFA siempre podemos verificar si una cadena pertenece o no al lenguaje.

☀Minimización de DFA
Grupos de estados minimizados: [{'q2', 'q3'}, {'q1'}, {'q0'}]

➤Por qué da este resultado:
°El algoritmo de minimización encontró que los estados q2 y q3 se comportan igual (tienen transiciones equivalentes y son de aceptación).
°Por lo tanto, los combinó en un solo grupo.
°El DFA final tiene menos estados pero sigue aceptando las mismas cadenas que el original.



