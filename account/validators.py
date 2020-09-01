import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("رمز ‌عبور حداقل باید حاوی یک عدد مابین 0-9 باشد."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "رمز ‌عبور حداقل باید حاوی یک عدد مابین 0-9 باشد."
        )


class NumericPasswordValidator:
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("رمز ‌عبور حداقل باید حاوی یکی از حروف انگلیسی باشد."),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _('رمز ‌عبور حداقل باید حاوی یکی از حروف انگلیسی باشد.')

class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("رمز ‌عبور حداقل باید حاوی یکی از کاراکتر‌های مقابل باشد " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "رمز ‌عبور حداقل باید حاوی یکی از کاراکتر‌های مقابل باشد " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )