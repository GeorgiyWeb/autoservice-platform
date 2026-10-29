# Architecture Decisions

## 2026-10-29: Защита от пересечения времени (Race Condition)
- **Проблема**: Два клиента могут одновременно записаться на одно время.
- **Решение**: Добавлен метод `validate` в `BookingSerializer`, который проверяет пересечение через `filter(start_time__lt=end_time, end_time__gt=start_time)`.
- **Ограничение**: На уровне SQLite это не защищает от Race Condition в 100% случаев (когда запросы приходят в одну миллисекунду). Для продакшена планируется переход на PostgreSQL и использование `select_for_update()`.
