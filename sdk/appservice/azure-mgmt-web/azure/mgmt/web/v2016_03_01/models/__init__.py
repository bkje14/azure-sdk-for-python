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

try:
    from ._models_py3 import AbnormalTimePeriod
    from ._models_py3 import AnalysisData
    from ._models_py3 import AnalysisDefinition
    from ._models_py3 import ApiDefinitionInfo
    from ._models_py3 import ApplicationStack
    from ._models_py3 import AppServiceEnvironment
    from ._models_py3 import AppServicePlan
    from ._models_py3 import AppServicePlanCollection
    from ._models_py3 import AutoHealActions
    from ._models_py3 import AutoHealCustomAction
    from ._models_py3 import AutoHealRules
    from ._models_py3 import AutoHealTriggers
    from ._models_py3 import BillingMeter
    from ._models_py3 import Capability
    from ._models_py3 import Certificate
    from ._models_py3 import CertificatePatchResource
    from ._models_py3 import CloningInfo
    from ._models_py3 import ConnStringInfo
    from ._models_py3 import CorsSettings
    from ._models_py3 import CsmMoveResourceEnvelope
    from ._models_py3 import CsmOperationDescription
    from ._models_py3 import CsmOperationDescriptionProperties
    from ._models_py3 import CsmOperationDisplay
    from ._models_py3 import CsmUsageQuota
    from ._models_py3 import CsmUsageQuotaCollection
    from ._models_py3 import DataSource
    from ._models_py3 import DataTableResponseColumn
    from ._models_py3 import DataTableResponseObject
    from ._models_py3 import DefaultErrorResponse, DefaultErrorResponseException
    from ._models_py3 import DefaultErrorResponseError
    from ._models_py3 import DefaultErrorResponseErrorDetailsItem
    from ._models_py3 import DeletedSite
    from ._models_py3 import DeploymentLocations
    from ._models_py3 import DetectorAbnormalTimePeriod
    from ._models_py3 import DetectorDefinition
    from ._models_py3 import DetectorInfo
    from ._models_py3 import DetectorResponse
    from ._models_py3 import DiagnosticAnalysis
    from ._models_py3 import DiagnosticCategory
    from ._models_py3 import DiagnosticData
    from ._models_py3 import DiagnosticDetectorResponse
    from ._models_py3 import DiagnosticMetricSample
    from ._models_py3 import DiagnosticMetricSet
    from ._models_py3 import Dimension
    from ._models_py3 import ErrorEntity
    from ._models_py3 import Experiments
    from ._models_py3 import GeoRegion
    from ._models_py3 import GlobalCsmSkuDescription
    from ._models_py3 import HandlerMapping
    from ._models_py3 import HostingEnvironmentDeploymentInfo
    from ._models_py3 import HostingEnvironmentProfile
    from ._models_py3 import HostNameSslState
    from ._models_py3 import HybridConnection
    from ._models_py3 import HybridConnectionKey
    from ._models_py3 import Identifier
    from ._models_py3 import IpSecurityRestriction
    from ._models_py3 import LocalizableString
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NameIdentifier
    from ._models_py3 import NameValuePair
    from ._models_py3 import NetworkAccessControlEntry
    from ._models_py3 import Operation
    from ._models_py3 import PremierAddOnOffer
    from ._models_py3 import ProxyOnlyResource
    from ._models_py3 import PushSettings
    from ._models_py3 import RampUpRule
    from ._models_py3 import Recommendation
    from ._models_py3 import RecommendationRule
    from ._models_py3 import Rendering
    from ._models_py3 import RequestsBasedTrigger
    from ._models_py3 import Resource
    from ._models_py3 import ResourceHealthMetadata
    from ._models_py3 import ResourceMetric
    from ._models_py3 import ResourceMetricAvailability
    from ._models_py3 import ResourceMetricCollection
    from ._models_py3 import ResourceMetricDefinition
    from ._models_py3 import ResourceMetricDefinitionCollection
    from ._models_py3 import ResourceMetricName
    from ._models_py3 import ResourceMetricProperty
    from ._models_py3 import ResourceMetricValue
    from ._models_py3 import ResourceNameAvailability
    from ._models_py3 import ResourceNameAvailabilityRequest
    from ._models_py3 import ResponseMetaData
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Site
    from ._models_py3 import SiteConfig
    from ._models_py3 import SiteLimits
    from ._models_py3 import SiteMachineKey
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SkuDescription
    from ._models_py3 import SkuInfos
    from ._models_py3 import SlotSwapStatus
    from ._models_py3 import SlowRequestsBasedTrigger
    from ._models_py3 import SnapshotRecoveryRequest
    from ._models_py3 import SnapshotRecoveryTarget
    from ._models_py3 import Solution
    from ._models_py3 import SourceControl
    from ._models_py3 import StackMajorVersion
    from ._models_py3 import StackMinorVersion
    from ._models_py3 import StampCapacity
    from ._models_py3 import StatusCodesBasedTrigger
    from ._models_py3 import User
    from ._models_py3 import ValidateRequest
    from ._models_py3 import ValidateResponse
    from ._models_py3 import ValidateResponseError
    from ._models_py3 import VirtualApplication
    from ._models_py3 import VirtualDirectory
    from ._models_py3 import VirtualIPMapping
    from ._models_py3 import VirtualNetworkProfile
    from ._models_py3 import VnetGateway
    from ._models_py3 import VnetInfo
    from ._models_py3 import VnetParameters
    from ._models_py3 import VnetRoute
    from ._models_py3 import VnetValidationFailureDetails
    from ._models_py3 import VnetValidationTestFailure
    from ._models_py3 import WebAppCollection
    from ._models_py3 import WorkerPool
