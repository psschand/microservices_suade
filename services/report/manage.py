


import sys
import unittest
from logging.config import dictConfig
from datetime import datetime
# import coverage
from flask.cli import FlaskGroup
from src import create_app, db
from src.models.report import Order,Orderline

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
# COV = coverage.coverage(
#     branch=True,
#     include='src/*',
#     omit=[
#         'tests/*',
#         'src/config.py',
#     ]
# )
# COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


# @cli.command()
# def cov():
#     """Runs the unit tests with coverage."""
#     tests = unittest.TestLoader().discover('tests')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         COV.stop()
#         COV.save()
#         print('Coverage Summary:')
#         COV.report()
#         COV.html_report()
#         COV.erase()
#         return 0
#     sys.exit(result)
    
@cli.command('populate_db')
def populate_db():
    """Populate the database with report."""

    db.session.add(Order(vendor_id='vend1',customer_id='cust1',created_at=datetime(2020, 5, 4)))
    db.session.add(Order(vendor_id='vend2',customer_id='cust2',created_at=datetime(2016, 2, 3)))
    db.session.add(Order(vendor_id='vend3',customer_id='cust3',created_at=datetime(2017, 5, 4)))
    db.session.add(Order(vendor_id='vend4',customer_id='cust4',created_at=datetime(2019, 8, 8)))
    db.session.add(Order(vendor_id='vend5',customer_id='cust5',created_at=datetime(2020, 5, 6)))
    db.session.add(Order(vendor_id='vend6',customer_id='cust6',created_at=datetime(2018, 6, 4)))

    db.session.add(Orderline(product_id=1,product_description='someproduct',product_price=5000,discount_rate=1,quantity=1,full_price_amount=3,discounted_amount=50,vat_amount=45,total_amount=5456))
    db.session.add(Orderline(product_id=2,product_description='someproduct',product_price=5000,discount_rate=1,quantity=1,full_price_amount=3,discounted_amount=50,vat_amount=45,total_amount=5456))
    db.session.add(Orderline(product_id=2,product_description='someproduct',product_price=5000,discount_rate=1,quantity=1,full_price_amount=3,discounted_amount=50,vat_amount=45,total_amount=5456))
    db.session.add(Orderline(product_id=3,product_description='someproduct',product_price=5000,discount_rate=1,quantity=1,full_price_amount=3,discounted_amount=50,vat_amount=45,total_amount=5456))
    db.session.add(Orderline(product_id=2,product_description='someproduct',product_price=5000,discount_rate=1,quantity=1,full_price_amount=3,discounted_amount=50,vat_amount=45,total_amount=5456))
    db.session.add(Orderline(product_id=4,product_description='someproduct',product_price=5000,discount_rate=1,quantity=1,full_price_amount=3,discounted_amount=50,vat_amount=45,total_amount=5456))
    
    
    db.session.commit()


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
