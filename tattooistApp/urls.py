from django.urls import path

from . import views

urlpatterns = [
    path("create_portfolio", views.create_portfolio_view, name="create_portfolio"),
    path("create_review/<int: tattooist_id>", views.create_review, name="create_review"),
    path("detail_portfolio/<int: tattooist_id>/<int: portfolio_id>", views.detail_portfolio_view, name="detail_portfolio"),
    path("message/<int: tattooist_id>", views.message_view, name="message"),
    path("modify_portfolio/<int: tattooist_id>/<int: portfolio_id>", views.modify_portfolio_view, name="modify_portfolio"),
    path("modify_review_view/<int: tattooist_id>/<int: review_id>", views.modify_review_view,name="modify_review"),
    path("report", views.report_view, name="report"),
]