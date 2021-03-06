# -*- coding: utf-8 -*-
from asgs_dataset.model.asgs_feature import ASGSFeature
from asgs_dataset.view.ldapi import ASGSClassRenderer
import asgs_dataset._config as config


class ASGSFeatureRenderer(ASGSClassRenderer):
    ASGS_CLASS = config.URI_ASGSFEATURE_CLASS

    def __init__(self, request, identifier, views, *args,
                 default_view_token=None, **kwargs):
        _views = views or {}
        if identifier.startswith("http:") or identifier.startswith("https:"):
            _uri = identifier
            identifier = _uri.split('/')[-1]
        else:
            _uri = ''.join([config.URI_ASGSFEATURE_INSTANCE_BASE, identifier])
        self.identifier = identifier
        self.instance = ASGSFeature(_uri)
        kwargs.setdefault('asgs_template',
                          'asgs-'+self.instance.asgs_type+'-en.html')
        super(ASGSFeatureRenderer, self).__init__(
            request, _uri, _views, *args,
            default_view_token=default_view_token, **kwargs)


