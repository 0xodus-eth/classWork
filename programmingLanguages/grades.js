function processStudentMarks(students) {

    function assignGrade(marks) {
        const average = marks / students[0].subjects.length;
        if (average >= 90) {
            return 'A';
        } else if (average >= 80) {
            return 'B';
        } else if (average >= 70) {
            return 'C';
        } else if (average >= 60) {
            return 'D';
        } else {
            return 'F';

        }
    }

    // Calculate total marks, average marks and grade for each student
    students.forEach(student => {
        student.totalMarks = student.subjects.reduce((sum, mark) => sum + mark, 0);
        student.averageMarks = student.totalMarks / student.subjects.length;
        student.grade = assignGrade(student.totalMarks);
    });


    const totalMarks = students.reduce((sum, student) => sum + student.totalMarks, 0);
    const meanMarks = totalMarks / students.length;

    const totalGrades = students.map(student => student.grade.charCodeAt(0)); // Convert grade to ASCII code
    const meanGrade = String.fromCharCode(Math.round(totalGrades.reduce((sum, grade) => sum + grade, 0) / students.length));

    // Create CSV string
    let csvContent = "Name,Total Marks,Average Marks,Grade\n";
    students.forEach(student => {
        csvContent += `${student.name},${student.totalMarks},${student.averageMarks},${student.grade}\n`;
    });
    csvContent += `,,${meanMarks},${meanGrade}`;

    return csvContent;
}


const students = [
    { name: 'Alice', subjects: [85, 92, 78] },
    { name: 'Bob', subjects: [75, 68, 80] },
    { name: 'Charlie', subjects: [90, 95, 88] }
];

const csvOutput = processStudentMarks(students);
console.log(csvOutput);