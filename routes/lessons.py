from flask import Blueprint, render_template
from models import Lesson

lessons_bp = Blueprint('lessons', __name__)

@lessons_bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>')
def lesson_detail(course_id, lesson_id):
    lesson = Lesson.query.filter_by(id=lesson_id, course_id=course_id).first_or_404()
    prev_lesson = Lesson.query.filter(Lesson.course_id == course_id, Lesson.id < lesson_id).order_by(Lesson.id.desc()).first()
    next_lesson = Lesson.query.filter(Lesson.course_id == course_id, Lesson.id > lesson_id).order_by(Lesson.id).first()
    return render_template('lesson.html', lesson=lesson, prev=prev_lesson, next=next_lesson)