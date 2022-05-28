# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.583335
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.diet import Diet
from models.distance import Distance
from models.exercise_plan import ExercisePlan
from models.person import Person
from models.place import Place
from models.play_action import PlayAction
from models.sports_activity_location import SportsActivityLocation
from models.sports_event import SportsEvent
from models.sports_team import SportsTeam
from models.text import Text


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
