from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class ActionType(str, Enum):
    LIKE = "LIKE"
    FOLLOW = "FOLLOW"
    BLOCK = "BLOCK"
    BIO_UPDATE = "BIO_UPDATE"
    MEDIA_UPLOAD = "MEDIA_UPLOAD"


class WarmupSession(BaseModel):
    session_id: str
    count: int
    start_time: str
    end_time: str
    isSessionCompleted: bool


class WarmupAction(BaseModel):
    action_type: ActionType
    sessions: List[WarmupSession]
    isActionCompleted: bool


class WarmupConfiguration(BaseModel):
    day_of_week: str
    actions: List[WarmupAction]
    isAllActionsCompleted: bool


class SessionAction(BaseModel):
    action_id: str
    action_type: ActionType
    target_usernames: Optional[List[str]] = None


class Session(BaseModel):
    session_id: str
    start_time: str
    end_time: str
    actions: List[SessionAction]


class DailyAction(BaseModel):
    date: str
    sessions: List[Session]


class Account(BaseModel):
    username: str
    password: str
    phoneNumber: Optional[str]
    createdTimestamp: datetime
    email: str
    followers: int
    following: int
    posts: int
    last_login: datetime
    created_at: datetime
    warmup_phase: bool
    warmup_configuration: List[WarmupConfiguration]
    daily_actions: List[DailyAction]

    class Config:
        from_attributes = True
