import Regrex_Practise_Code as r1
import sqlalchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class emails_Table(Base):
    __tablename__ = 'emails_Table'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    sender_name = sqlalchemy.Column(sqlalchemy.String)
    sender_email_address = sqlalchemy.Column(sqlalchemy.String)
    recipient_address = sqlalchemy.Column(sqlalchemy.String)
    date_sent = sqlalchemy.Column(sqlalchemy.String)
    subject = sqlalchemy.Column(sqlalchemy.String)
    email_body = sqlalchemy.Column(sqlalchemy.String)


# Replace 'your_database_path.db' with the actual path to your SQLite database file
database_url = 'sqlite:///your_database_path.db'
engine = sqlalchemy.create_engine(database_url)

# Create the tables defined in the models
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

for i, email in enumerate(r1.emails, 1):
    sender_name = r1.regrex_python_on_names(email.strip(), True)
    sender_address = r1.python_regrex_on_emails(email.strip(), "Sender", True)
    recipient_address = r1.python_regrex_on_emails(email.strip(), "recipient_address", True)
    date_sent = r1.email_date(email.strip(), True)
    subject = r1.email_subject(email.strip(), True)
    email_body = r1.body_email(email.strip(), True)
    if isinstance(sender_address, list):
        while isinstance(sender_address, list):
            sender_address = sender_address[0] if len(sender_address) > 0 else ""
    if isinstance(recipient_address, list):
        while isinstance(recipient_address, list):
            recipient_address = recipient_address[0] if len(recipient_address) > 0 else ""
    new_user = emails_Table(sender_name=sender_name, sender_email_address=sender_address,
                            recipient_address=recipient_address, date_sent=date_sent, subject=subject,
                            email_body=email_body)
    session.add(new_user)
session.commit()
print("done")
