# ----------------------------------------------------
# THIS CODE IS GENERATED AND MANUAL EDITS WILL BE LOST.
#
# To contribute, kindly make essential modifications through either the "opensearch-py client generator":
# https://github.com/opensearch-project/opensearch-py/blob/main/utils/generate-api.py
# or the "OpenSearch API specification" available at:
# https://github.com/opensearch-project/opensearch-api-specification/blob/main/OpenSearch.openapi.json
# -----------------------------------------------------

from .utils import NamespacedClient
from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

class RemoteStoreClient(NamespacedClient):
    async def restore(
        self,
        *,
        body: Any,
        cluster_manager_timeout: Optional[Any] = ...,
        wait_for_completion: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
