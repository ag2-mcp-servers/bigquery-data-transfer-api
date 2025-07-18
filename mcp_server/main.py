# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T01:01:47+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Query

from models import (
    Alt,
    CheckValidCredsRequest,
    CheckValidCredsResponse,
    DataSourceIds,
    Empty,
    EnrollDataSourcesRequest,
    FieldXgafv,
    ListDataSourcesResponse,
    ListLocationsResponse,
    ListTransferConfigsResponse,
    ListTransferLogsResponse,
    ListTransferRunsResponse,
    MessageTypes,
    RunAttempt,
    ScheduleTransferRunsRequest,
    ScheduleTransferRunsResponse,
    StartManualTransferRunsRequest,
    StartManualTransferRunsResponse,
    States,
    TransferConfig,
    TransferRun,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='Schedule queries or transfer external data from SaaS applications to Google BigQuery on a regular basis.',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='BigQuery Data Transfer API',
    version='v1',
    servers=[{'url': 'https://bigquerydatatransfer.googleapis.com/'}],
)


@app.delete(
    '/v1/{name}',
    description=""" Deletes the specified transfer run. """,
    tags=['bigquery_transfer_auth'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_runs_delete(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}',
    description=""" Returns information about the particular transfer run. """,
    tags=['bigquery_transfer_auth'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_runs_get(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1/{name}',
    description=""" Updates a data transfer configuration. All fields must be set, even if they are not updated. """,
    tags=['bigquery_transfer_configs', 'bigquery_transfer_auth'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_patch(
    name: str,
    authorization_code: Optional[str] = Query(None, alias='authorizationCode'),
    service_account_name: Optional[str] = Query(None, alias='serviceAccountName'),
    update_mask: Optional[str] = Query(None, alias='updateMask'),
    version_info: Optional[str] = Query(None, alias='versionInfo'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: TransferConfig = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}/locations',
    description=""" Lists information about the supported locations for this service. """,
    tags=[
        'bigquery_transfer_configs',
        'bigquery_transfer_runs',
        'bigquery_data_sources',
        'bigquery_transfer_logs',
        'bigquery_transfer_auth',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_locations_list(
    name: str,
    filter: Optional[str] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:checkValidCreds',
    description=""" Returns true if valid credentials exist for the given data source and requesting user. """,
    tags=['bigquery_transfer_auth'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def check_valid_credentials_for_data_source(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: CheckValidCredsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:enrollDataSources',
    description=""" Enroll data sources in a user project. This allows users to create transfer configurations for these data sources. They will also appear in the ListDataSources RPC and as such, will appear in the [BigQuery UI](https://console.cloud.google.com/bigquery), and the documents can be found in the public guide for [BigQuery Web UI](https://cloud.google.com/bigquery/bigquery-web-ui) and [Data Transfer Service](https://cloud.google.com/bigquery/docs/working-with-transfers). """,
    tags=['bigquery_data_sources'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_locations_enroll_data_sources(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: EnrollDataSourcesRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/dataSources',
    description=""" Lists supported data sources and returns their settings. """,
    tags=['bigquery_transfer_auth'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_locations_data_sources_list(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/runs',
    description=""" Returns information about running and completed transfer runs. """,
    tags=['bigquery_transfer_runs', 'bigquery_transfer_configs'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_runs_list(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    run_attempt: Optional[RunAttempt] = Query(None, alias='runAttempt'),
    states: Optional[States] = None,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/transferConfigs',
    description=""" Returns information about all transfer configs owned by a project in the specified location. """,
    tags=[
        'bigquery_transfer_configs',
        'bigquery_transfer_runs',
        'bigquery_data_sources',
        'bigquery_transfer_auth',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_list(
    parent: str,
    data_source_ids: Optional[DataSourceIds] = Query(None, alias='dataSourceIds'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}/transferConfigs',
    description=""" Creates a new data transfer configuration. """,
    tags=['bigquery_transfer_configs', 'bigquery_transfer_auth'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_create(
    parent: str,
    authorization_code: Optional[str] = Query(None, alias='authorizationCode'),
    service_account_name: Optional[str] = Query(None, alias='serviceAccountName'),
    version_info: Optional[str] = Query(None, alias='versionInfo'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: TransferConfig = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{parent}/transferLogs',
    description=""" Returns log messages for the transfer run. """,
    tags=['bigquery_transfer_configs', 'bigquery_transfer_logs'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def list_transfer_logs_for_transfer_config(
    parent: str,
    message_types: Optional[MessageTypes] = Query(None, alias='messageTypes'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}:scheduleRuns',
    description=""" Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. """,
    tags=['bigquery_transfer_runs'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_schedule_runs(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: ScheduleTransferRunsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}:startManualRuns',
    description=""" Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. """,
    tags=['bigquery_transfer_runs'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def bigquerydatatransfer_projects_transfer_configs_start_manual_runs(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: StartManualTransferRunsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
