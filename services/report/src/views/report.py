import logging

from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse

from ..services.report import report_service
reports_blueprint = Blueprint('reports', __name__)
api = Api(reports_blueprint)
logger = logging.getLogger(__name__)


@reports_blueprint.route('/reports/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


class ReportResources(Resource):
    """Report resources"""

    def get(self):
        """Get all reports """
        response = dict()
        reports = report_service.get_all()
        # response['results'] = reports
        response['count of orders'] = len(reports)
        response['total discount'] = report_service.total_discount()
        response['total products'] = report_service.total_products()
        response['total customers'] = report_service.total_customers()
        response['average discount'] = report_service.average_discount()
        return response, 200


class ReportDetailResources(Resource):
    """Report Detail resources"""

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'name', type=str, location='json', required=True
        )
        super(ReportDetailResources, self).__init__()

    def get(self, report_id):
        """Get detail report"""
        response = dict()
        report = report_service.get_by_id(id=report_id)
        response = report.to_json()
        return response, 200

    # def put(self, report_id):
    #     response = dict()
    #     data = self.parser.parse_args()
    #     if not data:
    #         err_msg = "Report: Bad request in update report {}, name field is mandatory".format(
    #             report_id
    #         )
    #         response['message'] = err_msg
    #         response['error'] = True
    #         return response, 400
    #     report = report_service.update(report_id, data)
    #     response['status'] = 'success'
    #     response['message'] = 'Report was updated!'
    #     response["data"] = report.to_json()
    #     return response, 200

# class ReportTemperatures(Resource):
#     """Report resources"""

    # def get(self):
    #     """Get all reports """
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('location')
    #     parser.add_argument('report')
    #     parser.add_argument('year', type=int, help='year cannot be converted')
        
    #     args = parser.parse_args()
    #     response = dict()
    #     location_arg= args['location']
    #     year_arg = args['year']
    #     report_arg= args['report']
    #     report=report_service.get_by_name(report_arg)
    #     month=report.to_json()["date"].split("-")[1]
    #     day=report.to_json()["date"].split("-")[2]
        
    #     woeid=report_service.get_woeid(location_arg)
        
        
        
    #     x,y=report_service.MaxMinReport(woeid,year_arg,month,day)
    #     response['result'] = report.to_json()
    #     response['year'] = year_arg
    #     response['month'] = month
    #     response['day'] = day
    #     response['woeid'] = woeid
    #     response['Max_Temperature'] = round(x, 2)
    #     response['Min_Temperature'] = round(y, 2)
    #     response['arguments'] = args
    #     return response, 200

# class ReportHighs(Resource):
#     """Report resources"""

#     def get(self):
#         """Get all reports """
#         parser = reqparse.RequestParser()
#         parser.add_argument('location')
#         parser.add_argument('report')
        
#         args = parser.parse_args()
#         response = dict()
#         location_arg= args['location']
#         report_arg= args['report']
#         woeid=report_service.get_woeid(location_arg)
#         dict_hol=report_service.ReportHighs(woeid,12,25)
#         max_key = max(dict_hol, key=dict_hol.get)
#         response['year'] = max_key
#         response['Max_Temperature'] = dict_hol[max_key]
#         response['results_year_vs_temp'] = dict_hol
#         return response, 200    

api.add_resource(ReportResources, '/v1/reports/')
api.add_resource(ReportDetailResources, '/v1/reports/<report_id>')
# api.add_resource(ReportTemperatures, '/v1/task1')
# api.add_resource(ReportHighs, '/v1/task2/')
