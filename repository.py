from connection import engine


def get_all_categories():
    with Session(autoflush=False, bind=engine) as db:
        categories = db.query().all()

    return categories
