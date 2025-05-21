from abc import ABC, abstractmethod
from typing import Optional

from src.core.domain.aggregates.pedido_aggregate import PedidoAggregate
from src.core.domain.base.repository import Repository
from src.core.domain.entities.compra_entity import CompraEntity, PartialCompraEntity
from src.core.domain.entities.pagamento_entity import (
    PagamentoEntity,
    PartialPagamentoEntity,
)
from src.core.helpers.enums.compra_status import CompraStatus
from src.core.helpers.interfaces.chace_service import CacheService
from src.core.helpers.options.pedido_find_options import PedidoFindOptions


class PedidoRepository(Repository, ABC):

    def __init__(self, cache_service: CacheService):
        super().__init__()
        self.cache_service = cache_service

    @abstractmethod
    def get(self, pedido_id: int) -> PedidoAggregate:
        raise NotImplementedError()

    @abstractmethod
    def update_status(
        self, pedido_id: int, compra_status: CompraStatus
    ) -> PedidoAggregate:
        raise NotImplementedError()
