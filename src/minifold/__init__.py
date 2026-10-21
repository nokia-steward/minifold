#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of the minifold project
# https://github.com/nokia/minifold

"""Top-level package."""

__author__ = "Marc-Olivier Buob"
__maintainer__ = "Marc-Olivier Buob"
__email__ = "marc-olivier.buob@nokia-bell-labs.com"
__copyright__ = "Copyright (C) 2018, Nokia"
__license__ = "BSD-3"
__version__ = '0.10.4'  # Use single quotes for bumpversion (see setup.cfg)


from .binary_predicate import OPERATORS, OPERATORS_TO_STR, BinaryPredicate
from .cached import CachedEntriesConnector, JsonCachedConnector, PickleCachedConnector
from .cache import (
    DEFAULT_CACHE_STORAGE_BASE_DIR,
    CacheConnector,
    JsonCacheConnector,
    PickleCacheConnector,
    make_cache_dir,
)
from .closure import is_multiple_key, closure, minimal_cover
from .config import DEFAULT_MINIFOLD_CONFIG, Config
from .connector import Connector
from .connector_util import show_some_values
from .count import CountConnector, count, count_gen
from .country import country_code_to_name
from .csv import CsvConnector, CsvModeEnum
from .dblp import DBLP_API_URL, DBLP_ALIASES, DblpConnector
from .dict_util import reverse_dict, freeze_dict
from .doc_type import DocType, doc_type_to_html
from .download import DownloadConnector, download, downloads, now, trim_http
from .entries_connector import EntriesConnector
from .filesystem import check_writable_directory, ctime, find, mkdir, mtime, rm
from .for_each import ForEachFilter, for_each_sub_entry
from .google_scholar import GoogleScholarConnector
from .group_by import GroupByConnector, group_by
from .hal import HAL_API_URL, HAL_ALIASES, HalConnector
from .html import (
    connector_to_html, entry_to_html, entries_to_html, html, print_error, value_to_html
)
from .html_table import HtmlTableConnector, HtmlTableParser, html_table
from .ipynb import in_ipynb
from .join_if import (
    INNER_JOIN, LEFT_JOIN, RIGHT_JOIN, FULL_OUTER_JOIN, merge_dict,
    JoinIfConnector, inner_join_if, left_join_if, right_join_if, full_outer_join_if
)
from .json import JsonConnector, JsonFileConnector
from .lambdas import LambdasConnector, lambdas
from .ldap import LdapConnector
from .lexical_cast import cast_bool, cast_none, lexical_cast, lexical_casts
from .limit import LimitConnector, limit
from .log import (
    RED, GREEN, YELLOW, BLUE, PINK, CYAN, GRAY,
    BOLD, UNDERLINED, BLINKING, HIGHLIGHTED,
    Log
)
from .mongo import MongoConnector
from .natural_join import NaturalJoinConnector, are_naturally_joined, natural_join
from .proxy import Proxy, proxy_enable, proxy_disable, make_session, proxy_enable_localhost
from .query import (
    ACTION_CREATE, ACTION_READ, ACTION_UPDATE, ACTION_DELETE,
    SORT_ASC, SORT_DESC, Query
)
from .rename import RenameConnector, rename, rename_query
from .request_cache import install_cache
from .search import (
    SearchFilter, search,
    equals, contains, lower_case_contains, lower_case_equals, contains_words
)
from .select import SelectConnector, select
from .singleton import Singleton
from .sort_by import SortByConnector, sort_by
from .strings import (
    to_international_string, remove_punctuation,
    remove_html_tags, remove_html_escape_sequences,
    remove_latex_escape_sequence,
    to_canonic_string, to_canonic_fullname, unicode_to_utf8
)
from .twitter import TwitterConnector, tweet_to_dict
from .union import UnionConnector, union
from .unique import UniqueConnector, unique
from .unnest import UnnestConnector, unnest
from .where import WhereConnector, where
