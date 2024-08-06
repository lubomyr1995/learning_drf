import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclasses.user_dataclass import User
from core.enums.template_enum import TemplateEnum
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject: str = '') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def activate_account(cls, user: User) -> None:
        token = JWTService.create_token(user, ActivateToken)
        url = f'{os.environ.get('FRONTEND_URL')}/{token}'
        cls.__send_email(
            to=user.email,
            template_name=TemplateEnum.ACTIVATE.template_name,
            context={'name': user.profile.name, 'url': url},
            subject=TemplateEnum.ACTIVATE.ACTIVATE.name_subject
        )

    @classmethod
    def recovery_password(cls, user: User) -> None:
        token = JWTService.create_token(user, RecoveryToken)
        url = f'{os.environ.get('FRONTEND_URL')}/recovery/{token}'
        cls.__send_email(
            to=user.email,
            template_name=TemplateEnum.RECOVERY.template_name,
            context={'name': user.profile.name, 'url': url},
            subject=TemplateEnum.RECOVERY.name_subject
        )