except (SyntaxError, ImportError):
    from ._models import AbnormalTimePeriod
    from ._models import AnalysisData
    from ._models import AnalysisDefinition
    from ._models import ApiDefinitionInfo
    from ._models import ApplicationStack
    from ._models import AppServiceEnvironment
    from ._models import AppServicePlan
    from ._models import AppServicePlanCollection
    from ._models import AutoHealActions
    from ._models import AutoHealCustomAction
    from ._models import AutoHealRules
    from ._models import AutoHealTriggers
    from ._models import BillingMeter
    from ._models import Capability
    from ._models import Certificate
    from ._models import CertificatePatchResource
    from ._models import CloningInfo
    from ._models import ConnStringInfo
    from ._models import CorsSettings
    from ._models import CsmMoveResourceEnvelope
    from ._models import CsmOperationDescription
    from ._models import CsmOperationDescriptionProperties
    from ._models import CsmOperationDisplay
    from ._models import CsmUsageQuota
    from ._models import CsmUsageQuotaCollection
    from ._models import DataSource
    from ._models import DataTableResponseColumn
    from ._models import DataTableResponseObject
    from ._models import DefaultErrorResponse, DefaultErrorResponseException
    from ._models import DefaultErrorResponseError
    from ._models import DefaultErrorResponseErrorDetailsItem
    from ._models import DeletedSite
    from ._models import DeploymentLocations
    from ._models import DetectorAbnormalTimePeriod
    from ._models import DetectorDefinition
    from ._models import DetectorInfo
    from ._models import DetectorResponse
    from ._models import DiagnosticAnalysis
    from ._models import DiagnosticCategory
    from ._models import DiagnosticData
    from ._models import DiagnosticDetectorResponse
    from ._models import DiagnosticMetricSample
    from ._models import DiagnosticMetricSet
    from ._models import Dimension
    from ._models import ErrorEntity
    from ._models import Experiments
    from ._models import GeoRegion
    from ._models import GlobalCsmSkuDescription
    from ._models import HandlerMapping
    from ._models import HostingEnvironmentDeploymentInfo
    from ._models import HostingEnvironmentProfile
    from ._models import HostNameSslState
    from ._models import HybridConnection
    from ._models import HybridConnectionKey
    from ._models import Identifier
    from ._models import IpSecurityRestriction
    from ._models import LocalizableString
    from ._models import ManagedServiceIdentity
    from ._models import MetricAvailability
    from ._models import MetricSpecification
    from ._models import NameIdentifier
    from ._models import NameValuePair
    from ._models import NetworkAccessControlEntry
    from ._models import Operation
    from ._models import PremierAddOnOffer
    from ._models import ProxyOnlyResource
    from ._models import PushSettings
    from ._models import RampUpRule
    from ._models import Recommendation
    from ._models import RecommendationRule
    from ._models import Rendering
    from ._models import RequestsBasedTrigger
    from ._models import Resource
    from ._models import ResourceHealthMetadata
    from ._models import ResourceMetric
    from ._models import ResourceMetricAvailability
    from ._models import ResourceMetricCollection
    from ._models import ResourceMetricDefinition
    from ._models import ResourceMetricDefinitionCollection
    from ._models import ResourceMetricName
    from ._models import ResourceMetricProperty
    from ._models import ResourceMetricValue
    from ._models import ResourceNameAvailability
    from ._models import ResourceNameAvailabilityRequest
    from ._models import ResponseMetaData
    from ._models import ServiceSpecification
    from ._models import Site
    from ._models import SiteConfig
    from ._models import SiteLimits
    from ._models import SiteMachineKey
    from ._models import SkuCapacity
    from ._models import SkuDescription
    from ._models import SkuInfos
    from ._models import SlotSwapStatus
    from ._models import SlowRequestsBasedTrigger
    from ._models import SnapshotRecoveryRequest
    from ._models import SnapshotRecoveryTarget
    from ._models import Solution
    from ._models import SourceControl
    from ._models import StackMajorVersion
    from ._models import StackMinorVersion
    from ._models import StampCapacity
    from ._models import StatusCodesBasedTrigger
    from ._models import User
    from ._models import ValidateRequest
    from ._models import ValidateResponse
    from ._models import ValidateResponseError
    from ._models import VirtualApplication
    from ._models import VirtualDirectory
    from ._models import VirtualIPMapping
    from ._models import VirtualNetworkProfile
    from ._models import VnetGateway
    from ._models import VnetInfo
    from ._models import VnetParameters
    from ._models import VnetRoute
    from ._models import VnetValidationFailureDetails
    from ._models import VnetValidationTestFailure
    from ._models import WebAppCollection
    from ._models import WorkerPool
