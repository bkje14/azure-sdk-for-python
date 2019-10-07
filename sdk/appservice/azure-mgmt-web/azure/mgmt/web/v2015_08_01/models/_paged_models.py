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


class AppServiceCertificateOrderPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AppServiceCertificateOrder <azure.mgmt.web.models.AppServiceCertificateOrder>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AppServiceCertificateOrder]'}
    }

    def __init__(self, *args, **kwargs):

        super(AppServiceCertificateOrderPaged, self).__init__(*args, **kwargs)
class AppServiceCertificateResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AppServiceCertificateResource <azure.mgmt.web.models.AppServiceCertificateResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AppServiceCertificateResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(AppServiceCertificateResourcePaged, self).__init__(*args, **kwargs)
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
