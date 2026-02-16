from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Achievement, Category
from .forms import StudentForm, AchievementForm 

# 1. View List of Students 
def student_list(request):
    students = Student.objects.all() #Select * from table_name 
    return render(request, 'student_list.html', {'students': students})

# 2. Add New Student 
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() #Inserting student
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# 3. View Individual Student + Achievements 
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    achievements = Achievement.objects.filter(student=student) # SELECT * FROM Achievement WHERE student_id = pk
    return render(request, 'student_details.html', {'student': student, 'achievements': achievements})

# 4. Update Student Details 
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save() # UPDATE Student SET ... WHERE id = pk
            return redirect('student_detail', pk=pk)
    return render(request, 'student_form.html', {'form': StudentForm(instance=student)})

# 5. Delete Student 
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete() # DELETE FROM Student WHERE id = pk
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'object': student})

# 6. Add Achievement (5 Marks)
def add_achievement(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.student = student
            achievement.save()
            return redirect('student_detail', pk=student_id)
    return render(request, 'achievement_form.html', {'form': AchievementForm()})

# 7. Update Achievement Status (Approved/Rejected) (5 Marks)
def update_achievement_status(request, pk, status):
    achievement = get_object_or_404(Achievement, pk=pk)
    if status in ['Approved', 'Rejected']:
        achievement.status = status
        achievement.save() # UPDATE Achievement SET status = ...
    return redirect('student_detail', pk=achievement.student.id)

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        next_page = request.GET.get('next') 
        if next_page:
            return redirect(next_page)
        return redirect('add_category') # Go back to home after adding
    categories = Category.objects.all() # Get all categories
    return render(request, 'category_form.html', {'categories': categories})

# 2. Update Category View
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        
        # --- CHANGE THIS LINE ---
        # If description is empty, save "No Description Provided" instead of crashing
        category.description = request.POST.get('description') or "No Description Provided" 
        
        category.save()
        return redirect('add_category')
    
    return render(request, 'category_update.html', {'category': category})

# 3. Delete Category View
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('add_category')

def master_report(request):
    # This acts like: SELECT * FROM Achievement JOIN Student JOIN Category
    achievements = Achievement.objects.select_related('student', 'category').all()
    return render(request, 'master_report.html', {'achievements': achievements})
