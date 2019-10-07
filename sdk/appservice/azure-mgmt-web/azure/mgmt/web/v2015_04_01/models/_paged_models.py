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

from msrest.paging import Paged


class DomainPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Domain <azure.mgmt.web.models.Domain>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Domain]'}
    }

    def __init__(self, *args, **kwargs):

        super(DomainPaged, self).__init__(*args, **kwargs)
class NameIdentifierPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NameIdentifier <azure.mgmt.web.models.NameIdentifier>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NameIdentifier]'}
    }

    def __init__(self, *args, **kwargs):

        super(NameIdentifierPaged, self).__init__(*args, **kwargs)
class DomainOwnershipIdentifierPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DomainOwnershipIdentifier <azure.mgmt.web.models.DomainOwnershipIdentifier>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DomainOwnershipIdentifier]'}
    }

    def __init__(self, *args, **kwargs):

        super(DomainOwnershipIdentifierPaged, self).__init__(*args, **kwargs)
class TopLevelDomainPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TopLevelDomain <azure.mgmt.web.models.TopLevelDomain>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TopLevelDomain]'}
    }

    def __init__(self, *args, **kwargs):

        super(TopLevelDomainPaged, self).__init__(*args, **kwargs)
class TldLegalAgreementPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TldLegalAgreement <azure.mgmt.web.models.TldLegalAgreement>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TldLegalAgreement]'}
    }

    def __init__(self, *args, **kwargs):

        super(TldLegalAgreementPaged, self).__init__(*args, **kwargs)
class CsmOperationDescriptionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CsmOperationDescription <azure.mgmt.web.models.CsmOperationDescription>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CsmOperationDescription]'}
    }

    def __init__(self, *args, **kwargs):

        super(CsmOperationDescriptionPaged, self).__init__(*args, **kwargs)
