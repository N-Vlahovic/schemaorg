# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.612198
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .alignment_object import AlignmentObject
from .course_instance import CourseInstance
from .creative_work import CreativeWork
from .educational_occupational_credential import EducationalOccupationalCredential
from .integer import Integer
from .learning_resource import LearningResource
from .structured_value import StructuredValue
from .text import Text
from .url import URL


@dataclass
class Course(CreativeWork, LearningResource):
    courseCode: Text | None
    coursePrerequisites: AlignmentObject | Course | Text | None
    educationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None
    hasCourseInstance: CourseInstance | None
    numberOfCredits: Integer | StructuredValue | None
    occupationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None
