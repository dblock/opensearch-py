# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
# ----------------------------------------------------
# THIS CODE IS GENERATED AND MANUAL EDITS WILL BE LOST.
#
# To contribute, kindly make essential modifications through either the "opensearch-py client generator":
# https://github.com/opensearch-project/opensearch-py/blob/main/utils/generate-api.py
# or the "OpenSearch API specification" available at:
# https://github.com/opensearch-project/opensearch-api-specification/blob/main/OpenSearch.openapi.json
# -----------------------------------------------------


from typing import Any, MutableMapping, Optional

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class DanglingIndicesClient(NamespacedClient):
    @query_params(
        "accept_data_loss", "cluster_manager_timeout", "master_timeout", "timeout"
    )
    async def delete_dangling_index(
        self,
        index_uuid: Any,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Deletes the specified dangling index.


        :arg index_uuid: The UUID of the dangling index.
        :arg accept_data_loss: Must be set to true in order to delete
            the dangling index.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        :arg timeout: Operation timeout.
        """
        if index_uuid in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index_uuid'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_dangling", index_uuid),
            params=params,
            headers=headers,
        )

    @query_params(
        "accept_data_loss", "cluster_manager_timeout", "master_timeout", "timeout"
    )
    async def import_dangling_index(
        self,
        index_uuid: Any,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Imports the specified dangling index.


        :arg index_uuid: The UUID of the dangling index.
        :arg accept_data_loss: Must be set to true in order to import
            the dangling index.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        :arg timeout: Operation timeout.
        """
        if index_uuid in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index_uuid'.")

        return await self.transport.perform_request(
            "POST", _make_path("_dangling", index_uuid), params=params, headers=headers
        )

    @query_params()
    async def list_dangling_indices(
        self,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns all dangling indices.

        """
        return await self.transport.perform_request(
            "GET", "/_dangling", params=params, headers=headers
        )
