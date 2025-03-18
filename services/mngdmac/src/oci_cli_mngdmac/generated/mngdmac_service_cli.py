# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250320

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('mac_order.mngdmac_service_group.command_name', 'mngdmac'), cls=CommandGroupWithAlias, help=cli_util.override('mac_order.mngdmac_service_group.help', """Use the OCI Managed Services for Mac API to create and manage orders for dedicated, partially-managed Mac servers hosted in an OCI Data Center. For more information, see the user guide documentation for the [OCI Managed Services for Mac]()"""), short_help=cli_util.override('mac_order.mngdmac_service_group.short_help', """OCI Managed Services for Mac API"""))
@cli_util.help_option_group
def mngdmac_service_group():
    pass