from ._paged_models import AnalysisDefinitionPaged
from ._paged_models import ApplicationStackPaged
from ._paged_models import BillingMeterPaged
from ._paged_models import CertificatePaged
from ._paged_models import CsmOperationDescriptionPaged
from ._paged_models import DeletedSitePaged
from ._paged_models import DetectorDefinitionPaged
from ._paged_models import DetectorResponsePaged
from ._paged_models import DiagnosticCategoryPaged
from ._paged_models import GeoRegionPaged
from ._paged_models import IdentifierPaged
from ._paged_models import PremierAddOnOfferPaged
from ._paged_models import RecommendationPaged
from ._paged_models import ResourceHealthMetadataPaged
from ._paged_models import SourceControlPaged
from ._web_site_management_client_enums import (
    KeyVaultSecretStatus,
    RouteType,
    ManagedServiceIdentityType,
    AutoHealActionType,
    ConnectionStringType,
    ScmType,
    ManagedPipelineMode,
    SiteLoadBalancing,
    SupportedTlsVersions,
    SslState,
    HostType,
    UsageState,
    SiteAvailabilityState,
    StatusOptions,
    ProvisioningState,
    HostingEnvironmentStatus,
    InternalLoadBalancingMode,
    ComputeModeOptions,
    WorkerSizeOptions,
    AccessControlEntryAction,
    OperationStatus,
    IssueType,
    SolutionType,
    RenderingType,
    ResourceScopeType,
    NotificationLevel,
    Channels,
    AppServicePlanRestrictions,
    InAvailabilityReasonType,
    CheckNameResourceTypes,
    ValidateResourceTypes,
    SkuName,
)

