import pytest
from datetime import date,time

from app.exceptions import InvalidCustomerError
#validacion del nombre
from app.validators import validate_customer_name
#validacion de servicios
from app.exceptions import InvalidServiceError
from app.validators import validate_service
#validacion duracion
from app.exceptions import InvalidDurationError
from app.validators import validate_duration
#validacion fecha de recervacion
from app.exceptions import InvalidReservationDateError
from app.validators import validate_reservation_date

#validacion hora de reservacion
from app.exceptions import InvalidReservationTimeError
from app.validators import validate_reservation_time

#test nombre
def test_validate_customer_name_removes_whitespace_and_validates_length():
    result = validate_customer_name("  John Doe  ")
    assert result == "John Doe"


def test_validate_customer_name_rejects_short_names():
    with pytest.raises(InvalidCustomerError, match="Customer name must be at least 3 characters long."):
        validate_customer_name("Jo")

#test servicio
def test_validate_service_function_positive():
    assert validate_service("ASESORIA") == "ASESORIA"
    assert validate_service("SOPORTE") == "SOPORTE"
    assert validate_service("DESARROLLO") == "DESARROLLO"


def test_validate_service_function_negative():
  with pytest.raises(InvalidServiceError, match="Service must be one of"):
      validate_service("The final service validation verification process concludes successfully.")

#test duracion

def test_validate_duration_consult_positive():
    assert validate_duration(30) == (30)
    assert validate_duration(60) == (60)
    assert validate_duration(90) == (90)

def test_validate_duration_consult_negative():
    with pytest.raises(InvalidDurationError, match="Duration must be one of"):
        validate_duration(45)

#test fecha de reservacion 

def test_validate_reservation_date_positive_today():
    reservation = date(2026, 8, 12)
    assert validate_reservation_date(reservation) == reservation


def test_validate_reservation_date_negative():
    with pytest.raises(InvalidReservationDateError,match="Reservation date cannot be on a weekend."):
        validate_reservation_date(date(2028, 1, 1))


#test hora de reservacion


def test_validate_reservation_time_positive():
    reservation_time = time(10, 30)

    result = validate_reservation_time(reservation_time)

    assert result == reservation_time


def test_validate_reservation_time_negative():
    with pytest.raises(
        InvalidReservationTimeError,
        match="Reservation time must be between"
    ):
        validate_reservation_time(time(20, 0))
