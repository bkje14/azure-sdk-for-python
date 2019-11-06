# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import CosmosDBConfiguration



class CosmosDB(MultiApiClientMixin, SDKClient):
    """Azure Cosmos DB Database Service Resource Provider REST API

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: CosmosDBConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-08-01'
    _PROFILE_TAG = "azure.mgmt.cosmosdb.CosmosDB"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = CosmosDBConfiguration(credentials, subscription_id, base_url)
        super(CosmosDB, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-04-08: :mod:`v2015_04_01.models<azure.mgmt.cosmosdb.v2015_04_01.models>`
           * 2019-08-01: :mod:`v2019_08_01.models<azure.mgmt.cosmosdb.v2019_08_01.models>`
           * 2019-08-01-preview: :mod:`v2019_08_01_preview.models<azure.mgmt.cosmosdb.v2019_08_01_preview.models>`
        """
        if api_version == '2015-04-08':
            from .v2015_04_01 import models
            return models
        elif api_version == '2019-08-01':
            from .v2019_08_01 import models
            return models
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def cassandra_resources(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`CassandraResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.CassandraResourcesOperations>`
           * 2019-08-01-preview: :class:`CassandraResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.CassandraResourcesOperations>`
        """
        api_version = self._get_api_version('cassandra_resources')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import CassandraResourcesOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import CassandraResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def collection(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`CollectionOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.CollectionOperations>`
           * 2019-08-01: :class:`CollectionOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.CollectionOperations>`
           * 2019-08-01-preview: :class:`CollectionOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.CollectionOperations>`
        """
        api_version = self._get_api_version('collection')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import CollectionOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import CollectionOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import CollectionOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def collection_partition(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`CollectionPartitionOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.CollectionPartitionOperations>`
           * 2019-08-01: :class:`CollectionPartitionOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.CollectionPartitionOperations>`
           * 2019-08-01-preview: :class:`CollectionPartitionOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.CollectionPartitionOperations>`
        """
        api_version = self._get_api_version('collection_partition')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import CollectionPartitionOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import CollectionPartitionOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import CollectionPartitionOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def collection_partition_region(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`CollectionPartitionRegionOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.CollectionPartitionRegionOperations>`
           * 2019-08-01: :class:`CollectionPartitionRegionOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.CollectionPartitionRegionOperations>`
           * 2019-08-01-preview: :class:`CollectionPartitionRegionOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.CollectionPartitionRegionOperations>`
        """
        api_version = self._get_api_version('collection_partition_region')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import CollectionPartitionRegionOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import CollectionPartitionRegionOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import CollectionPartitionRegionOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def collection_region(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`CollectionRegionOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.CollectionRegionOperations>`
           * 2019-08-01: :class:`CollectionRegionOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.CollectionRegionOperations>`
           * 2019-08-01-preview: :class:`CollectionRegionOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.CollectionRegionOperations>`
        """
        api_version = self._get_api_version('collection_region')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import CollectionRegionOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import CollectionRegionOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import CollectionRegionOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def database(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`DatabaseOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.DatabaseOperations>`
           * 2019-08-01: :class:`DatabaseOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.DatabaseOperations>`
           * 2019-08-01-preview: :class:`DatabaseOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.DatabaseOperations>`
        """
        api_version = self._get_api_version('database')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import DatabaseOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import DatabaseOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import DatabaseOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def database_account_region(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`DatabaseAccountRegionOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.DatabaseAccountRegionOperations>`
           * 2019-08-01: :class:`DatabaseAccountRegionOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.DatabaseAccountRegionOperations>`
           * 2019-08-01-preview: :class:`DatabaseAccountRegionOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.DatabaseAccountRegionOperations>`
        """
        api_version = self._get_api_version('database_account_region')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import DatabaseAccountRegionOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import DatabaseAccountRegionOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import DatabaseAccountRegionOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def database_accounts(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`DatabaseAccountsOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.DatabaseAccountsOperations>`
           * 2019-08-01: :class:`DatabaseAccountsOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.DatabaseAccountsOperations>`
           * 2019-08-01-preview: :class:`DatabaseAccountsOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.DatabaseAccountsOperations>`
        """
        api_version = self._get_api_version('database_accounts')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import DatabaseAccountsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import DatabaseAccountsOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import DatabaseAccountsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def gremlin_resources(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`GremlinResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.GremlinResourcesOperations>`
           * 2019-08-01-preview: :class:`GremlinResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.GremlinResourcesOperations>`
        """
        api_version = self._get_api_version('gremlin_resources')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import GremlinResourcesOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import GremlinResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def mongo_db_resources(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`MongoDBResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.MongoDBResourcesOperations>`
           * 2019-08-01-preview: :class:`MongoDBResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.MongoDBResourcesOperations>`
        """
        api_version = self._get_api_version('mongo_db_resources')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import MongoDBResourcesOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import MongoDBResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`Operations<azure.mgmt.cosmosdb.v2015_04_01.operations.Operations>`
           * 2019-08-01: :class:`Operations<azure.mgmt.cosmosdb.v2019_08_01.operations.Operations>`
           * 2019-08-01-preview: :class:`Operations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import Operations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import Operations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def partition_key_range_id(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`PartitionKeyRangeIdOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.PartitionKeyRangeIdOperations>`
           * 2019-08-01: :class:`PartitionKeyRangeIdOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.PartitionKeyRangeIdOperations>`
           * 2019-08-01-preview: :class:`PartitionKeyRangeIdOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PartitionKeyRangeIdOperations>`
        """
        api_version = self._get_api_version('partition_key_range_id')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import PartitionKeyRangeIdOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import PartitionKeyRangeIdOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PartitionKeyRangeIdOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def partition_key_range_id_region(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`PartitionKeyRangeIdRegionOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.PartitionKeyRangeIdRegionOperations>`
           * 2019-08-01: :class:`PartitionKeyRangeIdRegionOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.PartitionKeyRangeIdRegionOperations>`
           * 2019-08-01-preview: :class:`PartitionKeyRangeIdRegionOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PartitionKeyRangeIdRegionOperations>`
        """
        api_version = self._get_api_version('partition_key_range_id_region')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import PartitionKeyRangeIdRegionOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import PartitionKeyRangeIdRegionOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PartitionKeyRangeIdRegionOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def percentile(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`PercentileOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.PercentileOperations>`
           * 2019-08-01: :class:`PercentileOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.PercentileOperations>`
           * 2019-08-01-preview: :class:`PercentileOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PercentileOperations>`
        """
        api_version = self._get_api_version('percentile')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import PercentileOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import PercentileOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PercentileOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def percentile_source_target(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`PercentileSourceTargetOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.PercentileSourceTargetOperations>`
           * 2019-08-01: :class:`PercentileSourceTargetOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.PercentileSourceTargetOperations>`
           * 2019-08-01-preview: :class:`PercentileSourceTargetOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PercentileSourceTargetOperations>`
        """
        api_version = self._get_api_version('percentile_source_target')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import PercentileSourceTargetOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import PercentileSourceTargetOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PercentileSourceTargetOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def percentile_target(self):
        """Instance depends on the API version:

           * 2015-04-08: :class:`PercentileTargetOperations<azure.mgmt.cosmosdb.v2015_04_01.operations.PercentileTargetOperations>`
           * 2019-08-01: :class:`PercentileTargetOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.PercentileTargetOperations>`
           * 2019-08-01-preview: :class:`PercentileTargetOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PercentileTargetOperations>`
        """
        api_version = self._get_api_version('percentile_target')
        if api_version == '2015-04-08':
            from .v2015_04_01.operations import PercentileTargetOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import PercentileTargetOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PercentileTargetOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2019-08-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2019-08-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def sql_resources(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`SqlResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.SqlResourcesOperations>`
           * 2019-08-01-preview: :class:`SqlResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.SqlResourcesOperations>`
        """
        api_version = self._get_api_version('sql_resources')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import SqlResourcesOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import SqlResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def table_resources(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`TableResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01.operations.TableResourcesOperations>`
           * 2019-08-01-preview: :class:`TableResourcesOperations<azure.mgmt.cosmosdb.v2019_08_01_preview.operations.TableResourcesOperations>`
        """
        api_version = self._get_api_version('table_resources')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import TableResourcesOperations as OperationClass
        elif api_version == '2019-08-01-preview':
            from .v2019_08_01_preview.operations import TableResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
