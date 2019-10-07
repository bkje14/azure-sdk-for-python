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

from msrest.pipeline import ClientRawResponse

from .. import models


class LargePersonGroupOperations(object):
    """LargePersonGroupOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create(
            self, large_person_group_id, name=None, user_data=None, recognition_model="recognition_01", custom_headers=None, raw=False, **operation_config):
        """Create a new large person group with user-specified largePersonGroupId,
        name, an optional userData and recognitionModel.
        <br /> A large person group is the container of the uploaded person
        data, including face recognition feature, and up to 1,000,000
        people.
        <br /> After creation, use [LargePersonGroup Person -
        Create](/docs/services/563879b61984550e40cbbe8d/operations/599adcba3a7b9412a4d53f40)
        to add person into the group, and call [LargePersonGroup -
        Train](/docs/services/563879b61984550e40cbbe8d/operations/599ae2d16ac60f11b48b5aa4)
        to get this group ready for [Face -
        Identify](/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395239).
        <br /> No image will be stored. Only the person's extracted face
        features and userData will be stored on server until [LargePersonGroup
        Person -
        Delete](/docs/services/563879b61984550e40cbbe8d/operations/599ade5c6ac60f11b48b5aa2)
        or [LargePersonGroup -
        Delete](/docs/services/563879b61984550e40cbbe8d/operations/599adc216ac60f11b48b5a9f)
        is called.
        <br/>'recognitionModel' should be specified to associate with this
        large person group. The default value for 'recognitionModel' is
        'recognition_01', if the latest model needed, please explicitly specify
        the model you need in this parameter. New faces that are added to an
        existing large person group will use the recognition model that's
        already associated with the collection. Existing face features in a
        large person group can't be updated to features extracted by another
        version of recognition model.
        * 'recognition_01': The default recognition model for [LargePersonGroup
        -
        Create](/docs/services/563879b61984550e40cbbe8d/operations/599acdee6ac60f11b48b5a9d).
        All those large person groups created before 2019 March are bonded with
        this recognition model.
        * 'recognition_02': Recognition model released in 2019 March.
        'recognition_02' is recommended since its overall accuracy is improved
        compared with 'recognition_01'.
        Large person group quota:
        * Free-tier subscription quota: 1,000 large person groups.
        * S0-tier subscription quota: 1,000,000 large person groups.

        :param large_person_group_id: Id referencing a particular large person
         group.
        :type large_person_group_id: str
        :param name: User defined name, maximum length is 128.
        :type name: str
        :param user_data: User specified data. Length should not exceed 16KB.
        :type user_data: str
        :param recognition_model: Possible values include: 'recognition_01',
         'recognition_02'
        :type recognition_model: str or
         ~azure.cognitiveservices.vision.face.models.RecognitionModel
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.MetaDataContract(name=name, user_data=user_data, recognition_model=recognition_model)

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'largePersonGroupId': self._serialize.url("large_person_group_id", large_person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'MetaDataContract')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    create.metadata = {'url': '/largepersongroups/{largePersonGroupId}'}

    def delete(
            self, large_person_group_id, custom_headers=None, raw=False, **operation_config):
        """Delete an existing large person group. Persisted face features of all
        people in the large person group will also be deleted.

        :param large_person_group_id: Id referencing a particular large person
         group.
        :type large_person_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'largePersonGroupId': self._serialize.url("large_person_group_id", large_person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/largepersongroups/{largePersonGroupId}'}

    def get(
            self, large_person_group_id, return_recognition_model=False, custom_headers=None, raw=False, **operation_config):
        """Retrieve the information of a large person group, including its name,
        userData and recognitionModel. This API returns large person group
        information only, use [LargePersonGroup Person -
        List](/docs/services/563879b61984550e40cbbe8d/operations/599adda06ac60f11b48b5aa1)
        instead to retrieve person information under the large person group.
        .

        :param large_person_group_id: Id referencing a particular large person
         group.
        :type large_person_group_id: str
        :param return_recognition_model: A value indicating whether the
         operation should return 'recognitionModel' in response.
        :type return_recognition_model: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LargePersonGroup or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.LargePersonGroup
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'largePersonGroupId': self._serialize.url("large_person_group_id", large_person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if return_recognition_model is not None:
            query_parameters['returnRecognitionModel'] = self._serialize.query("return_recognition_model", return_recognition_model, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LargePersonGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/largepersongroups/{largePersonGroupId}'}

    def update(
            self, large_person_group_id, name=None, user_data=None, custom_headers=None, raw=False, **operation_config):
        """Update an existing large person group's display name and userData. The
        properties which does not appear in request body will not be updated.

        :param large_person_group_id: Id referencing a particular large person
         group.
        :type large_person_group_id: str
        :param name: User defined name, maximum length is 128.
        :type name: str
        :param user_data: User specified data. Length should not exceed 16KB.
        :type user_data: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.NameAndUserDataContract(name=name, user_data=user_data)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'largePersonGroupId': self._serialize.url("large_person_group_id", large_person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'NameAndUserDataContract')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update.metadata = {'url': '/largepersongroups/{largePersonGroupId}'}

    def get_training_status(
            self, large_person_group_id, custom_headers=None, raw=False, **operation_config):
        """Retrieve the training status of a large person group (completed or
        ongoing).

        :param large_person_group_id: Id referencing a particular large person
         group.
        :type large_person_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TrainingStatus or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.TrainingStatus or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.get_training_status.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'largePersonGroupId': self._serialize.url("large_person_group_id", large_person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('TrainingStatus', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_training_status.metadata = {'url': '/largepersongroups/{largePersonGroupId}/training'}

    def list(
            self, start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False, **operation_config):
        """List all existing large person groups’ largePersonGroupId, name,
        userData and recognitionModel.<br />
        * Large person groups are stored in alphabetical order of
        largePersonGroupId.
        * "start" parameter (string, optional) is a user-provided
        largePersonGroupId value that returned entries have larger ids by
        string comparison. "start" set to empty to indicate return from the
        first item.
        * "top" parameter (int, optional) specifies the number of entries to
        return. A maximal of 1000 entries can be returned in one call. To fetch
        more, you can specify "start" with the last returned entry’s Id of the
        current call.
        <br />
        For example, total 5 large person groups: "group1", ..., "group5".
        <br /> "start=&top=" will return all 5 groups.
        <br /> "start=&top=2" will return "group1", "group2".
        <br /> "start=group2&top=3" will return "group3", "group4", "group5".
        .

        :param start: List large person groups from the least
         largePersonGroupId greater than the "start".
        :type start: str
        :param top: The number of large person groups to list.
        :type top: int
        :param return_recognition_model: A value indicating whether the
         operation should return 'recognitionModel' in response.
        :type return_recognition_model: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.vision.face.models.LargePersonGroup] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'str', max_length=64)
        if top is not None:
            query_parameters['top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)
        if return_recognition_model is not None:
            query_parameters['returnRecognitionModel'] = self._serialize.query("return_recognition_model", return_recognition_model, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[LargePersonGroup]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/largepersongroups'}

    def train(
            self, large_person_group_id, custom_headers=None, raw=False, **operation_config):
        """Queue a large person group training task, the training task may not be
        started immediately.

        :param large_person_group_id: Id referencing a particular large person
         group.
        :type large_person_group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.train.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'largePersonGroupId': self._serialize.url("large_person_group_id", large_person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    train.metadata = {'url': '/largepersongroups/{largePersonGroupId}/train'}
