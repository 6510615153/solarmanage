from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__) # Get a logger for this module

def send_custom_email(subject, message, recipient_email, html_message=None):
    """
    Sends a custom email using Django's send_mail function.

    Args:
        subject (str): The subject of the email.
        message (str): The plain text content of the email.
        recipient_email (str or list): The email address(es) of the recipient(s).
                                       Can be a single string or a list of strings.
        html_message (str, optional): The HTML content of the email. If provided,
                                     the plain text message will be used as a fallback.
    """
    from_email = settings.DEFAULT_FROM_EMAIL # Use DEFAULT_FROM_EMAIL for consistency
                                            # (you should set this in settings.py)

    # Ensure recipient_email is a list
    if isinstance(recipient_email, str):
        recipient_list = [recipient_email]
    elif isinstance(recipient_email, (list, tuple)):
        recipient_list = recipient_email
    else:
        logger.error(f"Invalid recipient_email type: {type(recipient_email)}")
        return False # Indicate failure

    try:
        send_mail(
            subject,
            message,
            from_email, # Sender
            recipient_list, # List of manager that recieved
            html_message=html_message, # Optional HTML content
            fail_silently=False # Raise exceptions on failure
        )
        logger.info(f"Email '{subject}' successfully sent to {', '.join(recipient_list)}")
        return True # Indicate success
    except Exception as e:
        logger.error(f"Failed to send email '{subject}' to {', '.join(recipient_list)}: {e}")
        return False # Indicate failure