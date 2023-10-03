from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_cors import CORS

from db import db
from models import BusinessModel
from schemas import BusinessSchema


blp = Blueprint("Businesses,", "businesses", description="Operations on businesses")
# CORS(blp)


@blp.route("/business/<int:business_id>")
class Business(MethodView):
    @blp.response(200, BusinessSchema)
    def get(self, business_id):
        business = BusinessModel.query.get_or_404(business_id)
        return business
    

    def delete(self, business_id):
        business = BusinessModel.query.get_or_404(business_id)
        db.session.delete(business)
        db.session.commit()
        return {"message": "Business deleted"}, 200

@blp.route("/business")
class BusinessList(MethodView):
    @blp.response(200, BusinessSchema(many=True))
    def get(self):
        return BusinessModel.query.all()
    

    @blp.arguments(BusinessSchema)
    @blp.response(201, BusinessSchema)
    def post(self, business_data):
        business = BusinessModel(**business_data)
        try:
            db.session.add(business)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="Business name already exists."
            )
        except SQLAlchemyError:
            abort(500, message="An error occured while creating the store.")

        return business