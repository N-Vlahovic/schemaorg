# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597827
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .diet import Diet
from .distance import Distance
from .exercise_plan import ExercisePlan
from .person import Person
from .place import Place
from .play_action import PlayAction
from .sports_activity_location import SportsActivityLocation
from .sports_event import SportsEvent
from .sports_team import SportsTeam
from .text import Text


@dataclass
class ExerciseAction(PlayAction):
    course: Place | None
    diet: Diet | None
    distance: Distance | None
    exerciseCourse: Place | None
    exercisePlan: ExercisePlan | None
    exerciseRelatedDiet: Diet | None
    exerciseType: Text | None
    fromLocation: Place | None
    opponent: Person | None
    sportsActivityLocation: SportsActivityLocation | None
    sportsEvent: SportsEvent | None
    sportsTeam: SportsTeam | None
    toLocation: Place | None
