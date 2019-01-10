# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from ..generated import kms_service_cli, kmscrypto_cli, kmsmanagement_cli, kmsvault_cli
from .. import cli_util


# move kms vault commands under kms management vault
kms_service_cli.kms_service_group.commands.pop(kmsvault_cli.kms_vault_root_group.name)
kmsmanagement_cli.kms_management_root_group.add_command(kmsvault_cli.vault_group)

# remove one nested layer from crypto commands (e.g. kms crypto encrypted-data encrypt -> kms crypto encrypt)
kmscrypto_cli.kms_crypto_root_group.commands.pop(kmscrypto_cli.encrypted_data_group.name)
kmscrypto_cli.kms_crypto_root_group.commands.pop(kmscrypto_cli.decrypted_data_group.name)
kmscrypto_cli.kms_crypto_root_group.commands.pop(kmscrypto_cli.generated_key_group.name)
kmscrypto_cli.kms_crypto_root_group.add_command(kmscrypto_cli.decrypt)
kmscrypto_cli.kms_crypto_root_group.add_command(kmscrypto_cli.encrypt)
kmscrypto_cli.kms_crypto_root_group.add_command(kmscrypto_cli.generate_data_encryption_key)

# override help text that is not provided
cli_util.override_command_short_help_and_help(kmsmanagement_cli.key_group, "Source of cryptographic material used to encrypt and decrypt data")
cli_util.override_command_short_help_and_help(kmsmanagement_cli.key_version_group, "A specific version of a Key. Each master encryption key is automatically assigned a key version")
cli_util.override_command_short_help_and_help(kmsvault_cli.vault_group, "A logical entity where Key Management creates and stores your keys")

cli_util.override_command_short_help_and_help(kmsmanagement_cli.kms_management_root_group, "Operations for managing keys and vaults.")
cli_util.override_command_short_help_and_help(kmscrypto_cli.kms_crypto_root_group, "Operations for performing data encryption, decryption and generation of data encryption keys.")
cli_util.override_command_short_help_and_help(kms_service_cli.kms_service_group, "Key Management Service")
