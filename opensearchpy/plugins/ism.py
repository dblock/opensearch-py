# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

# ------------------------------------------------------------------------------------------
# THIS CODE IS AUTOMATICALLY GENERATED AND MANUAL EDITS WILL BE LOST
#
# To contribute, kindly make modifications in the opensearch-py client generator
# or in the OpenSearch API specification, and run `nox -rs generate`. See DEVELOPER_GUIDE.md
# and https://github.com/opensearch-project/opensearch-api-specification for details.
# -----------------------------------------------------------------------------------------+


from typing import Any

from ..client.utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class IsmClient(NamespacedClient):
    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def add_policy(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Adds a policy to an index.


        :arg index: Comma-separated list of data streams, indices, and
            aliases. Supports wildcards (`*`).
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "add", index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def change_policy(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the managed index policy to a new policy.


        :arg index: Comma-separated list of data streams, indices, and
            aliases. Supports wildcards (`*`).
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "change_policy", index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def delete_policy(
        self,
        policy_id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a policy.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if policy_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy_id'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_ism", "policies", policy_id),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def exists_policy(
        self,
        policy_id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Checks whether the policy exists.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if policy_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy_id'.")

        return self.transport.perform_request(
            "HEAD",
            _make_path("_plugins", "_ism", "policies", policy_id),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def explain_policy(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Gets the currently applied policy on indices.


        :arg index: Comma-separated list of data streams, indices, and
            aliases. Supports wildcards (`*`).
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "explain", index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def get_policies(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Gets the policies.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "GET", "/_plugins/_ism/policies", params=params, headers=headers
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def get_policy(
        self,
        policy_id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Gets a policy.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if policy_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy_id'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_ism", "policies", policy_id),
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace",
        "filter_path",
        "human",
        "if_primary_term",
        "if_seq_no",
        "policyID",
        "pretty",
        "source",
    )
    def put_policies(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Gets the policies.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg if_primary_term: Only perform the operation if the document
            has this primary term.
        :arg if_seq_no: Only perform the operation if the document has
            this sequence number.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "PUT", "/_plugins/_ism/policies", params=params, headers=headers, body=body
        )

    @query_params(
        "error_trace",
        "filter_path",
        "human",
        "if_primary_term",
        "if_seq_no",
        "pretty",
        "source",
    )
    def put_policy(
        self,
        policy_id: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a policy.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg if_primary_term: Only perform the operation if the document
            has this primary term.
        :arg if_seq_no: Only perform the operation if the document has
            this sequence number.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if policy_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy_id'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_ism", "policies", policy_id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def refresh_search_analyzers(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Refresh search analyzers in real time.


        :arg index: Comma-separated list of data streams, indices, and
            aliases. Supports wildcards (`*`).
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_refresh_search_analyzers", index),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def remove_policy(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Removes a policy from an index.


        :arg index: Comma-separated list of data streams, indices, and
            aliases. Supports wildcards (`*`).
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "remove", index),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def retry_index(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retry the failed action for an index.


        :arg index: Comma-separated list of data streams, indices, and
            aliases. Supports wildcards (`*`).
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Used to reduce the response. This parameter
            takes a comma-separated list of filters. It supports using wildcards to
            match any field or part of a field’s name. You can also exclude fields
            with "-".
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "retry", index),
            params=params,
            headers=headers,
            body=body,
        )
