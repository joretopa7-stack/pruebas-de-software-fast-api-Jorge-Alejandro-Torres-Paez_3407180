from datetime import datetime, time, date, timedelta
from app.exceptions import (
    InvalidCustomerError,
    InvalidServiceError,
    InvalidDurationError,
    InvalidReservationDateError,
    InvalidReservationTimeError,
    DuplicateReservationError,
)

ALLOWED_SERVICES = ["ASESORIA", "SOPORTE", "DESARROLLO"]

ALLOWED_DURATIONS = [30, 60, 90]

OPENING_TIME = time(9, 0)  # 9:00 AM
CLOSING_TIME = time(17, 0)  # 5:00 PM


def validate_customer_name(customer_name: str) -> str:
    normalized_name = customer_name.strip() # REMUEVE EL ESPACIO EN BLANCO AL PRINCIPIO Y AL FINAL DE LA CADENA

    if len(normalized_name) < 3:
        raise InvalidCustomerError("Customer name must be at least 3 characters long.")
    return normalized_name

def validate_service(service: str) -> str:
    normalized_service = service.strip().upper() # REMUEVE EL ESPACIO EN BLANCO AL PRINCIPIO Y AL FINAL DE LA CADENA

    if normalized_service not in ALLOWED_SERVICES:
        raise InvalidServiceError(f"Service must be one of {ALLOWED_SERVICES}.")
    return normalized_service

def validate_duration(duration: int) -> int:
    if duration not in ALLOWED_DURATIONS:
        raise InvalidDurationError(f"Duration must be one of {ALLOWED_DURATIONS}.")
    return duration

def validate_reservation_date(reservation_date: date) -> date:
    today = date.today()
    if reservation_date < today:
        raise InvalidReservationDateError("Reservation date cannot be in the past.")

    if reservation_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        raise InvalidReservationDateError("Reservation date cannot be on a weekend.")

    return reservation_date

def validate_reservation_time(reservation_time: time) -> time:
    if not (OPENING_TIME <= reservation_time <= CLOSING_TIME):
        raise InvalidReservationTimeError(
            f"Reservation time must be between {OPENING_TIME.strftime('%I:%M %p')} and {CLOSING_TIME.strftime('%I:%M %p')}."
        )
    return reservation_time



