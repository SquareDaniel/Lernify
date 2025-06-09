from flask import Blueprint, render_template
from models import Course

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/')
def home():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@courses_bp.route('/courses')
def list_courses():
    courses = Course.query.all()
    return render_template('course_list.html', courses=courses)

@courses_bp.route('/courses/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course_detail.html', course=course)