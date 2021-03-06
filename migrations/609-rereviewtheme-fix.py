#!/usr/bin/env python

import logging

from addons.models import Addon
from mkt.reviewers.models import RereviewQueueTheme


log = logging.getLogger('z.task')


def run():
    """Delete RereviewQueueTheme objects whose themes did not cascade delete
    with add-on. Came about from setting on_delete to invalid value in
    model."""
    for rqt in RereviewQueueTheme.objects.all():
        try:
            rqt.theme.addon
        except Addon.DoesNotExist:
            log.info('[Theme %s] Deleting rereview_queue_theme,'
                     ' add-on does not exist.' % rqt.theme.id)
            rqt.delete()