__all__ = [
    'AbnormalTimePeriod',
    'AnalysisData',
    'AnalysisDefinition',
    'ApiDefinitionInfo',
    'ApplicationStack',
    'AppServiceEnvironment',
    'AppServicePlan',
    'AppServicePlanCollection',
    'AutoHealActions',
    'AutoHealCustomAction',
    'AutoHealRules',
    'AutoHealTriggers',
    'BillingMeter',
    'Capability',
    'Certificate',
    'CertificatePatchResource',
    'CloningInfo',
    'ConnStringInfo',
    'CorsSettings',
    'CsmMoveResourceEnvelope',
    'CsmOperationDescription',
    'CsmOperationDescriptionProperties',
    'CsmOperationDisplay',
    'CsmUsageQuota',
    'CsmUsageQuotaCollection',
    'DataSource',
    'DataTableResponseColumn',
    'DataTableResponseObject',
    'DefaultErrorResponse', 'DefaultErrorResponseException',
    'DefaultErrorResponseError',
    'DefaultErrorResponseErrorDetailsItem',
    'DeletedSite',
    'DeploymentLocations',
    'DetectorAbnormalTimePeriod',
    'DetectorDefinition',
    'DetectorInfo',
    'DetectorResponse',
    'DiagnosticAnalysis',
    'DiagnosticCategory',
    'DiagnosticData',
    'DiagnosticDetectorResponse',
    'DiagnosticMetricSample',
    'DiagnosticMetricSet',
    'Dimension',
    'ErrorEntity',
    'Experiments',
    'GeoRegion',
    'GlobalCsmSkuDescription',
    'HandlerMapping',
    'HostingEnvironmentDeploymentInfo',
    'HostingEnvironmentProfile',
    'HostNameSslState',
    'HybridConnection',
    'HybridConnectionKey',
    'Identifier',
    'IpSecurityRestriction',
    'LocalizableString',
    'ManagedServiceIdentity',
    'MetricAvailability',
    'MetricSpecification',
    'NameIdentifier',
    'NameValuePair',
    'NetworkAccessControlEntry',
    'Operation',
    'PremierAddOnOffer',
    'ProxyOnlyResource',
    'PushSettings',
    'RampUpRule',
    'Recommendation',
    'RecommendationRule',
    'Rendering',
    'RequestsBasedTrigger',
    'Resource',
    'ResourceHealthMetadata',
    'ResourceMetric',
    'ResourceMetricAvailability',
    'ResourceMetricCollection',
    'ResourceMetricDefinition',
    'ResourceMetricDefinitionCollection',
    'ResourceMetricName',
    'ResourceMetricProperty',
    'ResourceMetricValue',
    'ResourceNameAvailability',
    'ResourceNameAvailabilityRequest',
    'ResponseMetaData',
    'ServiceSpecification',
    'Site',
    'SiteConfig',
    'SiteLimits',
    'SiteMachineKey',
    'SkuCapacity',
    'SkuDescription',
    'SkuInfos',
    'SlotSwapStatus',
    'SlowRequestsBasedTrigger',
    'SnapshotRecoveryRequest',
    'SnapshotRecoveryTarget',
    'Solution',
    'SourceControl',
    'StackMajorVersion',
    'StackMinorVersion',
    'StampCapacity',
    'StatusCodesBasedTrigger',
    'User',
    'ValidateRequest',
    'ValidateResponse',
    'ValidateResponseError',
    'VirtualApplication',
    'VirtualDirectory',
    'VirtualIPMapping',
    'VirtualNetworkProfile',
    'VnetGateway',
    'VnetInfo',
    'VnetParameters',
    'VnetRoute',
    'VnetValidationFailureDetails',
    'VnetValidationTestFailure',
    'WebAppCollection',
    'WorkerPool',
    'CertificatePaged',
    'DeletedSitePaged',
    'DetectorResponsePaged',
    'DiagnosticCategoryPaged',
    'AnalysisDefinitionPaged',
    'DetectorDefinitionPaged',
    'ApplicationStackPaged',
    'CsmOperationDescriptionPaged',
    'RecommendationPaged',
    'ResourceHealthMetadataPaged',
    'SourceControlPaged',
    'GeoRegionPaged',
    'IdentifierPaged',
    'PremierAddOnOfferPaged',
    'BillingMeterPaged',
    'KeyVaultSecretStatus',
    'RouteType',
    'ManagedServiceIdentityType',
    'AutoHealActionType',
    'ConnectionStringType',
    'ScmType',
    'ManagedPipelineMode',
    'SiteLoadBalancing',
    'SupportedTlsVersions',
    'SslState',
    'HostType',
    'UsageState',
    'SiteAvailabilityState',
    'StatusOptions',
    'ProvisioningState',
    'HostingEnvironmentStatus',
    'InternalLoadBalancingMode',
    'ComputeModeOptions',
    'WorkerSizeOptions',
    'AccessControlEntryAction',
    'OperationStatus',
    'IssueType',
    'SolutionType',
    'RenderingType',
    'ResourceScopeType',
    'NotificationLevel',
    'Channels',
    'AppServicePlanRestrictions',
    'InAvailabilityReasonType',
    'CheckNameResourceTypes',
    'ValidateResourceTypes',
    'SkuName',
]
