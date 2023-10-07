from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from config.database import (
get_db_connection,
)
