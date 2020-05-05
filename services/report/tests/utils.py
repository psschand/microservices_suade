from src import db
from src.models.report import Report


def add_report(name):
    report = Report(
        name=name
    )
    db.session.add(report)
    db.session.commit()
    return report
