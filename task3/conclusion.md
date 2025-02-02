# Результати тестування:
**стаття 1 (існуючий, вигаданий)**

Кнут-Морріс-Пратт: 0.000993 / 0.000881 seconds\
Боєр-Мур: 0.000233 / 0.000170 seconds\
Рабін-Карп: 0.002580 / 0.002578 seconds   

--------------------------------------------------
**стаття 2 (існуючий, вигаданий)**

Кнут-Морріс-Пратт: 0.002435 / 0.002163 seconds\
Боєр-Мур: 0.000531 / 0.000369 seconds\
Рабін-Карп: 0.006032 / 0.006206 seconds


# Висновки:
Алгоритм Кнута-Морріса-Пратта показує стабільний час виконання, незалежно від того, існує підрядок чи ні. Час виконання збільшується зі зростанням розміру тексту, що підтверджує теоретичну складність 𝑂(𝑛+𝑚). Найкращий вибір, коли важлива передбачуваність часу виконання.

Алгоритм Боєра-Мура демонструє найменший час виконання серед усіх алгоритмів, різниця між часом для існуючого та неіснуючого підрядка мінімальна. Цей алгоритм особливо ефективний для текстів, де збіги рідкісні, завдяки "стрибкам" за текстом, що підтверджує його теоретичну складність 𝑂(𝑛) у кращому випадку. Найкращий вибір для роботи з довгими текстами, де збіги рідкісні.

Алгоритм Рабіна-Карпа значно повільніше за інші алгоритми, його продуктивність залежить від довжини підрядка, оскільки алгоритм покладається на хеш-функцію для порівняння. Хоча теоретично він має складність 𝑂(𝑛+𝑚), велика константа у обчисленнях хешів робить його на практиці повільним. Хороший вибір, якщо потрібно шукати багато підрядків, використовуючи один текст.