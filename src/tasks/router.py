from fastapi import APIRouter
from tasks.tasks import send_message_to_email

router = APIRouter(
    prefix='/report'
)


@router.get("/dashboard")
def get_report():
    send_message_to_email()

    return {
        'status': 200,
        'data': 'Письмо отправлена',
        'details': []
    }
