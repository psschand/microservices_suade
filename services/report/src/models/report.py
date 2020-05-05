from src import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor_id = db.Column(db.String, nullable=False)
    customer_id=db.Column(db.String, nullable=False)
    created_at=db.Column(db.DateTime, nullable=False)

    def __init__(self, vendor_id,customer_id,created_at):
        self.vendor_id = vendor_id
        self.customer_id = customer_id
        self.created_at = created_at

    def __repr__(self):
        return "# order ID:{} vendor - {} customer - {} date {}".format(self.id, self.vendor_id,self.customer_id,self.created_at)

    def to_json(self):
        return {
            'id': self.id,
            'vendor_id': self.vendor_id,
            'customer_id': self.customer_id,
            'created_at': self.created_at.strftime("%m/%d/%Y"),
        }

    def save(self, commit=True):
        """ save """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def update(self, payload, commit=True):
        for attr, value in payload.items():
            setattr(self, attr, value)
        return commit and self.save() or self
    
class Orderline(db.Model):
    __tablename__ = 'orderlines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, nullable=False)
    product_description=db.Column(db.String, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    discount_rate=db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    full_price_amount=db.Column(db.Integer, nullable=False)
    discounted_amount = db.Column(db.Integer, nullable=False)
    vat_amount=db.Column(db.Integer, nullable=False)
    total_amount=db.Column(db.Integer, nullable=False)


    def __init__(self, product_id,product_description,product_price,discount_rate,quantity,full_price_amount,discounted_amount,vat_amount,total_amount):
        self.product_id=product_id
        self.product_description=product_description
        self.product_price=product_price
        self.discount_rate=discount_rate
        self.quantity=quantity
        self.full_price_amount=full_price_amount
        self.discounted_amount=discounted_amount
        self.vat_amount=vat_amount
        self.total_amount=total_amount

    def __repr__(self):
        return "# order ID:{} product id- {} description - {}".format(self.id, self.product_id,self.product_description)

    def to_json(self):
        return {
            'id': self.id,
            'product ID': self.name,
            'Description': self.date,
            'product_id':self.product_id,
            'product_description': self.product_description,
            'product_price':self.product_price,
            'discount_rate':self.discount_rate,
            'quantity':self.quantity,
            'full_price_amount':self.full_price_amount,
            'discounted_amount':self.discounted_amount,
            'vat_amount':self.vat_amount,
            'total_amount':self.total_amount
        }

    def save(self, commit=True):
        """ save """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def update(self, payload, commit=True):
        for attr, value in payload.items():
            setattr(self, attr, value)
        return commit and self.save() or self    




