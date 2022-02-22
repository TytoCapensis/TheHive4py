import mimetypes

from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.session import TheHiveSession


class EndpointBase:
    def __init__(self, session: TheHiveSession):
        self._session = session

    def _fileinfo_from_filepath(self, filepath: str) -> tuple:
        filename = filepath.split("/")[-1]
        mimetype = mimetypes.guess_type(filepath)
        filestream = open(filepath, "rb")

        return (filename, filestream, mimetype)

    def _build_subquery(
        self,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
    ) -> QueryExpr:

        subquery: QueryExpr = []
        if filters:
            subquery = [*subquery, {"_name": "filter", **filters}]
        if sortby:
            subquery = [*subquery, {"_name": "sort", **sortby}]
        if paginate:
            subquery = [*subquery, {"_name": "page", **paginate}]

        return subquery
