from passlib.hash import pbkdf2_sha256
from helpers.models import ValidationResult


class PasswordService:
    def hash(self, password):
        hash = pbkdf2_sha256.hash(password)
        return hash

    def verify(self, password, hashed):
        return pbkdf2_sha256.verify(password, hashed)

    def validate_rules(self, password):
        # TODO: validate password rules.
        return ValidationResult(
            valid=True
        )


password_service = PasswordService()
