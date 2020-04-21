# -*- coding: utf-8 -*-
import xadmin
from .models import LogsEntry

class LogsEntryAdmin(object):
    list_display = ["time_added", "user", "object_repr", "action_flag", "message"]

xadmin.site.register(LogsEntry, LogsEntryAdmin)