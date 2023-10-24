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


class IngestClient(NamespacedClient):
    @query_params("cluster_manager_timeout", "master_timeout")
    def get_pipeline(
        self,
        id: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns a pipeline.


        :arg id: Comma-separated list of pipeline ids. Wildcards
            supported.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        """
        return self.transport.perform_request(
            "GET", _make_path("_ingest", "pipeline", id), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def put_pipeline(
        self,
        id: Any,
        body: Any,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Creates or updates a pipeline.


        :arg id: Pipeline ID.
        :arg body: The ingest definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        :arg timeout: Operation timeout.
        """
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def delete_pipeline(
        self,
        id: Any,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Deletes a pipeline.


        :arg id: Pipeline ID.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead): Operation timeout for connection
            to master node.
        :arg timeout: Operation timeout.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
        )

    @query_params("verbose")
    def simulate(
        self,
        body: Any,
        id: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Allows to simulate a pipeline with example documents.


        :arg body: The simulate definition
        :arg id: Pipeline ID.
        :arg verbose: Verbose mode. Display data output for each
            processor in executed pipeline. (default: false)
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_ingest", "pipeline", id, "_simulate"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def processor_grok(
        self,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns a list of the built-in patterns.

        """
        return self.transport.perform_request(
            "GET", "/_ingest/processor/grok", params=params, headers=headers
        )
