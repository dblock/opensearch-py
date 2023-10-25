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

from .utils import NamespacedClient, _make_path, query_params


class NodesClient(NamespacedClient):
    @query_params("timeout")
    def reload_secure_settings(
        self,
        body: Optional[Any] = None,
        node_id: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Reloads secure settings.


        :arg body: An object containing the password for the opensearch
            keystore
        :arg node_id: Comma-separated list of node IDs to span the
            reload/reinit call. Should stay empty because reloading usually involves
            all cluster nodes.
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_nodes", node_id, "reload_secure_settings"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("flat_settings", "timeout")
    def info(
        self,
        node_id: Optional[Any] = None,
        metric: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns information about nodes in the cluster.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg metric: Comma-separated list of metrics you wish returned.
            Leave empty to return all.  Valid choices: settings, os, process, jvm,
            thread_pool, transport, http, plugins, ingest
        :arg flat_settings: Return settings in flat format. (default:
            false)
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "GET", _make_path("_nodes", node_id, metric), params=params, headers=headers
        )

    @query_params(
        "completion_fields",
        "fielddata_fields",
        "fields",
        "groups",
        "include_segment_file_sizes",
        "level",
        "timeout",
        "types",
    )
    def stats(
        self,
        node_id: Optional[Any] = None,
        metric: Optional[Any] = None,
        index_metric: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns statistical information about nodes in the cluster.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg metric: Limit the information returned to the specified
            metrics.  Valid choices: _all, breaker, fs, http, indices, jvm, os,
            process, thread_pool, transport, discovery, indexing_pressure
        :arg index_metric: Limit the information returned for `indices`
            metric to the specific index metrics. Isn't used if `indices` (or `all`)
            metric isn't specified.  Valid choices: _all, store, indexing, get,
            search, merge, flush, refresh, query_cache, fielddata, docs, warmer,
            completion, segments, translog, suggest, request_cache, recovery
        :arg completion_fields: Comma-separated list of fields for
            `fielddata` and `suggest` index metric (supports wildcards).
        :arg fielddata_fields: Comma-separated list of fields for
            `fielddata` index metric (supports wildcards).
        :arg fields: Comma-separated list of fields for `fielddata` and
            `completion` index metric (supports wildcards).
        :arg groups: Comma-separated list of search groups for `search`
            index metric.
        :arg include_segment_file_sizes: Whether to report the
            aggregated disk usage of each one of the Lucene index files (only
            applies if segment stats are requested). (default: false)
        :arg level: Return indices stats aggregated at index, node or
            shard level.  Valid choices: indices, node, shards
        :arg timeout: Operation timeout.
        :arg types: Comma-separated list of document types for the
            `indexing` index metric.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "stats", metric, index_metric),
            params=params,
            headers=headers,
        )

    @query_params(
        "doc_type", "ignore_idle_threads", "interval", "snapshots", "threads", "timeout"
    )
    def hot_threads(
        self,
        node_id: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns information about hot threads on each node in the cluster.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg doc_type: The type to sample.  Valid choices: cpu, wait,
            block
        :arg ignore_idle_threads: Don't show threads that are in known-
            idle places, such as waiting on a socket select or pulling from an empty
            task queue. (default: True)
        :arg interval: The interval for the second sampling of threads.
        :arg snapshots: Number of samples of thread stacktrace.
            (default: 10)
        :arg threads: Specify the number of threads to provide
            information for. (default: 3)
        :arg timeout: Operation timeout.
        """
        # type is a reserved word so it cannot be used, use doc_type instead
        if "doc_type" in params:
            params["type"] = params.pop("doc_type")

        return self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "hot_threads"),
            params=params,
            headers=headers,
        )

    @query_params("timeout")
    def usage(
        self,
        node_id: Optional[Any] = None,
        metric: Optional[Any] = None,
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> Any:
        """
        Returns low-level information about REST actions usage on nodes.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg metric: Limit the information returned to the specified
            metrics.  Valid choices: _all, rest_actions
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "usage", metric),
            params=params,
            headers=headers,
        )
