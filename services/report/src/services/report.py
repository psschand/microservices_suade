import logging
from ..exceptions import ResourceNotFound
from src.models.report import Order,Orderline
import requests 
logger = logging.getLogger(__name__)
from src import db
from sqlalchemy.sql import select
from datetime import datetime

from decimal import Decimal
        
class ReportService:
    """Report Service"""

    def get_by_id(self, id: int):
        report = Order.query.filter_by(id=id).first()
        if not report:
            logger.info("Report: Report Not found with id {id}".format(id=id))
            raise ResourceNotFound(
                message="Report Not found with id: {id}".format(id=id)
            )
        return report
    def get_by_name(self, name):
        report = Order.query.filter_by(name=name).first()
        if not report:
            logger.info("Report: Order Not found with name {name}".format(id=id))
            raise ResourceNotFound(
                message="Order Not found with name: {name}".format(name=name)
            )
        return report

    def get_all(self):
        reports = [p.to_json() for p in Order.query.order_by(Order.id.asc())]
        return reports


    def update(self, id, payload):
        report = self.get_by_id(id)
        report = Order.update(payload, commit=True)
        logger.info(
            "Report: Report with id: {id} update successfuly".format(id=id)
        )
        return report
    
    def average_discount(self):
        # result = db.session.query(Orderline).join(Order, Order.id==Orderline.product_id).all()
        # result = db.session.query(Order, Orderline)\
        # .join(Orderline,Order.id==Orderline.id)\
        # # .first() or.all()
     
        s=db.session.query(db.func.avg(Orderline.discounted_amount), Order.created_at)\
        .join(Orderline,Order.id==Orderline.id)\
        .group_by(Order.created_at).order_by(Order.created_at.desc()).first() 
    
        # print(str(round(s[0],2)))
        output = str(round(s[0],2)) if s is not None else 0 
        return output
    
    def total_discount(self):
        s=db.session.query(db.func.sum(Orderline.total_amount), Order.created_at)\
        .join(Orderline,Order.id==Orderline.id)\
        .group_by(Order.created_at).order_by(Order.created_at.desc()).first() 
    
        # print(str(round(s[0],2)))
        output = str(round(s[0],2)) if s is not None else 0 
        return output
    
    def total_customers(self):
        s=db.session.query(db.func.count(Order.customer_id), Order.created_at)\
        .join(Orderline,Order.id==Orderline.id)\
        .group_by(Order.created_at).order_by(Order.created_at.desc()).first() 
    
        # print(str(round(s[0],2)))
        output = str(round(s[0],2)) if s is not None else 0 
        return output
    
    def total_products(self):
        s=db.session.query(db.func.count(Orderline.product_id), Order.created_at)\
        .join(Orderline,Order.id==Orderline.id)\
        .group_by(Order.created_at).order_by(Order.created_at.desc()).first() 
    
        # print(str(round(s[0],2)))
        output = str(round(s[0],2)) if s is not None else 0 
        return output


report_service = ReportService()
