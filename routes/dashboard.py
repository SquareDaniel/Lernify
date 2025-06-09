from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Course

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    if current_user.is_teacher:
        courses = current_user.courses
        return render_template('dashboard_teacher.html', courses=courses)
    else:
        courses = Course.query.all()
        return render_template('dashboard_student.html', courses=courses)