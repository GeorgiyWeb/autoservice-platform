## ViewSet: основные атрибуты
- queryset - какие обьекты
- serializers_class - каким сериализатором
- filter_backends - список бэкендов 
- filterset_fields - по каким полям будет применять фильтр (DjangoFilterBackend)
- search_fields - по каким полям будет применять поиск (SearchFilter)
- ordering_fields - по каким полям будет применять сортировку (OrderingFilter)
- permission_classes - кто имеет доступ
- pagination_class - как пагинировать